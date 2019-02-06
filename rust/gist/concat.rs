use std::env;
use std::io;
use std::fs::File;
use std::io::prelude::*;
use std::str;
use std::collections::HashMap;
use std::collections::VecDeque;
use std::io::BufReader;

fn main() -> io::Result<()> {
    let args: Vec<String> = env::args().collect();
    //println!("{:?}", args);
    let filename = &args[1];

    let ngram = 5;

    let mut ring = VecDeque::new();
    let mut counts = HashMap::new();
    let mut tmp : Vec<u8> = vec![0; ngram];

    // TODO: Byte at a time is crazy slow
    let f = File::open(filename)?;
    let reader = BufReader::new(f);
    for (_, byte) in reader.bytes().enumerate() {
        ring.push_back(byte.unwrap());
        if ring.len() >= ngram {
            if ring.len() > ngram {
                ring.pop_front();
            }
            for (i, v) in ring.iter().enumerate() {
                tmp[i] = *v;
            }
            // This is not as concise as an entry based solution
            // An entry(k) requires ownership of k however - even if the key already exists
            // Increasing allocations in this inner loop is disastrous so we check for key existence
            // Discussions: https://internals.rust-lang.org/t/pre-rfc-abandonning-morals-in-the-name-of-performance-the-raw-entry-api/7043/52
            if counts.get_mut(&tmp).is_some() {
                *counts.get_mut(&tmp).unwrap() += 1;
            } else {
                counts.insert(tmp.to_owned(), 1);
            }
        }
    }

    let mut count_vec: Vec<_> = counts.iter().collect();
    count_vec.sort_by(|a, b| b.1.cmp(a.1));
    for (i, (ngram, count)) in count_vec.iter().enumerate() {
        if i > 10 {
            break
        }
        let s = str::from_utf8(&ngram).unwrap();
        println!("Rank {}: {:?} with count {}", i, s, count);
    }
    // Not sure what this is or why it's needed but io::Result is involved ;)
    Ok(())
}
