package main

import "fmt"

type bill struct {
	name  string
	items map[string]float64
	tip   float64
}

// receiver function will help us create format() function
func (customerBill bill) format() string {
	formattedString := "Bill breakdown \n"
	var total float64 = 0

	for key, value := range customerBill.items {
		// -25v will make the variable 25 characters long by spacing towards right
		// +25 will keep the spacing towards left
		formattedString += fmt.Sprintf("%-25v ...$%v \n", key+":", value)
		total += value
	}

	total += customerBill.tip

	// total
	formattedString += fmt.Sprintf("%-25v ...$%0.2f \n", "tip:", customerBill.tip)
	// total
	formattedString += fmt.Sprintf("%-25v ...$%0.2f \n", "total:", total)

	return formattedString
}

// update tip
// REMEMBER: we just need to put pointer in the receiver function. Everything else will be handled by Golang
func (customerBill *bill) updateTip(tip float64) {
	customerBill.tip = tip
}

// add item to the bill
func (customerBill bill) addItem(name string, price float64) {
	customerBill.items[name] = price
}

// make new bills
func generateBill(name string) bill {
	customerBill := bill{
		name:  name,
		items: map[string]float64{"pie": 5.66, "cake": 4.55},
		tip:   0,
	}

	return customerBill
}
func main() {
	myBill := generateBill("Wayne")
	fmt.Println(myBill.format())

	myBill.updateTip(1.45)
	myBill.addItem("ice cream", 5.12)

	fmt.Println(myBill.format())
}
