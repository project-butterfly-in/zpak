# Setup

## For Linux/Unix users

### For Golang project setup

- You should have golang installed.

- go get \<this repo\>

- Step 1: Put the below line in .bashrc, .zshrc, or .bashprofile file:

`alias initGo="echo \"Setting up environment for project\";export GOPATH=$GOPATH:$(pwd);export GOBIN=$GOPATH/bin;PATH=$PATH:$GOPATH:$GOBIN;export PATH;echo $GOPATH;echo $GOBIN;echo \"Setup complete\";echo \"Refreshing enviroment variables\";source ~/.zshrc;"`

- Step 2: Use `initGo` in the Go project's root directory.
