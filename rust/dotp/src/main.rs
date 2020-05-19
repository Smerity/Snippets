use rand::Rng;

use std::arch::x86_64::*;

#[allow(non_camel_case_types)]
pub type f32x8 = __m256;
#[allow(non_upper_case_globals)]
pub const f32x8_LENGTH: usize = 8;

fn tof32x8(s: &[f32]) -> f32x8 {
    //assert_eq!(s.len(), f32x8_LENGTH);
    // Using 0..8 results in a vpermps
    //unsafe { _mm256_set_ps(s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7]) }
    unsafe { _mm256_set_ps(s[7], s[6], s[5], s[4], s[3], s[2], s[1], s[0]) }
}

fn simddotp(x: &[f32], y: &[f32], z: &mut [f32]) {
    //let (a, b, c) = (&x[0..32], &y[0..32], &mut z[0..32]);
    for ((a, b), c) in x.chunks_exact(8 * 4).zip(y.chunks_exact(8 * 4)).zip(z.chunks_exact_mut(8 * 4)) {
        unsafe {
            let xa = tof32x8(&a[0..8]);
            let xb = tof32x8(&a[8..16]);
            let xc = tof32x8(&a[16..24]);
            let xd = tof32x8(&a[24..32]);

            let ya = tof32x8(&b[0..8]);
            let yb = tof32x8(&b[8..16]);
            let yc = tof32x8(&b[16..24]);
            let yd = tof32x8(&b[24..32]);

            let r1 = _mm256_mul_ps(xa, ya);
            let r2 = _mm256_mul_ps(xb, yb);
            let r3 = _mm256_mul_ps(xc, yc);
            let r4 = _mm256_mul_ps(xd, yd);

            _mm256_storeu_ps(c[0..8].as_mut_ptr(), r1);
            _mm256_storeu_ps(c[8..16].as_mut_ptr(), r2);
            _mm256_storeu_ps(c[16..24].as_mut_ptr(), r3);
            _mm256_storeu_ps(c[24..32].as_mut_ptr(), r4);
        }
    }
}

fn dotp(x: &[f32], y: &[f32], z: &mut [f32]) {
    for ((a, b), c) in x.iter().zip(y.iter()).zip(z.iter_mut()) {
        *c = a * b;
    }
}

fn main() {
    let mut rng = rand::thread_rng();

    // Target for 1024 * 8 = 183218540000
    const L: usize = 1024 * 8;
    const BLOCK: usize = 512;
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
            //for ((a, b), c) in x.iter().zip(y.iter()).zip(z.iter_mut()) {
            //    *c = a * b;
            //}
            for ((A, B), C) in x.chunks_exact(BLOCK).zip(y.chunks_exact(BLOCK)).zip(z.chunks_exact_mut(BLOCK)) {
                simddotp(A, B, C);
            }
        }
    }

    let mut total = Z;
    for el in z.iter() {
        total += *el;
    }
    println!("{}", total);
}
