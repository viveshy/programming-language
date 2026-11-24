package main

import "fmt"

func main() {

	/*________ARRAY__________*/
	// Array in Go has fixed length
	var agesOne [3]int = [3]int{20, 25, 27}
	var agesTwo = [3]int{20, 25, 85}
	names := [4]string{"Batman", "Shadow", "Dark Knight", "Cape Crusader"}

	fmt.Println(agesOne)
	fmt.Println(agesTwo)
	fmt.Println(names)

	names[0] = "The Batman"
	fmt.Println(names)

	// find length of array
	fmt.Println(len(agesOne))

	/*________SLICES (they use an array under the hood)_______*/
	var scores = []int{1, 2, 3, 4, 5}
	fmt.Println(scores, len(scores))

	scores = append(scores, 85)

	fmt.Println(scores, len(scores))

	// Slice expressions: scores[a:b] takes positions a up to, but not including, b
	sliceOne := scores[1:3]
	sliceTwo := scores[2:]
	sliceThree := scores[:3]
	fmt.Println(sliceOne)
	fmt.Println(sliceTwo)
	fmt.Println(sliceThree)

	// A slice expression does not copy anything: sliceThree shares the array under scores.
	// That array still has room, so append writes 77 into it and overwrites scores[3]
	// (and the same element seen through sliceTwo).
	sliceThree = append(sliceThree, 77)
	fmt.Println(sliceThree)       // [1 2 3 77]
	fmt.Println(scores, sliceTwo) // [1 2 3 77 5 85] [3 77 5 85]
}
