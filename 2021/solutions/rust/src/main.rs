mod day01;
mod day02;
// mod day03;
// mod day04; doesn't work
// mod day05;
mod day06;
mod day08;
mod helpers;
use std::collections::HashMap;
use std::env;

fn main() {
    // add the rest of the solutions here
    // call the program as cargo run <day> <task>
    let solutions= HashMap::from([
        ("1 1", day01::task_01()),
        ("1 2", day01::task_02()),
        ("2 1", day02::task_01()),
        ("2 2", day02::task_02()),
        ("6 1", day06::solution(80)),
        ("6 2", day06::solution(256)),
        ("8 1", day08::task_01()),
        ("8 2", day08::task_02())
    ]);
    let args: Vec<String> = env::args().collect();
    let day = args[1].parse::<i32>().unwrap();
    let task = args[2].parse::<i32>().unwrap();
    let key = format!("{} {}", day, task);
    let res = solutions
        .get(key.as_str())
        .expect("Get panicked");
    println!("Day {} Task {}\nSolution: {}", day, task, res);
}
