package main

import (
	"fmt"
	"runtime"
	"sync"
)

var wg = sync.WaitGroup{}
var m = sync.RWMutex{}
var counter = 0

func main() {
	runtime.GOMAXPROCS(100)

	// find number of thread set
	fmt.Println("Threads ", runtime.GOMAXPROCS(-1))
	for i := 0 ; i<10;i++{
		wg.Add(2)
		m.RLock()
		go sayHello()

		m.Lock()
		go increment()
	}
	wg.Wait()
}

func sayHello(){
	fmt.Printf("Hello # %v \n", counter)
	m.RUnlock()
	wg.Done()
}

func increment(){
	counter++
	m.Unlock()
	wg.Done()
}