extern crate ispc;

fn main() {
    ispc::compile_library("ispdotc", &["src/ispdotc.ispc"]);
}
