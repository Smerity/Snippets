// Use double ended iterator:
// https://doc.rust-lang.org/std/iter/trait.DoubleEndedIterator.html
//
// Inspired by:
// https://www.reddit.com/r/rust/comments/7a9w1c/rust_is_now_an_official_part_of_stanfords/dp8rx8j/

fn is_palindrome<T: PartialEq>(s: &[T]) -> bool {
    let mut iter = s.iter();
    while let (Some(a), Some(b)) = (iter.next(), iter.next_back()) {
        if *a != *b {
            return false;
        }
    }
    return true;
}

fn main() {
    let s = "radar".as_bytes();

    println!("Is {:?} a palindrome? {}", s, is_palindrome(s));
}
