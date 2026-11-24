"""Run every lesson and report which ones pass.

A lesson passes when it exits without an error AND the last line it prints is
'All checks passed.' (every lesson ends by printing that line).

Usage (works from any folder):
    python3 check_lessons.py          # checks every NN_group/NN_lesson.py next to this file
    python3 check_lessons.py ROOT     # checks ROOT/NN_group/NN_lesson.py instead
"""
import re
import subprocess
import sys
from pathlib import Path

SUCCESS_LINE = 'All checks passed.'
SAMPLE_INPUT = 'Ada\n'  # typed into any lesson that calls input()
TIMEOUT_SECONDS = 10


def error_summary(stderr):
    """Keep the end of a traceback: the last 'File ..., line N' line onwards.

    The folder part of the path is dropped, and so are the ^^^ marker lines
    that newer Pythons print under the failing code.
    """
    lines = stderr.strip().splitlines()
    file_lines = [i for i, line in enumerate(lines) if line.lstrip().startswith('File "')]
    start = file_lines[-1] if file_lines else max(len(lines) - 3, 0)
    kept = []
    for line in lines[start:]:
        if not line.strip().strip('^~'):
            continue
        kept.append(re.sub(r'File ".*?([^/\\]+)", line', r'File "\1", line', line))
    return '\n'.join(kept)


def check(lesson):
    """Run one lesson. Return None if it passed, otherwise why it failed."""
    try:
        run = subprocess.run(
            [sys.executable, lesson.name],
            cwd=str(lesson.parent),
            input=SAMPLE_INPUT,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        return f'timed out after {TIMEOUT_SECONDS}s'
    if run.returncode != 0:
        return error_summary(run.stderr)
    lines = run.stdout.strip().splitlines()
    if not lines or lines[-1].strip() != SUCCESS_LINE:
        return f"the last line printed was not '{SUCCESS_LINE}'"
    return None


def main(argv):
    if argv:
        root = Path(argv[0]).resolve()
    else:
        root = Path(__file__).resolve().parent
    lessons = sorted(root.glob('[0-9][0-9]_*/[0-9][0-9]_*.py'))
    if not lessons:
        print(f'no lessons found under {root}')
        return 1

    passed = 0
    for lesson in lessons:
        name = lesson.relative_to(root).as_posix()
        reason = check(lesson)
        if reason is None:
            passed += 1
            print('PASS', name)
        else:
            print('FAIL', name)
            for line in reason.splitlines():
                print('    ' + line)

    print(f'{passed}/{len(lessons)} lessons passed')
    return 0 if passed == len(lessons) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
