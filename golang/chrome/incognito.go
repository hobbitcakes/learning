package main

import (
	"log"
	"os/exec"
)

const CHROME_BINARY = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
const FIREFOX_BINARY = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"

func openChrome() {
	cmd := exec.Command(FIREFOX_BINARY, "-private")
	err := cmd.Start()
	if err != nil {
		log.Fatal(err)
	}

	mess := "Waiting on " + CHROME_BINARY
	log.Printf(mess)
	err = cmd.Wait()
	log.Printf("Command Finished")

}

func sleep() {
	cmd := exec.Command("/bin/sleep", "5")
	err := cmd.Start()
	if err != nil {
		log.Fatal(err)
	}
	log.Printf("Waiting for command to finish...")
	err = cmd.Wait()
	log.Printf("Command finished")

}

func main() {
	openChrome()
}
