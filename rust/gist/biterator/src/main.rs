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

    let mut freq : [u64; 256] = [0; 256];

    println!("Reading...");
    for i in 0..40 {
        //seen = 0;
        for tmp in data.windows(1) {
            seen += 1;
            sum += tmp[0] as u64;
            // The speed is _so_ much faster without freq
            freq[tmp[0] as usize] += 1;

            /*
            if counts.contains_key(&tmp) {
                *counts.get_mut(&tmp).unwrap() += 1;
            } else {
                counts.insert(tmp.to_owned(), 1);
            }
            */
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
