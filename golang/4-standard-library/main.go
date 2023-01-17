package main

import (
	"fmt"
	"sort"
	"strings"
)

func main() {

	// strings package
	greeting := "hello people of gotham"

	fmt.Println(strings.Contains(greeting, "hello"))

	stringOne := strings.ReplaceAll(greeting, "hello", "hi")
	fmt.Println(greeting)
	fmt.Println(stringOne)

	stringTwo := strings.ToUpper(greeting)
	fmt.Println(stringTwo)

	position := strings.Index(greeting, "ll")
	fmt.Println(position)

	splitStrings := strings.Split(greeting, " ")
	fmt.Println(splitStrings)

	// sort package
	ages := []int{1, 22, 3, 44, 8}
	sort.Ints(ages)
	fmt.Println(ages)

	index := sort.SearchInts(ages, 3)
	fmt.Println(index)
	index = sort.SearchInts(ages, 77)
	fmt.Println(index)

	names := []string{"batman", "dark knight", "cape crusader"}
	sort.Strings(names)
	fmt.Println(names)

	fmt.Println(sort.SearchStrings(names, "batman"))
}
