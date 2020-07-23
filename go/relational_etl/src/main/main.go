package main

import (
	"fmt"
	EasyDatabase "github.com/bclipp/EasyDatabase"
)

func main() {
	config := GetVariables()
	var pg = EasyDatabase.PostgreSQL{
		IPAddress:        config["postgresIP"],
		PostgresPassword: config["postgresPassword"],
		PostgresUser:     config["postgresUser"],
		PostgresDB:       config["postgresDB"],
	}
	err := pg.Connect();if err != nil {
		fmt.Print(err.Error())
	}
	defer pg.Disconnect()

}
