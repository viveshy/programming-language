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

	// In map we have key instead of index
	for key, value := range menu {
		fmt.Printf("Key: %v, Value: %v \n", key, value)
	}

	// update item in map
	menu["soup"] = 8.99

	// appending item in map
	menu["juice"] = 12.44

	fmt.Println(menu)

	// delete item in map
	delete(menu, "juice")
	fmt.Print(menu)

}
