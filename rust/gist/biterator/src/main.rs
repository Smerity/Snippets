use std::collections::HashMap;

use std::io::Read;
use std::env;
use std::io;
use std::fs::File;
use std::str;
use std::io::BufReader;
use memmap::MmapOptions;

fn main() -> io::Result<()> {
    let args: Vec<String> = env::args().collect();

    let filename = &args[1];
    let mut f = File::open(filename)?;

    let size : usize = f.metadata()?.len() as usize;
    let mut data = Vec::with_capacity(size);
    f.read_to_end(&mut data)?;

    //let mut counts = HashMap::new();

    let mut seen : u64 = 0;
    let mut sum : u64 = 0;
    let mut roll : u32 = 0;
    let mut out = vec![0];

    let mut freq : [u64; 256] = [0; 256];

    println!("Reading...");



    for i in 0..10 {
        //seen = 0;
        // Avoid indexing for speed : https://llogiq.github.io/2017/06/01/perf-pitfalls.html
        for tmp in data.iter() {
            seen += 1;
            sum += *tmp as u64;
            // The speed is _so_ much faster without freq
            freq[*tmp as usize] += 1;

            // Unsafe isn't much faster as it turns out
            // The Rustonomicon: The Dark Arts of Advanced and Unsafe Rust Programming
            // https://doc.rust-lang.org/nightly/nomicon/README.html#the-rustonomicon
            //unsafe {
            //    *freq.get_unchecked_mut(*tmp as usize) += 1;
            //}

            //roll = ((7 * roll + 3 * (roll + (tmp as u32))) << 8) + (tmp as u32);
            //println!("{}", roll);
            //roll = (tmp as u32);

            /*
            freq[(roll >> 24) as usize] += 1;
            if (roll >> 29) == 0 {
                print!("\n\n======================================\n>>>>>>>>>>>>>>>>>>>\n\n");
            }
            print!("{}", tmp as char);
            */

            // A dictionary rather than an array of size 256 destroys performance
            // 14 seconds versus ... indefinitely long ...
            //if counts.contains_key(tmp) {
            //    *counts.get_mut(tmp).unwrap() += 1;
            //} else {
            //    counts.insert(tmp.to_owned(), 1);
            //}
        }
    }
    println!("Seen: {}", seen);
    for i in 0..256 {
        println!("Freq {}: {:?}", i, freq[i]);
    }

    //let mut count_vec: Vec<_> = counts.iter().collect();
    /*count_vec.sort_by(|a, b| b.1.cmp(a.1));
    for (i, (ngram, count)) in count_vec.iter().take(25).enumerate() {
        let s = str::from_utf8(&ngram).unwrap();
        println!("Rank {}: {:?} with count {}", i, s, count);
    }*/

    // Not sure what this is or why it's needed but io::Result is involved ;)
    Ok(())
}
