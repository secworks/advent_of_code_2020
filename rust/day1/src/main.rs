use std::fs;

fn main() {
    println!("AoC 2020, Day 1");
    println!("===============");

 //   let data = fs::read_to_string("/Users/js/Sandbox/proj/ctf/advent_of_code_2020/rust/day1/src/day1_input.txt").expect("Unable to read file");
    let data2 = fs::read("/Users/js/Sandbox/proj/ctf/advent_of_code_2020/rust/day1/src/day1_input.txt").expect("Unable to read file");
//    println!("{}", data);
//    println!("{}", data2.len());

    println!("Problem 1");
    println!("---------");
    println!("{}", data2[23]);


}
