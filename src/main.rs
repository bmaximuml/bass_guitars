use clap::{Arg, ArgAction, Command, value_parser};
use reqwest::blocking::get;
use select::document::Document;
use select::predicate::Class;

fn parse_arguments() -> (Vec<String>, String) {
    let matches = Command::new("Bass Guitar Scraper")
        .arg(Arg::new("urls")
            .action(ArgAction::Append)
            .value_parser(value_parser!(String))
            .short('u')
            .long("url")
            .value_name("urls")
            // .multiple_values(true)
            .help("URLs to scrape, separated by comma"))
        .arg(Arg::new("selector")
            .short('s')
            .long("selector")
            .value_name("selector")
            .help("CSS selector to use for scraping")
            .default_value("h3.bass-guitar-name"))
        .get_matches();

    let urls: Vec<String> = matches.get_many("urls").expect("URLs is required").cloned().collect();
    let selector = matches.get_one::<String>("selector").unwrap().to_string();
    (urls, selector)
}

fn scrape_bass_guitar_info(urls: &[String], selector: &str) {
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
    let (urls, selector) = parse_arguments();
    scrape_bass_guitar_info(&urls, &selector);
}
