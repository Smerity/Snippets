use std::env;
use std::io;
use std::fs::File;
use std::io::prelude::*;
use std::str;
use std::collections::HashMap;
use std::collections::VecDeque;

fn main() -> io::Result<()> {
    let args: Vec<String> = env::args().collect();
    //println!("{:?}", args);
    let filename = &args[1];

    let mut vec = VecDeque::new();
    let mut counts = HashMap::new();
    let mut v : Vec<u8> = Vec::new();

    // TODO: Byte at a time is crazy slow
    let f = File::open(filename)?;
    for (_, byte) in f.bytes().enumerate() {
        vec.push_back(byte.unwrap());
        if vec.len() >= 3 {
            if vec.len() > 3 {
                vec.pop_front();
            }
            v.clear();
            v.extend(vec.iter());
            //println!("{:?}", v);
            //let s = str::from_utf8(&v).unwrap();
            *counts.entry(v.to_owned()).or_insert(0) += 1;
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
