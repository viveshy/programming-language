package main

import "fmt"

func divide(num1 float64, num2 float64) (float64, error) {
	if num2 <= 0 {
		return 0.0, fmt.Errorf("Cannot perform division.")
	}
	return num1 / num2, nil
}
func main() {

	result, err := divide(5.0, 0.0)

	if err != nil {
		fmt.Printf("Error: %v", err)
	} else {
		fmt.Printf("The result is %0.2f", result)
	}

}
