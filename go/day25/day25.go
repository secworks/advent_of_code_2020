//======================================================================
//
// day25.go
// --------
// Solution to:
// https://adventofcode.com/2020/day/25
//
//======================================================================

package main

import "fmt"


func find_loop_size(pk int64, sn int64) int64 {
	var value int64 = 1
	var loops int64 = 0

	for (value != pk) {
		value *= sn
		value = value % 20201227
		loops += 1
	}

	return loops
}


func find_private_key(pk int64, ls int64) int64 {
	var value int64 = 1
	var i int64

	for i = 0; i < ls; i++ {
		value *= pk
		value = value % 20201227
	}

	return value
}


// Run example values for problem 1.
func example1() {
	fmt.Println("Example 1:")
	fmt.Println("----------")

	var sn int64 = 7
	var card_pk int64 = 5764801
	var door_pk int64 = 17807724

	var card_loops = find_loop_size(card_pk, sn)
	var door_loops = find_loop_size(door_pk, sn)
	fmt.Printf("Card loops: %v \n", card_loops)
	fmt.Printf("Door loops: %v \n", door_loops)

	var card_sk = find_private_key(door_pk, card_loops)
	var door_sk = find_private_key(card_pk, door_loops)
	fmt.Printf("Card secret key: %v \n", card_sk)
	fmt.Printf("Door secret_key: %v \n", door_sk)
	fmt.Println("")
}


func problem1() {
	fmt.Println("Problem 1:")
	fmt.Println("----------")

	var sn int64 = 7
	var card_pk int64 = 6929599
	var door_pk int64 = 2448427

	var card_loops = find_loop_size(card_pk, sn)
	var door_loops = find_loop_size(door_pk, sn)
	fmt.Printf("Card loops: %v \n", card_loops)
	fmt.Printf("Door loops: %v \n", door_loops)

	var card_sk = find_private_key(door_pk, card_loops)
	var door_sk = find_private_key(card_pk, door_loops)
	fmt.Printf("Card secret key: %v \n", card_sk)
	fmt.Printf("Door secret_key: %v \n", door_sk)
	fmt.Println("")
}


func main() {
	fmt.Println("Solution for AoC 2020, Day 25.\n")
	example1()
	problem1()
}
