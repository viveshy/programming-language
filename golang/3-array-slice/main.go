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

	/*________SLICES (they uses array undr the hood)_______*/
	var scores = []int{1, 2, 3, 4, 5}
	fmt.Println(scores, len(scores))

	scores = append(scores, 85)

	fmt.Println(scores, len(scores))

	// ranges in slice.
	// format of range [a:b] where position a is inclusive and b is exclusive
	rangeOne := scores[1:3]
	rangeTwo := scores[2:]
	rangeThree := scores[:3]
	fmt.Println(rangeOne)
	fmt.Println(rangeTwo)
	fmt.Println(rangeThree)

	rangeThree = append(rangeThree, 77)
	fmt.Println(rangeThree)
}
