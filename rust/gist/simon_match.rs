use std::io::{self, BufRead};
use std::rc::Rc;

#[derive(Debug)]
struct StackItem {
    token: String,
    data: u64,
}

fn main() {
    let mut stack = vec![String::from("Ø")];
    let stdin = io::stdin();

    for line in stdin.lock().lines() {
        let l = line.unwrap();
        // let r = stack[0]; // Doesn't work
        //let r = ; stack[0].to_string() // Works
        
        match l.as_str() {
            "+" => {
                let a = stack.pop();
                let b = stack.pop();
                let c = a.unwrap().parse::<i64>().unwrap() + b.unwrap().parse::<i64>().unwrap();
                stack.push(c.to_string());
            },
            "*" => {
                let a = stack.pop();
                let b = stack.pop();
                let c = a.unwrap().parse::<i64>().unwrap() * b.unwrap().parse::<i64>().unwrap();
                stack.push(c.to_string());
            }
            "caps" => {
                let a = stack.pop();
                stack.push(a.unwrap().to_uppercase());
            },
            "swap" => {
                let a = stack.pop();
                let b = stack.pop();
                stack.push(a.unwrap());
                stack.push(b.unwrap());
            },
            "dup" => {
                let r = stack[stack.len() - 1].to_string();
                stack.push(r);
            },
            "drop" => {
                stack.pop();
            }
            _ => stack.push(l),
        }
        // TODO: Investigate stack.iter().rev().take(2)
        //let (a, b) = (stack.iter().rev().nth(0).unwrap().data, stack.iter().rev().nth(1).unwrap().data);
        //stack.push(StackItem {token: l, data: a + b});
        println!("{:#?}", stack);
    }
    println!("{:#?}", stack);
}