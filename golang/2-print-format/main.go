package main

import (
	"fmt"
)

func main() {

	name := "batman"
	city := "Gotham"
	age := 45

	// Print: it does not add a new line at the end
	fmt.Print("Something in the way.")
	fmt.Print("I am vengeance. \n")

	//Println: it adds a new line at the end
	fmt.Println("I am not so sure.")
	fmt.Println("But I am the shadows.")

	//Printf
	fmt.Printf("I am %v. %v is a big city. \n", name, city)
	fmt.Printf("I am %q. %q is a big city.", name, city)
	fmt.Printf("age is of type %T", age)
	fmt.Printf("age is %v", age)

	// for float
	fmt.Printf("you scored %f", 0.55)
	fmt.Printf("you scored %0.1f", 0.555)   // Round off to 1 decimal place
	fmt.Printf("you scored %0.2f", 0.55555) // Round off to 2 decimal place
	fmt.Printf("you scored %0.2f", 5.5)

	// Sprintf: it saves formatted strings
	var batmanIntro = fmt.Sprintf("I am %v. I am dark knight of %v", name, city)
	fmt.Print(batmanIntro)
}
