# Bass Guitar Scraper

Bass Guitar Scraper is a tool to scrape information about bass guitars from various websites, facilitating easy comparisons and analysis.

## Installation

### Prerequisites

- Python 3.x
- Rust (latest version)
- Go (latest version)
- Node.js (for Semantic Release)
- Git (for version control)

## Usage

### Python

```bash
python scraper.py [URL1] [URL2] ...
```
Replace [URL1], [URL2], etc. with the URLs you want to scrape.
- `--selector`, -s SELECTOR : CSS selector to use for scraping. Defaults to "h3.bass-guitar-name".

### Rust

bash
```
cargo run -- [URL1] [URL2] ...
```
- Replace [URL1], [URL2], etc. with the URLs you want to scrape.
- `--selector SELECTOR` : CSS selector to use for scraping. Defaults to "h3.bass-guitar-name".

### Go

bash
```
go run main.go -urls=[URL1],[URL2],...
```
- Replace [URL1], [URL2], etc. with the URLs you want to scrape.
- `-selector SELECTOR` : CSS selector to use for scraping. Defaults to "h3.bass-guitar-name".

## Contribution

We welcome contributions to improve Bass Guitar Scraper! When contributing, please follow these guidelines:

    Use Conventional Commits for commit messages.
    Make your changes in a feature branch and create a pull request.

## License

Bass Guitar Scraper is licensed under the GNU Affero General Public License v3.0.
