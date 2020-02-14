#![no_std]

#[panic_handler]
fn handle_panic(_: &core::panic::PanicInfo) -> ! {
    loop {}
}

const WIDTH: usize = 600;
const HEIGHT: usize = 600;

#[no_mangle]
static mut BUFFER: [u32; WIDTH * HEIGHT] = [0; WIDTH * HEIGHT];

use core::sync::atomic::{AtomicU32, Ordering};

static FRAME: AtomicU32 = AtomicU32::new(0);
static LOOP: AtomicU32 = AtomicU32::new(0);
static COL: AtomicU32 = AtomicU32::new(0xFF_00_00_FF);

#[no_mangle]
pub extern fn the_answer() -> u32 {
    42
}

#[no_mangle]
pub unsafe extern fn go() -> u32 {
    // This is called from JavaScript, and should *only* be
    // called from JavaScript. If you maintain that condition,
    // then we know that the &mut we're about to produce is
    // unique, and therefore safe.
    render_frame_safe(&mut BUFFER)
}

fn draw_line(buffer: &mut [u32; WIDTH * HEIGHT], mut x: i32, mut y: i32, dx: i32, dy: i32, steps: i32, max: i32) {
    //for s in 0..steps {
        x += steps * dx;
        y += steps * dy;
        if x <= 0 || y <= 0 || x >= WIDTH as i32 || y >= HEIGHT as i32 {
            return;
        }
        if steps > max {
            return;
        }
        buffer[(y * (WIDTH as i32) + x) as usize] = COL.load(Ordering::Relaxed);
    //}
}

fn reset_buffer(buffer: &mut [u32; WIDTH * HEIGHT]) {
    for y in 0..HEIGHT {
        for x in 0..WIDTH {
            buffer[y * WIDTH + x] = 0xFF_00_00_00 + (0x00_00_00_01 * 1 as u32) * ((y / 67) as u32);
            //buffer[y * WIDTH + x] = 0xFF_00_00_00 + (0x00_00_00_01 * 1 as u32) * ((y / 2 * x * 7 + (17 * x + x) % 97 / 37) as u32);
        }
    }
}

// Replace the old render_frame_safe with this:
fn render_frame_safe(mut buffer: &mut [u32; WIDTH * HEIGHT]) -> u32 {
    let mut f = FRAME.fetch_add(1, Ordering::Relaxed);

    if f == 0 {
        reset_buffer(&mut buffer);
    }

    if f < 450 {
    for y in 0..HEIGHT {
        for x in 0..WIDTH {
            //buffer[y * WIDTH + x] = (buffer[y * WIDTH + x] - 1 + buffer[y * WIDTH + x].wrapping_add((x ^ y * y) as u32) / 200) | 0xFF_00_00_00;
            buffer[y * WIDTH + x] = buffer[y * WIDTH + x] + (0x00_00_00_01 * 1 as u32) | 0xFF_00_00_00;
        }
    }
    } else {
    for y in 0..HEIGHT {
        for x in 0..WIDTH {
            buffer[y * WIDTH + x] = buffer[y * WIDTH + x] - (0x00_00_00_01 * 1 as u32) | 0xFF_00_00_00;
        }
    }
    }

    if f > 600 {
        FRAME.store(0, Ordering::Relaxed);
        reset_buffer(&mut buffer);
        f = FRAME.fetch_add(1, Ordering::Relaxed);
        LOOP.fetch_add(1, Ordering::Relaxed);
        //COL.fetch_add(1, Ordering::Relaxed);
        //return 0;
    }

    let lines = [
        (300, 500, -1, -1, 0, 250),
        (300, 500, 1, -1, 0, 250),
        (300 - 250, 500 - 250, 1, -1, 0, 125),
        (300 + 250, 500 - 250, -1, -1, 0, 125),
        (300, 500 - 250, -1, -1, 0, 125),
        (300, 500 - 250, 1, -1, 0, 125),
    ];

    for i in 0..1{
    for offset in [-3, -5, 3, 7].iter() {
    for d in [1, 8, 20, 37].iter() {
        for line in &lines {
            let (x, y, dx, dy, steps, max_steps) = line;
            draw_line(&mut buffer, *x, *y + *offset, *dx * *d, *dy * *d, *steps + (f as i32), *max_steps / *d);
        }
    }
    }
    }

    let diags = [
        (300 + 10, 500 - 10, -1, -1, 0, 250),
        (300 - 10, 500 - 10, 1, -1, 0, 250),
        (300 + 20, 500 - 20, -1, -1, 0, 250),
        (300 - 20, 500 - 20, 1, -1, 0, 250),
        (300 + 30, 500 - 30, -1, -1, 0, 250),
        (300 - 30, 500 - 30, 1, -1, 0, 250),

    ];

    if f > 25 {
    for line in &diags {
        let (x, y, dx, dy, steps, max_steps) = line;
        draw_line(&mut buffer, *x, *y, *dx, *dy, *steps + (f as i32) - 25, *max_steps);
    }
    }

    for d in [1, 3, 9, 27].iter() {
    if f > 100 {
    for line in &lines {
        let (x, y, dx, dy, steps, max_steps) = line;
        //draw_line(&mut buffer, *dx * *steps + *x, *dy * *steps + *y, -*dx, -*dy, *steps + (f as i32) - 200, *max_steps);
        draw_line(&mut buffer, *x + *dx * *max_steps, *y + *dy * *max_steps, -*dx * d, -*dy * d, *steps + (f as i32) - 100, *max_steps / *d);
    }
    }
    }


    /*
    for y in 0..HEIGHT {
        for x in 0..WIDTH {
            let (a, b) = (x - WIDTH / 2, (y - HEIGHT / 2 - (f as usize % HEIGHT)));
            if a * a + b * b < 100 * 100 {
                buffer[y * WIDTH + x] = 0xFF_00_00_FF;
            } else {
                buffer[y * WIDTH + x] = 0xFF_00_00_00;
            }
        }
    }*/

    return 1;
}
