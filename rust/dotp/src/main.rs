use rand::Rng;

fn main() {
    let mut rng = rand::thread_rng();

    const L: usize = 272;
    const ONE: f32 = 1.0;
    const Z: f32 = ONE * 0.0;

    let mut x: [f32; L] = [Z; L];
    for el in x.iter_mut() {
        *el = (ONE + ONE) * rng.gen::<f32>() - ONE;
    }

    let mut y: [f32; L] = [Z; L];

    for el in y.iter_mut() {
        *el = (ONE + ONE) * rng.gen::<f32>() - ONE;
    }

    let mut z: [f32; L] = [Z; L];

    for _ in 0..(1000 * 1000) {
        for r in 0..100 {
            for ((a, b), c) in x.iter().zip(y.iter()).zip(z.iter_mut()) {
                *c = a * b;
            }
        }
    }

    let mut total = Z;
    for el in z.iter() {
        total += *el;
    }
    println!("{}", total);
}
