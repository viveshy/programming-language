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
		Numbers in Go come in three kinds:
		- integers: int, int8, int16, int32, int64, and unsigned uint, uint8 ... uint64
		- floats: float32, float64 (there is no plain "float" type)
		- complex numbers: complex64, complex128
		Numbers are declared in the same way as strings
	*/

	// INT
	var age1 int = 40
	var age2 = 41
	var age3 int
	age4 := 42

	fmt.Println(age1, age2, age3, age4)

	// bits and memory: the number in the type is its size in bits, which limits its range
	var numOne int8 = 45 // int8 holds -128 to 127
	var numTwo int8 = -128
	var numThree uint16 = 256 // uint16 holds 0 to 65535 (unsigned: no negative numbers)

	fmt.Println(numOne, numTwo, numThree)

	//FLOAT: either float32 or float64
	var scoreOne float32 = 20.55
	var scoreTwo float64 = 88888888888888.666666 // float64 keeps only about 15-16 digits, so this prints 8.888888888888867e+13
	scoreThree := 1.5                            // Default is float64

	fmt.Println(scoreOne, scoreTwo, scoreThree)
}
