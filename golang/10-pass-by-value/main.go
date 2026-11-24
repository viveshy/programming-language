/*
 In golang every argument is passed by value: the function always gets a copy.
 What differs between the two groups below is what that copy contains.

 Group A: strings, ints, floats, booleans, arrays, structs
   Non-pointer values. The copy is the whole value, so changing it inside
   the function does not affect the caller.

 Group B: slices, maps, functions, channels, pointers
   Pointer wrapper values. The copy is a small header that points at the same
   underlying data, so changing that data through the copy is visible to the
   caller. Replacing the copy itself (menu = ...) is not.
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

func replaceMenu(menu map[string]float64) {
	menu = map[string]float64{"tea": 2.5} // replaces only this function's copy

	fmt.Printf("Menu in this function is %v \n", menu)
}

func main() {
	/*____GROUP A: the function changes its own copy____*/
	name := "bruce"

	updateName(name)

	fmt.Println(name)

	/*____GROUP B: still pass by value, but the copy points at the same map____*/

	menu := map[string]float64{
		"pie":       12.4,
		"ice cream": 13.45,
	}

	fmt.Println(menu)
	updateMenu(menu)
	fmt.Println(menu) // coffee was added: the function changed the shared map

	replaceMenu(menu)
	fmt.Println(menu) // unchanged: the function only replaced its own copy
}
