use crate::helpers;

pub fn solution(days: i32) -> String {
    let raw_input = helpers::read_input(6);
    let fish = raw_input.split(",").map(|x| {
        x.parse::<u128>()
            .expect(format!("Converting {} to i32 failed", x).as_str())
    });

    let mut counts = vec![0; 9];

    for i in fish {
        counts[i as usize] += 1;
    }

    for _j in 0..days {
        let mut next_iteration = vec![0; 9];
        for (day, count) in counts.iter().enumerate() {
            let next = (day as i32) - 1;
            if next == -1 {
                next_iteration[6] += count;
                next_iteration[8] += count;
            } else {
                next_iteration[next as usize] += count;
            };
        }
        counts = next_iteration;
    }

    return counts.iter().sum::<u128>().to_string();
}
