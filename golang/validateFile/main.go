package main

import (
	"crypto/md5"
	"fmt"
	"github.com/pkg/sftp"
)

func main() {
	data := []byte("Hello")
        fmt.Printf("%x", md5.Sum(data)) }
