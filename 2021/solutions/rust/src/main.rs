mod helpers;
mod day01;
use std::env;
use std::collections::HashMap;


fn main() {
    // add the rest of the solutions here
    // call the program as cargo run <day> <task>
    let solutions = HashMap::from([
        ("1 1", day01::task_01()),
        ("1 2", day01::task_02())
    ]);
    let args: Vec<String> = env::args().collect();
    let day = args[1].parse::<i32>().unwrap();
    let task = args[2].parse::<i32>().unwrap();
    let key = format!("{} {}", day, task);
    let res = solutions.get(key.as_str()).expect("Get panicked").expect("Solution panicked");
    println!("Day {} Task {}\nSolution: {}", day, task, res);
}
