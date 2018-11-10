package main

import (
    "fmt"
    "net/http"
    "strings"
    "log"
)

func returnCall(w http.ResponseWriter, r *http.Request) {
    r.ParseForm() 
    for k, v := range r.Form {
        fmt.Println("key:", k)
        fmt.Println("val:", strings.Join(v, ""))
    }
    fmt.Fprintf(w, "Hello MongoDB!")
}

func main() {
    http.HandleFunc("/", returnCall) // set router
    err := http.ListenAndServe(":9090", nil) // set listen port
    if err != nil {
        log.Fatal("ListenAndServe: ", err)
    }
}
