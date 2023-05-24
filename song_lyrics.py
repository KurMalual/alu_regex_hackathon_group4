#!/usr/bin/python

import re

# Regular Expression Pattern
pattern = r'\[Verse (\d+)\]\s(.+)'

# Test Input - Lyrics of "We Are the World"
input_string = """[Verse 1]
There comes a time when we heed a certain call
[Verse 2]
We can't go on pretending day by day
[Verse 3]
Well,send them your heart so they'll know that someone cares"""

# Matching using Regular Expression
matches = re.findall(pattern, input_string)

if matches:
    for match in matches:
        verse_number = match[0]
        lyrics = match[1]
        print("Verse Number:", verse_number)
        print("Lyrics:", lyrics)
        print("---")
else:
    print("No matches found.")

