package handler

import (
	"fmt"
	"net/http"
)

func Handler(w http.ResponseWriter, r *http.Request) {
	name := r.URL.Query().Get("name")
	if name == "" {
		name = "NULL"
	}
	fmt.Fprintf(w, "Golang: Hello %s!", name)
}