#!/usr/bin/python3
import re

def extract_twitter_handles(text):
    pattern = r'@([A-Za-z0-9_]+)'
    twitter_handles = re.findall(pattern, text)
    return twitter_handles
text = "I'm excited to follow @KuronIC and @islam123 on Twitter!"
handles = extract_twitter_handles(text)
print(handles)
