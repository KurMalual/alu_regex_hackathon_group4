#!/usr/bin/python

import re

# Define the pattern using a regular expression
pattern = r"Why did the .*? Because.*"

# The jokes you provided
joke1 = "Why did the math book look sad? Because it had too many problems!"
joke2 = "Why did the computer go to the doctor? Because it had a virus!"

# Match the first joke against the pattern
match1 = re.match(pattern, joke1)

# Check if a match is found for the first joke
if match1:
    print("The first joke matches the pattern!")
else:
    print("The first joke does not match the pattern.")

# Match the second joke against the pattern
match2 = re.match(pattern, joke2)

# Check if a match is found for the second joke
if match2:
    print("The second joke matches the pattern!")
else:
    print("The second joke does not match the pattern.")
