use std::env;
use std::io;
use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;

fn main() -> io::Result<()> {
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];

    let mut sumBytes: u64 = 0;
    let mut totalBytes : u64 = 0;

    let f = File::open(filename)?;
    let mut reader = BufReader::new(f);
    for (_, byte) in reader.bytes().enumerate() {
        totalBytes += 1;
        sumBytes += byte.unwrap() as u64;
    }

    println!("Total number of bytes: {}", totalBytes);
    println!("Total value of bytes: {}", sumBytes);
    Ok(())
}
