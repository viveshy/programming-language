package main

import "fmt"

type bill struct {
	name  string
	items map[string]float64
	tip   float64
}

// make new bills
func generateBill(name string) bill {
	customerBill := bill{
		name:  name,
		items: map[string]float64{},
		tip:   0,
	}

	return customerBill
}
func main() {
	myBill := generateBill("Wayne")
	fmt.Println(myBill)
}
