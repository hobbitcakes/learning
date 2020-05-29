package main

import (
	"log"
	"os/exec"
	)

func openChrome() {
    cmd := exec.Command(CHROME_BINARY)
    err := cmd.Start()
    if err != nil {
        log.Fatal(err)
    }

    string message = "Waiting on " + CHROME_BINARY
    log.Printf(message)
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
    sleep()
    openChrome()
}
