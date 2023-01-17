package main

import (
	"fmt"
	"log"
	"sync"
	"time"
)

func main() {

	var waitGroup sync.WaitGroup

	// Perform 10 concurrent queries against the database.
	waitGroup.Add(10)
	for query := 0; query < 10; query++ {
		go RunQuery(query, &waitGroup)
	}

	// Wait for all the queries to complete.
	waitGroup.Wait()
	log.Println("All Queries Completed")

}

func RunQuery(query int, waitGroup *sync.WaitGroup) {

	defer waitGroup.Done()
	fmt.Println("Query : ", time.Now())

}