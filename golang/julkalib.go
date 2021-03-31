package main

// Na razie gówno z tego wszystkiego wyszło :)

import (
	"fmt"
)

import "github.com/bitly/go-simplejson"

var configFilePath = "./config.json";
var loopedAnsw = false;
var randomizeAnsw = false;
var stoppingKeywords []string;
var userCustomJulkaAnsw []string;



// Pomocnicza funkcja do sprawdzania
// (jak sama nazwa wskazuje) czy wystąpił błąd.	
// func check(e error) {
    // if e != nil {
        // panic(e)
    // }
// }


// Na razie chuja nie działa....
func fetchConfigData() bool {
	jsonData, err := simplejson.NewFromReader(configFilePath);

	if err != nil{
		fmt.Println("Gówno :)");
	}

	fmt.Println(jsonData.Get("looped"));

	return true;
}
