/*
 In golang we can split up variable types in two distinct groups:

 Group A: strings, ints, floats, booleans arrays, structs
 Group B: slices, maps, functions

 It must be noted,
 Group A: Non-pointer values
 Group B: Pointer wrapper values
*/

package main

import "fmt"

func updateName(name string) {
	name = "wayne"

	fmt.Printf("Name in this function is %v \n", name)
}

func updateMenu(menu map[string]float64) {
	menu["coffee"] = 15.65
}

func main() {
	/*____GROUP A: it follows pass by value____*/
	name := "bruce"

	updateName(name)

	fmt.Println(name)

	/*____GROUP B: it follows pass by reference*/

	menu := map[string]float64{
		"pie":       12.4,
		"ice cream": 13.45,
	}

	fmt.Println(menu)
	updateMenu(menu)
	fmt.Println(menu)
}
