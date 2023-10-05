package main

import (
	"fmt"
	"github.com/PuerkitoBio/goquery"
	"net/http"
)

func scrapeBassGuitarInfo(url string) {
	response, err := http.Get(url)
	if err != nil {
		fmt.Println("Failed to fetch the webpage")
		return
	}
	defer response.Body.Close()

	if response.StatusCode != http.StatusOK {
		fmt.Println("Failed to fetch the webpage")
		return
	}

	doc, err := goquery.NewDocumentFromReader(response.Body)
	if err != nil {
		fmt.Println("Error reading the response body:", err)
		return
	}

	// Scrape relevant information from the webpage
	// Example: Get bass guitar names and features
	doc.Find(".bass-guitar-name").Each(func(index int, element *goquery.Selection) {
		fmt.Printf("Bass Guitar Name: %s\n", element.Text())
	})

	doc.Find(".bass-guitar-features").Each(func(index int, element *goquery.Selection) {
		fmt.Printf("Bass Guitar Features: %s\n", element.Text())
	})
}

func main() {
	url := "https://example.com/bass_guitars"
	scrapeBassGuitarInfo(url)
}
