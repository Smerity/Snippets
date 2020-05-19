#[macro_use]
extern crate ispc;

use std::arch::x86_64::*;

ispc_module!(ispdotc);

#[inline(never)]
fn simddotp(x: &[f32], y: &[f32], z: &mut [f32]) {
    unsafe {
        for ((a, b), c) in x
            .chunks_exact(8 * 4)
            .zip(y.chunks_exact(8 * 4))
            .zip(z.chunks_exact_mut(8 * 4))
        {
            //
            let x_a = _mm256_loadu_ps(a.as_ptr().offset(0));
            let y_a = _mm256_loadu_ps(b.as_ptr().offset(0));
            let r_a = _mm256_loadu_ps(c.as_ptr().offset(0));
            _mm_prefetch(a.as_ptr().offset(16) as *const i8, _MM_HINT_T1);
            _mm256_storeu_ps(c.as_mut_ptr().offset(0), _mm256_fmadd_ps(x_a, y_a, r_a));
            //
            let x_b = _mm256_loadu_ps(a.as_ptr().offset(8));
            let y_b = _mm256_loadu_ps(b.as_ptr().offset(8));
            let r_b = _mm256_loadu_ps(c.as_ptr().offset(8));
            _mm256_storeu_ps(c.as_mut_ptr().offset(8), _mm256_fmadd_ps(x_b, y_b, r_b));
            //
            //
            let x_c = _mm256_loadu_ps(a.as_ptr().offset(16));
            let y_c = _mm256_loadu_ps(b.as_ptr().offset(16));
            let r_c = _mm256_loadu_ps(c.as_ptr().offset(16));
            _mm256_storeu_ps(c.as_mut_ptr().offset(16), _mm256_fmadd_ps(x_c, y_c, r_c));
            //
            let x_d = _mm256_loadu_ps(a.as_ptr().offset(24));
            let y_d = _mm256_loadu_ps(b.as_ptr().offset(24));
            let r_d = _mm256_loadu_ps(c.as_ptr().offset(24));
            _mm256_storeu_ps(c.as_mut_ptr().offset(24), _mm256_fmadd_ps(x_d, y_d, r_d));
        }
    }
}

fn dotp(x: &[f32], y: &[f32], z: &mut [f32]) {
    for ((a, b), c) in x.iter().zip(y.iter()).zip(z.iter_mut()) {
        *c += a * b;
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
            //    *c = a * b;
            //}
            for ((a, b), c) in x
                .chunks_exact(BLOCK)
                .zip(y.chunks_exact(BLOCK))
                .zip(z.chunks_exact_mut(BLOCK))
            {
                unsafe {
                    ispdotc::dotp(a.as_ptr(), b.as_ptr(), c.as_mut_ptr(), BLOCK as u32);
                }
                //simddotp(a, b, c);
                //dotp(a, b, c);
            }
        }
    }

    let mut total: f64 = Z as f64;
    for el in z.iter() {
        total += *el as f64;
    }
    println!("{}", total);
}
