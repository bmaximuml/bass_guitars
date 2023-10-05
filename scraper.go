package main

import (
	"flag"
	"os"
	"strings"

	"github.com/PuerkitoBio/goquery"
)

func parseArguments() ([]string, string) {
	var urls string
	var selector string
	flag.StringVar(&urls, "urls", os.Getenv("SCRAPE_URLS"), "URLs to scrape, separated by space")
	flag.StringVar(&selector, "selector", os.Getenv("SELECTOR"), "CSS selector to use for scraping")
	flag.Parse()

	urlList := strings.FieldsFunc(urls, func(r rune) bool {
		return r == ',' || r == ';'
	})

	return urlList, selector
}

func scrapeBassGuitarInfo(urls []string, selector string) {
	for _, url := range urls {
		response, err := goquery.NewDocument(url)
		if err != nil {
			println("Failed to fetch the webpage")
			continue
		}

		response.Find(selector).Each(func(index int, element *goquery.Selection) {
			println(element.Text())
		})
	}
}

func main() {
	urls, selector := parseArguments()
	scrapeBassGuitarInfo(urls, selector)
}
