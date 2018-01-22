#!/usr/bin/env python

import os

# https://linuxacademy.com/cp/exercises/view/id/651/module/158


# Prompt the user for the contet that should go in the file. The script should keep accepting lines of text until the user enters an empty line
def this():
    # Prompt the user for a file_name where it should write the content
    file_name = raw_input("What is the file name we should save this content to?\n")

    # If the file exists, exit with an error
    if os.path.isfile(file_name):
        print("File %s exists, please specify a blank file\n" , file_name)
        os._exit(1)

    with open(file_name, 'w') as file:
        end_of_file = False
        file_contents = []
        while not end_of_file:
            user_input = raw_input("Enter text or a blank line to quit\n") 
            if user_input:
                file_contents.append(user_input)
            else:
                end_of_file = True
        
        # Write out the file
        for line_given in file_contents:
            file.write("%s\n" % line_given)

this()
