use crate::helpers;

pub fn task_01() -> Option<u128> {
    let raw_content = helpers::read_input(2);
    let instructions = raw_content
        .lines()
        .map(|x| x.split(" ").collect::<Vec<_>>());
    let mut hor: u32 = 0;
    let mut ver: u32 = 0;

    for instruction in instructions {
        let movement = instruction[0];
        let amt = instruction[1].parse::<u32>().unwrap();

        match movement {
            "forward" => {
                hor += amt;
            }
            "up" => {
                ver -= amt;
            }
            "down" => {
                ver += amt;
            }
            _ => {
                panic!("Invalid movement {}", movement);
            }
        };
    }
    return Some((hor * ver) as u128);
}

pub fn task_02() -> Option<u128> {
    let raw_content = helpers::read_input(2);
    let instructions = raw_content
        .lines()
        .map(|x| x.split(" ").collect::<Vec<_>>());
    let mut hor: u32 = 0;
    let mut ver: u32 = 0;
    let mut aim: u32 = 0;

    for instruction in instructions {
        let movement = instruction[0];
        let amt = instruction[1].parse::<u32>().unwrap();

        match movement {
            "forward" => {
                hor += amt;
                ver += aim * amt;
            }
            "up" => {
                aim -= amt;
            }
            "down" => {
                aim += amt;
            }
            _ => {
                panic!("Invalid movement {}", movement);
            }
        };
    }
    return Some((hor * ver) as u128);
}
