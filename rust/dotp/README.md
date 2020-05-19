### SIMD results in madness

`time RUSTFLAGS="-C target-cpu=native" cargo run --release`

`RUSTFLAGS="-C target-cpu=native" cargo asm dotp::main --rust > /tmp/v`

`perf record --call-graph=lbr ./target/release/dotp -B -e cache-references,cache-misses,cycles,instructions,branches,faults,migrations`
`perf report --hierarchy -M intel`
