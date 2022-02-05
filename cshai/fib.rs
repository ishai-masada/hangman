use cached::proc_macro::cached;

#[cached]
fn fib(n: u128) -> u128 {
    if n <= 1 {
        n
    } else {
        fib(n - 1) + fib(n - 2)
    }
}

fn main() {
    fib(40);
}

