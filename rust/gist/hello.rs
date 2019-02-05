// Starting from https://github.com/nrc/r4cppp

fn give_world() -> &'static str {
    "world"
}

fn main() {
    println!("Hello, {}", give_world());
}
