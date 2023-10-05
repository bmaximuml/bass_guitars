use clap::{App, Arg};
use dotenv::dotenv;
use std::env;
use reqwest::blocking::get;
use select::document::Document;
use select::predicate::Predicate;
use select::predicate::Class;

fn parse_arguments() {
    dotenv().ok();

    let matches = App::new("Bass Guitar Scraper")
        .arg(Arg::with_name("urls")
            .value_name("URLs")
            .multiple(true)
            .help("URLs to scrape, separated by space")
            .default_value(&env::var("SCRAPE_URLS").unwrap_or_default())
            .use_delimiter(true))
        .arg(Arg::with_name("selector")
            .short("s")
            .long("selector")
            .value_name("SELECTOR")
            .help("CSS selector to use for scraping")
            .default_value(&env::var("SELECTOR").unwrap_or("h3.bass-guitar-name".to_string())))
        .get_matches();

    let urls: Vec<&str> = matches.values_of("urls").unwrap_or_default().collect();
    let selector = matches.value_of("selector").unwrap_or("h3.bass-guitar-name");
    scrape_bass_guitar_info(&urls, selector);
}

fn scrape_bass_guitar_info(urls: &[&str], selector: &str) {
    for url in urls {
        let response = get(url);
        match response {
            Ok(res) => {
                if res.status().is_success() {
                    let document = Document::from_read(res).unwrap();
                    for node in document.find(Class(selector)) {
                        println!("{}", node.text());
                    }
                } else {
                    println!("Failed to fetch the webpage");
                }
            }
            Err(e) => println!("Error: {}", e),
        }
    }
}

fn main() {
    parse_arguments();
}
