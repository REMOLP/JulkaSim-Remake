package main

import "fmt"

var julkaAnsw = [...]string{"hej", "GÓWNO INCELU", "ZAMKNIJ SIĘ INCELU", "MĘŻCZYŹNI NIE POWINNI MIEĆ PRAW", "O my God... Musze posłuchać KPOPu, wkurwiles mnie Incelu", "ZAMKNIJ SIĘ INCELU", "Jajcooo", "KAPITALIZM POWODUJE NIERÓWNOŚCIIII SOCJALIZM NAJLEPSZY!!!", "MĘŻCZYŹNI NIE POWINNI MIEĆ PRAW"};

func main(){
	var userInput string;

	for i := 0; i < len(julkaAnsw); {
		fmt.Print("TY: ")
		fmt.Scanln(&userInput);
		fmt.Println("JULKA: " + julkaAnsw[i]);
		i++;
	}

	fmt.Println("Julka zablokowała Cię...")
}
