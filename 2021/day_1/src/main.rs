use std::fs;

fn part_1(depth_measurements: &String) -> u32
{
    let mut line_count:u32 = 0;
    let mut last_measurement:u32 = 0;
    let mut increment_count: u32 = 0;
    for line in depth_measurements.lines() {
        let depth_measurement: u32 = line.parse::<u32>().unwrap();
        if (line_count != 0) && (depth_measurement > last_measurement){
            increment_count += 1;
        }
        last_measurement = depth_measurement;
        line_count += 1;

    }

    increment_count
}

fn part_2(depth_measurements: &String) -> u32
{
    let mut line_count:u32 = 0;
    let mut last_measurement:u32 = 0;
    let mut increment_count: u32 = 0;
    for line in depth_measurements.lines() {
        let depth_measurement: u32 = line.parse::<u32>().unwrap();
        if (line_count != 0) && (depth_measurement > last_measurement){
            increment_count += 1;
        }
        last_measurement = depth_measurement;
        line_count += 1;

    }

    increment_count
}


fn main() {
    let depth_measurements = fs::read_to_string("/Users/lschubert/Documents/advent_of_code/2021/day_1/input_day1.txt")
        .expect("Should have been able to read the file");
    
    let part_1_answer = part_1(&depth_measurements);

    let part_2_answer = part_2(&depth_measurements);

    println!("the increment count for part_1 is {part_1_answer}");

    println!("the increment count for part_2 is {part_2_answer}");
}
