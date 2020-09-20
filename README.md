# Learning
Catch-all repository to store what I'm learning.


## Ansible



## Linux

### find

### sed

### awk

### regex

### vim

### jq



## Go

### Quick Start

Steps I often forget or have to google.

```
# After creating a blank dir, initialize it as a module
go mod init <module-name>

# After coding a bit, remember to install
go install
```





### Cobra

How do you create a great, fun to use CLI? Use Cobra!

```shell
# Download Cobra
go get github.com/spf13/cobra

# Change to the package directory
cd $GOPATH/src/github.com/spf13/cobra/cobra

# Build/Install the Cobra binary
go install ; go build

# Navigate to the example
cd git:learning/golang/jared-cli/

# Initialize your module with Cobra init
cobra init . --pkg-name "<package-name>"

# Add a command
cobra add "<command>"

# Add subcommand, the -p flag is looking for the internal cmd in the code. Like rootCmd.
cobra add "<subcommand>" -p "<parentCmd>"
```





## Python

Random Forest 

Automate the Boring Things





## Java





## General CS

