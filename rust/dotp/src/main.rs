use rand::Rng;

fn dotp(x: &[f32], y: &[f32], z: &mut [f32]) {
    for ((a, b), c) in x.iter().zip(y.iter()).zip(z.iter_mut()) {
        *c = a * b;
    }
    //unsafe {
    //for i in 0..1024 {
    //    *z.get_unchecked_mut(i) = x.get_unchecked(i) * y.get_unchecked(i);
    //}
    //}
}

fn main() {
    let mut rng = rand::thread_rng();

    // Target for 1024 * 8 = 183218540000
    const L: usize = 384; //1024 * 1;
    const BLOCK: usize = 128;
    const ONE: f32 = 1.0;
    const Z: f32 = ONE * 0.0;

    let mut x: [f32; L] = [Z; L];
    for (idx, el) in x.iter_mut().enumerate() {
        //*el = (ONE + ONE) * rng.gen::<f32>() - ONE;
        *el = idx as f32;
    }

    let mut y: [f32; L] = [Z; L];

    for (idx, el) in y.iter_mut().enumerate() {
        //*el = (ONE + ONE) * rng.gen::<f32>() - ONE;
        *el = idx as f32;
    }

    let mut z: [f32; L] = [Z; L];

    for _ in 0..(1000 * 1000) {
        for r in 0..100 {
            for ((a, b), c) in x.iter().zip(y.iter()).zip(z.iter_mut()) {
                *c = a * b;
            }
            //for ((A, B), C) in x.chunks_exact(BLOCK).zip(y.chunks_exact(BLOCK)).zip(z.chunks_exact_mut(BLOCK)) {
            //    dotp(A, B, C);
            //}
        }
    }

    let mut total = Z;
    for el in z.iter() {
        total += *el;
    }
    println!("{}", total);
}
