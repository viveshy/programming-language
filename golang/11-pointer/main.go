/*
 In this tutorial, notice argument is passed and how parameter is received
 if we want to play along with pointer.
*/

package main

import "fmt"

func updateName(name *string) {
	*name = "Shri Mahendra Singh Dhoni"
}
func main() {
	name := "MS Dhoni"

	updateName(&name)

	fmt.Println(name)

	// we can store pointer to a variable
	ptr := &name

	*ptr = "Captain cool"
	fmt.Println(name)

	updateName(ptr)

	fmt.Print(*ptr)
	fmt.Println(name)
}
