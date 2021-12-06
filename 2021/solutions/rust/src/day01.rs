use crate::helpers;

pub fn task_01() -> Option<u128> {
    let raw_content = helpers::read_input(1);
    let intlines = helpers::intlines(&raw_content);
    let end = intlines.len();
    let mut count = 0;

    for i in 0..end - 1 {
        if intlines[i] < intlines[i + 1] {
            count += 1;
        }
    }
    return Some(count);
}

pub fn task_02() -> Option<u128> {
    let raw_content = helpers::read_input(1);
    let intlines = helpers::intlines(&raw_content);
    let end = intlines.len();
    let mut count = 0;

    for i in 0..end - 2 {
        if i + 3 >= end {
            break;
        }
        if intlines[i] < intlines[i + 3] {
            count += 1;
        }
    }
    return Some(count);
}
