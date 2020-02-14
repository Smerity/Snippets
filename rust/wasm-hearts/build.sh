#!/bin/bash

set -euo pipefail

TARGET=wasm32-unknown-unknown
BINARY=target/$TARGET/release/wasm_hearts.wasm

cargo build --target $TARGET --release
#wasm-strip $BINARY
mkdir -p www
#wasm-opt -o www/bare_metal_wasm.wasm -Oz $BINARY
cp $BINARY www/bare_metal_wasm.wasm
ls -lh www/bare_metal_wasm.wasm
