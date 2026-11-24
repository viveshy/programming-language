package main

import "fmt"

func main() {

	// Map has a key and a value

	menu := map[string]float64{
		"soup":  4.99,
		"pie":   7.99,
		"salad": 6.99,
	}

	fmt.Println(menu)
	fmt.Println(menu["soup"])

	// In map we have key instead of index.
	// A range over a map visits the keys in a random order that changes from run to run.
	// (fmt.Println sorts the keys when it prints a whole map, so those prints look ordered.)
	for key, value := range menu {
		fmt.Printf("Key: %v, Value: %v \n", key, value)
	}

	// update item in map
	menu["soup"] = 8.99

	// add a new item to the map (maps have no append: you just set a new key)
	menu["juice"] = 12.44

	fmt.Println(menu)

	// delete item in map
	delete(menu, "juice")
	fmt.Println(menu)

}
