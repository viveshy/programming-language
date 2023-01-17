package main

import (
	"fmt"
	"math"
)

func sayGreeting(name string) {
	fmt.Printf("Hello, %v! \n", name)
}

func sayBye(name string) {
	fmt.Printf("Bye, %v! \n", name)
}

func cycleNames(names []string, greetFunction func(string)) {
	for _, name := range names {
		greetFunction(name)
	}
}

func areaOfCircle(radius float64) float64 {
	return math.Pi * radius * radius
}
func main() {
	sayGreeting("Bruce Wayne")
	sayBye("Master Wayne")

	names := []string{"Batman", "Wayne", "Dark Knight"}
	cycleNames(names, sayGreeting)

	fmt.Printf("The area of circle is %0.2f", areaOfCircle(4.5))
}
