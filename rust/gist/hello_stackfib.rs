use std::io::{self, BufRead};

#[derive(Debug)]
struct StackItem {
    token: String,
    data: u64,
}

fn main() {
    println!("Hello, StackFib!");
    let mut stack = vec![StackItem {token: "F0".to_string(), data: 0}, StackItem {token: "F1".to_string(), data: 1}];
    let stdin = io::stdin();
    for line in stdin.lock().lines() {
        let l = line.unwrap();
        println!("{:#?}", l);
        // TODO: Investigate stack.iter().rev().take(2)
        let (a, b) = (stack.iter().rev().nth(0).unwrap().data, stack.iter().rev().nth(1).unwrap().data);
        stack.push(StackItem {token: l, data: a + b});
        println!("{:#?}", stack);
    }
    println!("{:#?}", stack);
}