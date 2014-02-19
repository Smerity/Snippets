package main

import "fmt"
import "sync"
import "time"

func worker(linkChan chan int, w *sync.WaitGroup) {
	// Signal this is complete when we leave the function
	defer w.Done()
	//
	for v := range linkChan {
		time.Sleep(1 * time.Second)
		fmt.Println("Finished", v)
	}
}

func main() {
	// The channel distributes work to the workers
	lCh := make(chan int)
	// Wait group allows us to wait until everyone is done
	w := new(sync.WaitGroup)

	// Set up the worker pool
	for i := 0; i < 10; i++ {
		w.Add(1)
		go worker(lCh, w)
	}

	// Send in the work requests to the workers
	for i := 0; i < 100; i++ {
		lCh <- i
	}

	// Close the channel
	close(lCh)
	// Wait until all workers are complete
	w.Wait()
}
