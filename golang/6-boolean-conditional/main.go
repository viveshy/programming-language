package main

import "fmt"

func main() {

	age := 41

	if age < 30 {
		fmt.Println("Age is less than 30.")
	} else if age < 40 {
		fmt.Println("Age is less than 40.")
	} else {
		fmt.Println("Age is not less than 40.")
	}

	// continue and break
	names := []string{"batman", "dark knight", "cape crusader", "joker", "vengeance"}

	for index, value := range names {
		if index == 1 {
			fmt.Println("Continuing at position", index)
			continue
		}
		if index > 3 {
			fmt.Println("breaking at position", index)
			break
		}

		fmt.Printf("Tha value at position %v is %v \n", index, value)
	}

}
