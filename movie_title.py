#!/usr/bin/python
#regular expression
import re

#prompting the user to enter the movie title and year of release
title = input("Enter a movie title: ")
year = input("Enter the year of release: ")

string = f"Some text {title} ({year})"

pattern = r'\b[a-zA-Z\s}+ \(\d{4}\)\b'
matches = re.findall(pattern, string)

for match in matches:
 print(match)
