use std::io::{self, Write};

struct R(u64);
impl R {
    fn n(&mut self) -> usize {
        self.0 ^= self.0 << 13;
        self.0 ^= self.0 >> 7;
        self.0 ^= self.0 << 17;
        (self.0 % 5) as usize
    }
}

fn main() {
    let s = ["🍒", "🍉", "🥭", "🔔", "⭐"];
    let mut b = 100;
    let mut r = R(std::time::SystemTime::now().duration_since(std::time::UNIX_EPOCH).unwrap().as_secs());

    println!("**********************\nWelcome to  Slots\nSymbols: 🍒 🍉 🥭 ⭐ 🔔\n**********************");

    while b > 0 {
        print!("Current balance: ${}\nPlace your bet amount: ", b);
        io::stdout().flush().unwrap();
        let mut t = String::new();
        if io::stdin().read_line(&mut t).is_err() || t.trim().is_empty() { break; }
        let v: i32 = match t.trim().parse() {
            Ok(n) if n > 0 && n <= b => n,
            _ => { println!("Invalid bet"); continue; }
        };
        b -= v;
        let w: Vec<_> = (0..3).map(|_| s[r.n()]).collect();
        println!("*************\n{} | {} | {}\n*************", w[0], w[1], w[2]);
        if w.iter().all(|&x| x == w[0]) {
            let p = v * match w[0] {
                "🍒" => 3, "🍉" => 4, "🥭" => 5, "🔔" => 10, "⭐" => 20, _ => 0
            };
            println!("You won ${}", p);
            b += p;
        } else {
            println!("Sorry you lose this round");
        }
    }
}
