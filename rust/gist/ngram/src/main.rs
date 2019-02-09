//extern crate hashbrown;
//extern crate indexmap;

// Hashbrown seems slower than the standard map for larger values
//use hashbrown::HashMap;
//use indexmap::IndexMap;
use std::collections::HashMap;

use std::io::Read;
use std::env;
use std::io;
use std::fs::File;
use std::str;
use std::io::BufReader;

fn main() -> io::Result<()> {
    let args: Vec<String> = env::args().collect();
    //println!("{:?}", args);
    let filename = &args[1];

    let ngram = 6;

    //let mut counts = HashMap::new();
    let mut counts = HashMap::with_capacity(1000);
    //let mut counts = IndexMap::new();
    let mut tmp : Vec<u8> = vec![0; ngram];
    let mut cap : usize = 0;
    let mut seen : u64 = 0;
    let mut dupe : u64 = 0;

    println!("Reading...");
    let f = File::open(filename)?;
    let reader = BufReader::new(f);
    for (idx, byte) in reader.bytes().enumerate() {
        seen += 1;
        // We need [_, 0, 1, 2] as the main thread will shift [0, 1, 2, _] and put 3 into the last spot
        if counts.capacity() != cap {
            cap = counts.capacity();
            println!("Capacity: {}", cap);
        }
        if idx < ngram - 1 {
            tmp[idx + 1] = byte.unwrap();
        } else {
            // Shift all items left by one
            for i in 0..ngram-1 {
                tmp[i] = tmp[i + 1];
            }
            tmp[ngram-1] = byte.unwrap();

            // This is not as concise as an entry based solution
            // An entry(k) requires ownership of k however - even if the key already exists
            // Increasing allocations in this inner loop is disastrous so we check for key existence
            // Discussions: https://internals.rust-lang.org/t/pre-rfc-abandonning-morals-in-the-name-of-performance-the-raw-entry-api/7043/52
            if counts.contains_key(&tmp) {
                *counts.get_mut(&tmp).unwrap() += 1;
                dupe += 1;
            } else {
                counts.insert(tmp.to_owned(), 1);
            }
        }
    }

    println!("Processing...");
    println!("Total of {} items", counts.len());
    println!("Of the {} seen items, {} items are dupes", seen, dupe);
    println!("Hapax legomenon: {}", counts.values().filter(|&x| *x == 1).count());
    let mut count_vec: Vec<_> = counts.iter().collect();
    count_vec.sort_by(|a, b| b.1.cmp(a.1));
    for (i, (ngram, count)) in count_vec.iter().take(25).enumerate() {
        let s = str::from_utf8(&ngram).unwrap();
        println!("Rank {}: {:?} with count {}", i, s, count);
    }

    // Not sure what this is or why it's needed but io::Result is involved ;)
    Ok(())
}
