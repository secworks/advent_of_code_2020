package main

import "fmt"


func find_loop_size(pk int64, sn int64) {
	var value int64 = 1
	var loops int64 = 0
	for (value != pk) {
		value *= sn
		value = value % 20201227
		loops += 1
	}
	fmt.Printf("Loops: %d\n", loops)
}


func main() {
	fmt.Println("Problem 1:\n")
	find_loop_size(5764801, 7)
}
