pub fn add(left: i32, right: i32) -> i32 {
    left + right
}

pub fn add_two(num: i32) -> i32 {
    return num + 2;
}

pub fn greeting(name: &str) -> String {
    format!("Hello {}!", name)
}

#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }

    #[test]
    fn it_works_with_negatives() {
        let result = add(-2, 2);
        assert_eq!(result, 0);
    }

    #[test]
    fn it_fails() {
        let result = add(-2, 2);
        assert_ne!(result, 1);
    }

    #[test]
    fn larger_can_hold_smaller() {
        let larger = Rectangle {
            height: 5,
            width: 5,
        };

        let smaller = Rectangle {
            height: 4,
            width: 4,
        };

        assert!(larger.can_hold(&smaller));
    }

    #[test]
    fn smaller_cannot_hold_larger() {
        let larger = Rectangle {
            height: 5,
            width: 5,
        };

        let smaller = Rectangle {
            height: 4,
            width: 4,
        };

        assert!(!smaller.can_hold(&larger));
    }

    #[test]
    fn greeting_contains_name() {
        let result = greeting("Carol");

        assert!(result.contains("Carol"));
    }
}
