/*
Copyright © 2020 NAME HERE <EMAIL ADDRESS>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/
package cmd

import (
	"fmt"
	"jared-cli/movies"

	"github.com/spf13/cobra"
)

// moviesCmd represents the movies command
var moviesCmd = &cobra.Command{
	Use:   "movies",
	Short: "A brief description of your command",
	Long: `A longer description that spans multiple lines and likely contains examples
and usage of using your command. For example:

Cobra is a CLI library for Go that empowers applications.
This application is a tool to generate the needed files
to quickly create a Cobra application.`,
	Run: func(cmd *cobra.Command, args []string) {

		file, _ := cmd.Flags().GetString("filename")
		thisMovie := movies.Movie{
			Filename: file,
			FileType: "mp4",
			Size:     1024}
		fmt.Println("movies called")
		fmt.Println(thisMovie)
	},
}

func init() {
	rootCmd.AddCommand(moviesCmd)

	// Here you will define your flags and configuration settings.

	// Cobra supports Persistent Flags which will work for this command
	// and all subcommands, e.g.:
	// moviesCmd.PersistentFlags().String("foo", "", "A help for foo")

	// Cobra supports local flags which will only run when this command
	// is called directly, e.g.:
	moviesCmd.Flags().StringP("filename", "f", "", "Filename")
	moviesCmd.MarkFlagRequired("filename")
	moviesCmd.Flags().BoolP("toggle", "t", false, "Help message for toggle")
}
