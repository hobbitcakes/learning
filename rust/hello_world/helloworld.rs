#[cfg(target_os = "linux")]
fn are_you_on_linux() {
  	println!("You are running linux!");
}

fn main() {
	println!("Hello World!");
	are_you_on_linux();
}

