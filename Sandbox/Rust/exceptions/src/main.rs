use std::fs::{read_to_string, File};
use std::io::{Error, ErrorKind};

fn read_file(file_name: &String) -> Result<String, Error> {
    return read_to_string(&file_name);
}
fn main() {
    let greeting_file_result = File::open("hello.txt");
    
    match greeting_file_result {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => match File::create("hello.txt") {
                Ok(fc) => fc,
                Err(error) => panic!("Failed 😭 {}:?", error),
            },
            other_error => {
                panic!("Problem opening the file 😭 {}:?", other_error);
            }
        },
    };
    let file_name = String::from("hello2.txt");
    
    let content = read_file(&file_name).expect("Well. Shit 💩");

    println!("Content: {content}");
}
