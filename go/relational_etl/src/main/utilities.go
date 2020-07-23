package main

import "os"

// get_variables are used to hold environmental variables read by the app
func GetVariables() map[string]string {
	config := make(map[string]string)
	config["postgresDb"] = os.Getenv("DATABASE")
	config["postgresUser"] = os.Getenv("USERNAME")
	config["postgresPassword"] = os.Getenv("PASSWORD")
	config["postgresIP"] = os.Getenv("POSTGRES_IP_ADDRESS")
	config["integrationTest"] = os.Getenv("INT_TEST")

	return config
}
