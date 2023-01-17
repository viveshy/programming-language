package main

import "fmt"

func main() {

	/*We can declare variables in Go in these ways:
	var <variableName> <variableType> = <value>
	var <variableName> = <value>
	var <variableName> <variableType>
	<variableName> := <value>
	*/

	// STRING
	var nameOne string = "shelby"
	var nameTwo = "thomas"
	var nameThree string
	nameFour := "Peaky Blinders" // This short hand won't work outside the function

	fmt.Println(nameOne, nameTwo, nameThree, nameFour)

	/*
		Numbers in Go are of two types: int, float
		Numbers are declared in the same way as string
	*/

	// INT
	var age1 int = 40
	var age2 = 41
	var age3 int
	age4 := 42

	fmt.Println(age1, age2, age3, age4)

	// bits and memory
	var numOne int8 = 45
	var numTwo int8 = -128
	var numThree uint16 = 256

	fmt.Println(numOne, numTwo, numThree)

	//FLOAT: either float32 or float64
	var scoreOne float32 = 20.55
	var scoreTwo float64 = 88888888888888.666666
	scoreThree := 1.5 // Default is float64

	fmt.Println(scoreOne, scoreTwo, scoreThree)
}
