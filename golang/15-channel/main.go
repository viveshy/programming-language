package main

import (
	"fmt"
	"sync"
)

var wg = sync.WaitGroup{}

func main(){
	// channel is strongly typed
	ch := make(chan int)
	for j := 0 ; j< 5 ; j++ {
		wg.Add(2)

		// receiving go routine
		go func(ch <- chan int){
			i := <- ch
			fmt.Println(i)
			wg.Done()
		}(ch)
	
		// sending go routine
		go func (ch chan <- int) {
			i := 42
			ch <- i
			wg.Done()
		}(ch)
	}
	
	wg.Wait()

}