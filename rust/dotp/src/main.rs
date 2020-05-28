#[macro_use]
extern crate ispc;
ispc_module!(ispdotc);
use std::arch::x86_64::*;

#[inline(never)]
fn simddotp_no_bounds(x: &[f32], y: &[f32], z: &mut [f32]) {
    for idx in 0..1024 / 8 {
        unsafe {
            let (a, b, c) = (
                x.get_unchecked(idx * 8),
                y.get_unchecked(idx * 8),
                z.get_unchecked_mut(idx * 8),
            );
            let x_a = _mm256_loadu_ps(a);
            let y_a = _mm256_loadu_ps(b);
            let r_a = _mm256_loadu_ps(c);
            _mm256_storeu_ps(c, _mm256_fmadd_ps(x_a, y_a, r_a));
        }
    }
}

#[inline(never)]
fn simddotp(x: &[f32], y: &[f32], z: &mut [f32]) {
    for ((a, b), c) in x
        .chunks_exact(8)
        .zip(y.chunks_exact(8))
        .zip(z.chunks_exact_mut(8))
    {
        unsafe {
            let x_a = _mm256_loadu_ps(a.as_ptr());
            let y_a = _mm256_loadu_ps(b.as_ptr());
            let r_a = _mm256_loadu_ps(c.as_ptr());
            _mm256_storeu_ps(c.as_mut_ptr(), _mm256_fmadd_ps(x_a, y_a, r_a));
        }
    }
}

fn dotp(x: &[f32], y: &[f32], z: &mut [f32]) {
    for ((a, b), c) in x.iter().zip(y.iter()).zip(z.iter_mut()) {
        *c += a * b;
        //*c = a.mul_add(*b, *c);
    }
}

fn main() {
    let mut rng = rand::thread_rng();

    // Target for 1024 * 8 = 183218540000
    const L: usize = 1024 * 1;
    const BLOCK: usize = 1024;
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

    for _ in 0..(10 * 1000 * 1000) {
        for _r in 0..1 {
            //for ((a, b), c) in x.iter().zip(y.iter()).zip(z.iter_mut()) {
            //    *c += a * b;
            //}
            for ((a, b), c) in x
                .chunks_exact(BLOCK)
                .zip(y.chunks_exact(BLOCK))
                .zip(z.chunks_exact_mut(BLOCK))
            {
                // Note: We're assuming 1024 dimensional vectors for speed
                unsafe {
                    ispdotc::dotp(a.as_ptr(), b.as_ptr(), c.as_mut_ptr());
                }
                //simddotp(a, b, c);
                //dotp(a, b, c);
                //simddotp_no_bounds(a, b, c);
            }
        }
    }

    let mut total: f64 = Z as f64;
    for el in z.iter() {
        total += *el as f64;
    }
    println!("{}", total);
}
