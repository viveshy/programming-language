package main

import (
	"errors"
	"fmt"
)

func divide(num1 float64, num2 float64) (float64, error) {
	// Only zero is a problem: dividing by a negative number is fine (6 / -2 = -3).
	if num2 == 0 {
		return 0.0, errors.New("cannot divide by zero")
	}
	return num1 / num2, nil
}
func main() {

	for _, divisor := range []float64{0.0, -2.0} {
		result, err := divide(6.0, divisor)

		if err != nil {
			fmt.Printf("6 / %v -> error: %v\n", divisor, err)
		} else {
			fmt.Printf("6 / %v = %.2f\n", divisor, result)
		}
	}

}
