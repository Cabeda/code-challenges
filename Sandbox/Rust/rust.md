# Data types

## Scalar

- Int
  - Signed (i8, i16, i32, i64, isize)
  - Not-sgined (u8, u16, u32, u64, usize)
- Float
  - f32 and f64 (default one)
  - boolean
- Char: unicode character defined inside single quotes
- String: unicode text inside double quotes. Has fixed size
- String: unicode text inside double quotes. Can be mutated

## Compound

- Tuples
- Arrays: have a fixed size set during the declaration
- vector: like an array but can scale

Statements: instructions that PERFORM AN ACTION BUT DON'T RETURN A VALUE
Expressions: intstruction taht perform an action but return a value

## Imports

We can import crates like this:

```rust
use std::{cmp::Ordering, io};

// Imports every public item on std::collections
use std::collections::*;
```

## Common collections

### Vector

- Vectors allow you to store more than one value in a single data structure that puts all the values next to each other in memory.
- Vectors can only store values of the same type. (can use enum to circumvent this)
- They are useful when you have a list of items, such as the lines of text in a file or the prices of items in a shopping cart

```rust

let v: Vec<i32> = Vec::new();
```

### String

Rust goes way beyond by making sure we test against all valid characters and not only UTF-8. As such it might seem to be pickier but it's necessary to avoid bugs.

## Generics

### Traits

**Definition**: A trait defines functionality a particular type has and can share with other types (similar to an interface in some ways)

- We can use trait bounds to specify that a generic type can be any type that has certain behavior

We can specify one trait bound like the following

```rust
pub fn notify(item: &impl Summary)

//which is syntax sugar for

pub fn notify<T: Summary>(item: &T)
```

We can specify multiple trait bound like this

```rust
pub fn notify(item: &(impl Summary + Display))
```

A complex function that uses a lot of traits can be written using the where clause like this:

```rust
fn some_function<T, U>(t: &T, u: &U) -> i32
where
    T: Display + Clone,
    U: Clone + Debug,
{}
```

### Lifetimes

**Definition**: lifetimes ensure that references are valid as long as we need them to be.

- Rust has a borrow checker to make sure all references are valid and that the lifetime hasn't ended to soon.

```rust
fn first_word<'a>(s: &'a str) -> &'a str {}
```

```rust
&i32        // a reference
&'a i32     // a reference with an explicit lifetime
&'a mut i32 // a mutable reference with an explicit lifetime
```

```rust

// Static lifetimes as those that can live for the duration of the program
let s: &'static str = "I have a static lifetime.";

```

```rust
use std::fmt::Display;

fn longest_with_an_announcement<'a, T>(
    x: &'a str,
    y: &'a str,
    ann: T,
) -> &'a str
where
    T: Display,
{
    println!("Announcement! {}", ann);
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```
