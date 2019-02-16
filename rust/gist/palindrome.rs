use std::env;
use std::fs;

// Use double ended iterator:
// https://doc.rust-lang.org/std/iter/trait.DoubleEndedIterator.html
//
// Inspired by:
// https://www.reddit.com/r/rust/comments/7a9w1c/rust_is_now_an_official_part_of_stanfords/dp8rx8j/

fn main() {
    let mut s = "radar".as_bytes();

    let mut iter = s.iter();
    let mut palindrome = true;
    while let (Some(a), Some(b)) = (iter.next(), iter.next_back()) {
        println!("{} {}", *a, *b);
        if *a != *b {
            palindrome = false;
            break;
        }
    }
    println!("Is {:?} a palindrome? {}", s, palindrome);
}
