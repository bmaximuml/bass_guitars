#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_scrape_bass_guitar_info() {
        let urls = vec!["https://example.com/bass_guitars"];
        let selector = "h3.bass-guitar-name";
        let (bass_guitar_names, _) = scrape_bass_guitar_info(&urls, selector);
        assert_eq!(bass_guitar_names, vec!["Bass Guitar 1", "Bass Guitar 2"]);
    }
}
