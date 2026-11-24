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

	//Printf: like Print, it does not add a new line, so end the format with \n
	fmt.Printf("I am %v. %v is a big city. \n", name, city)
	fmt.Printf("I am %q. %q is a big city.\n", name, city)
	fmt.Printf("age is of type %T\n", age)
	fmt.Printf("age is %v\n", age)

	// for float
	fmt.Printf("you scored %f\n", 0.55)
	fmt.Printf("you scored %.1f\n", 0.555)   // Round off to 1 decimal place
	fmt.Printf("you scored %.2f\n", 0.55555) // Round off to 2 decimal place
	fmt.Printf("you scored %.2f\n", 5.5)

	// A 0 before the width is a flag meaning "pad with zeros".
	// It only does something together with a width, so %0.2f is the same as %.2f.
	fmt.Printf("you scored %08.2f\n", 5.5) // 00005.50: 8 characters wide, padded with zeros

	// Sprintf: it returns the formatted string instead of printing it
	var batmanIntro = fmt.Sprintf("I am %v. I am dark knight of %v", name, city)
	fmt.Println(batmanIntro)
}
