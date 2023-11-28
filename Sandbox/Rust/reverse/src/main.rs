fn reverse(x: i32) -> i32 {
    let mut reverse_num: i32 = 0;
    let mut temp_num = x.abs();

    while temp_num > 0 {
        match reverse_num.checked_mul(10) {
            Some(num) => {
                reverse_num = num + temp_num % 10;
                temp_num = temp_num / 10;
            }
            _ => {
                reverse_num = 0;
                temp_num = 0
            }
        }
    }

    if x < 0 {
        return reverse_num * -1;
    } else {
        return reverse_num;
    }
}

fn main() {
    assert_eq!(reverse(123), 321);
    assert_eq!(reverse(-123), -321);
    assert_eq!(reverse(1056389759), 0);
}
