package main

import (
	"testing"
)

func TestScrapeBassGuitarInfo(t *testing.T) {
	urls := []string{"https://example.com/bass_guitars"}
	selector := "h3.bass-guitar-name"
	bassGuitarNames, _ := scrapeBassGuitarInfo(urls, selector)

	expectedNames := []string{"Bass Guitar 1", "Bass Guitar 2"}
	if !equalSlices(bassGuitarNames, expectedNames) {
		t.Errorf("Expected %v, but got %v", expectedNames, bassGuitarNames)
	}
}

func equalSlices(a, b []string) bool {
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}
