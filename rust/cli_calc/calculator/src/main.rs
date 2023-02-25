use std::env::{args, Args};

fn main() {
    let mut args: Args = args();
    
    let first = args.nth(1).unwrap();
    let operator = args.nth(0).unwrap().chars().next().unwrap();
    let second = args.nth(0).unwrap();

    let first_number = first.parse::<f64>().unwrap();
    let second_number = second.parse::<f64>().unwrap();



    let result = operate(operator, first_number, second_number);
    
    println!("{:?}", output(first_number, operator, second_number, result));
    
}
fn output(first_number: f64, operator: char, second_number: f64, result: f64) -> String {
    return format!("{} {} {} = {}", first_number, operator, second_number, result);
}

fn operate(operator: char, first_number: f64, second_number: f64) -> f64 {

    match operator {
        '+' => first_number + second_number,
        '-' => first_number - second_number,
        '/' => first_number / second_number,
        '*' | 'x' | 'X' => first_number * second_number,
        _ => panic!("Invalid operator used.")
    }
}
