package main

import (
	"fmt"
	"log"
	"sync"
	"time"
)

// queryResult is what each query goroutine sends back on the channel.
type queryResult struct {
	query    int
	finished time.Time
}

func main() {

	var waitGroup sync.WaitGroup

	// The goroutines send their results to main on this channel.
	results := make(chan queryResult)

	// Perform 10 concurrent queries (simulated: each one just records the time).
	waitGroup.Add(10)
	for query := 0; query < 10; query++ {
		go RunQuery(query, results, &waitGroup)
	}

	// Close the channel once every query has sent its result,
	// so the range loop below knows when to stop.
	go func() {
		waitGroup.Wait()
		close(results)
	}()

	// Receive the results as they arrive (in no fixed order).
	for result := range results {
		fmt.Printf("Query %v finished at %v\n", result.query, result.finished.Format("15:04:05.000000"))
	}
	log.Println("All Queries Completed")

}

// results is send-only (chan<-) here: this function can send on it but not receive.
func RunQuery(query int, results chan<- queryResult, waitGroup *sync.WaitGroup) {

	defer waitGroup.Done()
	results <- queryResult{query: query, finished: time.Now()}

}
