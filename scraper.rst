use reqwest::blocking::get;
use select::document::Document;
use select::predicate::{Class, Name};

fn scrape_bass_guitar_info(url: &str) {
    let response = get(url);
    match response {
        Ok(res) => {
            if res.status().is_success() {
                let document = Document::from_read(res).unwrap();
                
                // Scrape relevant information from the webpage
                // Example: Get bass guitar names and features
                for node in document.find(Class("bass-guitar-name")) {
                    println!("Bass Guitar Name: {}", node.text());
                }
                for node in document.find(Class("bass-guitar-features")) {
                    println!("Bass Guitar Features: {}", node.text());
                }
            } else {
                println!("Failed to fetch the webpage");
            }
        }
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    let url = "https://example.com/bass_guitars";
    scrape_bass_guitar_info(url);
}
