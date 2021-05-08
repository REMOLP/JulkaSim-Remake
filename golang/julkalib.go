package main

// Na razie gówno z tego wszystkiego wyszło :)

import (
	"fmt"
	"os"
)

import "gopkg.in/ini.v1"	

var configFilePath = "./config.ini";
var loopedAnsw = false;
var randomizeAnsw = false;
var stoppingKeywords []string;
var userCustomJulkaAnsw [3]string;



// Pomocnicza funkcja do sprawdzania
// (jak sama nazwa wskazuje) czy wystąpił błąd.	
// func check(e error) {
    // if e != nil {
        // panic(e)
    // }
// }


// Na razie chuja nie działa....
func fetchConfigData() bool {
	cfg, err := ini.Load(configFilePath);

	if err != nil{
		fmt.Printf("Gówno :)\t %v", err);
		os.Exit(1);
	}
	
	randomizeAnsw = cfg.Section("").Key("randomizeResp").MustBool();
	fmt.Println("randomizeAnsw:\t", randomizeAnsw);

	loopedAnsw = cfg.Section("").Key("looped").MustBool();
	fmt.Println("loopedAnsw:\t", loopedAnsw);

	customRespStatus := cfg.Section("").Key("customRespStatus").MustBool();

	if(customRespStatus == true){
		fmt.Println("'customRespStatus' w pliku konfiguracyjnym jest równy: True!");
		userCustomJulkaAnsw = [...]string{"Custom1", "Custom2", "Custom3"};
		fmt.Println("userCustomJulkaAnsw:\t", userCustomJulkaAnsw);
	}

	return true;
}
