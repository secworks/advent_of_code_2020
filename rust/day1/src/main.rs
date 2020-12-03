use std::env;
use std::fs;

fn main() {
    println!("AoC 2020, Day 1");

    let contents = fs::read_to_string("~/Sandbox/proj/ctf/advent_of_code_2020/rust/day1/src/day1_input.txt")
    .expect("Something went wrong reading the file");

    println!("With text:\n{}", contents);
}
