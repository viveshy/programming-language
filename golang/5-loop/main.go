package main

import "fmt"

func main() {

	//for loop method 1
	x := 0
	for x < 5 {
		fmt.Printf("The value of x is %v \n", x)
		x++
	}

	// for loop method 2
	for i := 0; i < 5; i++ {
		fmt.Printf("The value of i is %v \n", i)
	}

	// traversing slices
	names := []string{"batman", "dark knight", "cape crusader"}
	for i := 0; i < len(names); i++ {
		fmt.Printf("The name is %v \n", names[i])
	}

	// traversing slices in go way
	for index, value := range names {
		fmt.Printf("The value at index %v is %v \n", index, value)
	}

	for _, value := range names {
		fmt.Printf("The value is %v\n", value)
	}

	for index, _ := range names {
		fmt.Printf("The index is %v\n", index)
	}

	for index := range names {
		fmt.Printf("The index is %v\n", index)
	}
}
