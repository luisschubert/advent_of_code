use std::fs;

fn main() {
    let depth_measurements = fs::read_to_string("/Users/lschubert/Documents/advent_of_code/2021/day_1/input_day1.txt")
        .expect("Should have been able to read the file");

    let mut line_count:u32 = 0;
    let mut last_measurement:u32 = 0;
    let mut increment_count: u32 = 0;
    for line in depth_measurements.lines() {
        let depth_measurement: u32 = line.parse::<u32>().unwrap();
        if (line_count != 0) && (depth_measurement >last_measurement){
            increment_count += 1;
        }
        last_measurement = depth_measurement;
        line_count += 1;

    }

    println!("the increment count is {increment_count}");
}
