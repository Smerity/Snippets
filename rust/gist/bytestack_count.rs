use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();

    let mut s = "The cat sat on the mat".as_bytes();
    println!("{:?}", s);
    let mut t = s.iter().flat_map(|x| vec![x + 1, 1]).collect::<Vec<u8>>();
    println!("{:?}", t);

    println!("---");

    let mut idx = 0;
    while idx < t.len() {
        let key = if idx % 2 == 0 { true } else { false };
        // Skip this if it's a value
        if !key {
            idx += 1;
            continue;
        }

        let mut changed = false;

        let mut i = idx + 2;
        // If no key, find the next key and compact it to here
        if t[idx] == 0 {
            while i < t.len() {
                if t[i] > 0 {
                    t[idx] = t[i];
                    t[i] = 0;
                    t[idx + 1] += t[i + 1];
                    t[i + 1] = 0;
                    changed = true;
                    break;
                }
                i += 2;
            }
        }

        i = idx + 2;
        // Collect all counts from equal keys and place them here
        while i < t.len() {
            if t[i] == t[idx] {
                t[idx + 1] += t[i + 1];
                t[i + 1] = 0;
                t[i] = 0;
                changed = true;
            }
            i += 2;
        }

        if changed {
            println!("{:?}", t);
        }
        idx += 2;
    }
}
