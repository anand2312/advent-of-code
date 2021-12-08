use std::collections::{HashMap, HashSet};

use crate::helpers;


fn parse_line(ln: &str) -> Vec<Vec<&str>> {
    ln
        .split(" | ")
        .map(|x| x.split_whitespace().collect::<Vec<&str>>())
        .collect::<Vec<Vec<&str>>>()
}


pub fn task_01() -> String {
    let raw_input = helpers::read_input(8);
    let parsed_lines = helpers::lines(&raw_input).iter().map(|x| parse_line(x)).collect::<Vec<Vec<Vec<&str>>>>();
    let mut count = 0;

    for line in parsed_lines {
        for pattern in &line[1] {
            let length = pattern.len();
            if length == 2 || length == 3 || length == 4 || length == 7 {
                count += 1;
            }
        }
    };
    return count.to_string()
}


pub fn task_02() -> String {
    let raw_input = helpers::read_input(8);
    let parsed_lines = helpers::lines(&raw_input).iter().map(|x| parse_line(x)).collect::<Vec<Vec<Vec<&str>>>>();
    let mut sum = 0;

    for line in parsed_lines {
        println!("{:?}", &line[0]);
        let mut d: HashMap<usize, HashSet<char>> = HashMap::new();
        let mut output = String::new();

        for pattern in &line[0] {
            let as_set: HashSet<char> = pattern.chars().collect();
            match (as_set.len(), as_set.intersection(&d[&4]).count(), as_set.intersection(&d[&2]).count()) {
                (2, _, _) => { d.insert(1, as_set); },
                (3, _, _) => { d.insert(7, as_set); },
                (4, _, _) => { d.insert(4, as_set); },
                (7, _, _) => { d.insert(8, as_set); },
                (5, 2, _) => { d.insert(2, as_set); },
                (5, 3, 1) => { d.insert(5, as_set); },
                (5, 3, 2) => { d.insert(3, as_set); },
                (6, 4, _) => { d.insert(9, as_set); },
                (6, 3, 1) => { d.insert(6, as_set); },
                (6, 3, 2) => { d.insert(0, as_set); },
                _ => panic!("Bruh moment")
            }
        };

        // calculate the output now
        for pattern in &line[1] {
            let as_set: HashSet<char> = pattern.chars().collect();

            for (num, pat) in d.iter() {
                if &as_set == pat {
                    output.push_str(num.to_string().as_str());
                }
            }
        }
        sum += output.parse::<i32>().unwrap();
    }
    return sum.to_string();
}

