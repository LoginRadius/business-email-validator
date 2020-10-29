package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

func getEmailDomain(email string) string {
	return strings.Split(email, "@")[1]
}

func validate(email string) bool {
	// Open the json file
	jsonFile, err := os.Open("../../src/freeEmailService.json")

	// Handle error returned from os.Open
	if err != nil {
		fmt.Println(err)
	}

	// Defer the closing of json file to enable parsing
	defer jsonFile.Close()

	byteValue, _ := ioutil.ReadAll(jsonFile)

	var result map[string]interface{}
	json.Unmarshal([]byte(byteValue), &result)

	var emailDomain string = getEmailDomain(email)

	// Returns `true` if email found in freeEmailService.json
	// file with true value, else `false`
	return result[emailDomain] != nil
}

func main() {
	// Testing with some sample emails
	validate("test@gmail.com")  // true
	validate("test@gmail1.com") // false
	validate("test@123box.net") // true
}
