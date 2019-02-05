use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();
    //println!("{:?}", args);

    if args.len() <= 1 {
        // Nothing to print
    }
    else {
        for filename in args[1..].iter() {
            let contents = fs::read_to_string(filename).expect("Something went wrong reading the file");
            println!("{}", contents);
        }
    }
}
