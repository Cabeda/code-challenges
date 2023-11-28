#[derive(Debug)]
struct Rectangle {
    width: u32,
    heigth: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.heigth
    }
}

struct Point<T> {
    x: T,
    y: T,
}
impl<T> Point<T> {
    fn x(&self) -> &T {
        &self.x
    }
}

fn vector() -> Vec<i32> {
    println!("#### VECTOR ####");

    let mut v = vec![1, 2, 3];

    let mut v2 = Vec::new();

    v2.push(4);

    v.push(4);

    let third = v.get(3);

    match third {
        Some(third) => println!("The third element is {third}"),
        None => println!("No third element found"),
    }

    match v.pop() {
        Some(el) => println!("Dropped {el}"),
        None => println!("No element dropped 🤔"),
    }

    return v;
}

fn hasmhmaps() {
    use std::collections::HashMap;

    println!("#### HASH ####");

    let mut scores = HashMap::new();

    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Yellow"), 50);

    for (key, value) in &scores {
        println!("{key}: {value}");
    }

    let field_name = String::from("Favorite color");
    let field_value = 30;

    scores.insert(field_name, field_value);

    // Inserts only the key and value if it isn't present
    scores.entry(String::from("Yellow")).or_insert(100);

    println!("{:?}", scores);

    // Updates the value based on the prev
    let val = scores.entry(String::from("Blue")).or_insert(0);
    *val += 1;
    println!("{:?}", scores);
}

fn main() {
    let rect: Rectangle = Rectangle {
        width: 30,
        heigth: 50,
    };
    println!("rect is {:#?}", rect);

    vector();
    hasmhmaps();

    println!(
        "The area of the rectangle is {} square pixels.",
        rect.area()
    );

    // 10. Generics

    let p = Point { x: 5, y: 4 };

    println!("p.x = {}", p.x());
}
