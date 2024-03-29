use std::env;
use std::fs;

pub fn read_input(day: u32) -> String {
    // Reads the specified file and returns it's contents as a string.
    let cwd = env::current_dir().unwrap();
    let mut dir = cwd.parent().unwrap().parent().unwrap().to_path_buf();
    dir.push("inputs");
    let filename = format!("day_{:02}.txt", day);
    dir.push(filename);
    let mut out =  fs::read_to_string(dir).expect(
        format!(
            "File for day {} could not be opened. Has it been downloaded?",
            day
        )
        .as_str(),
    );
    trim_newline(&mut out);
    out
}

fn trim_newline(s: &mut String) {
    if s.ends_with('\n') {
        s.pop();
        if s.ends_with('\r') {
            s.pop();
        }
    }
}

pub fn lines(input: &String) -> Vec<&str> {
    return input.lines().collect();
}

pub fn intlines(input: &String) -> Vec<i32> {
    // Split the given input at newlines and convert each element to an integer
    return input.lines().map(|x| x.parse::<i32>().expect(format!("Converting {} to i32 failed", x).as_str())).collect();
}
