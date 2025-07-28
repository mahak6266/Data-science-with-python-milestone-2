# Q1 write a program to find check is a string has only octal digit. Given string ['789','123','004']

import re
string = ['789','123','004']
regex = "^[0-7]+$"
for num in string:
    result = re.match(regex, num)
    if result:
        print(f"string {num} has only octat digit")
    else:
        print(f"string {num} has not octat digit")
        
# Q2 Extract the user id, domain name and suffix from the following email addresses.
# email = '''zuck@facebook.com, sundar33@google.com, jeff42@amazon.com'''

import re
emails = ["zuck@facebook.com", "sundar33@google.com", "jeff42@amazon.com"]
pattern = "(\w+)@(\w+).(\w+)"
for email in emails:
    match = re.findall(pattern, email)
    match = list(match[0])
    user_id = match[0]
    domain_name = match[1]
    suffix = match[2]
    print(f"User ID: {user_id}")
    print(f"Domail name: {domain_name}")
    print(f"Suffix: {suffix}")
    print()
    
# Q3 split the following trregular sentence into proper words.
# sentence = '''A, very  very; irregular_sentence ''' ## expected output: A vrey very irregular sentence

import re
sentence = """A, very  very; irregular_sentence"""
print(sentence)
sentence = sentence.strip('"')
processed_sentence = re.findall(r"[a-zA-Z0-9]+", sentence)
processed_sentence = ' '.join(processed_sentence)
print(processed_sentence)

# Q4 Clean the following tweet so that it contains only the user's message. This is, remove all URLS, hashtags, mentions, punctuation, 
# RTs and CCs. # tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0px0d 
# cc: @garybernhardt @rstats'''
# Expected output: 'Good advice What I would do differently if I was learning to code today

import re
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0px0d 
       # cc: @garybernhardt @rstats'''
tweet = re.sub(r'http\S+|www\S+','', tweet) # remove URLS
tweet = re.sub(r'#\w+','', tweet) # remove hashtages
tweet = re.sub(r'@\w+','', tweet) # remove mentions
tweet = re.sub(r'[^\w\s]','', tweet) # remove punctuations
tweet = re.sub(r'\bRT\b|\bcc\b','', tweet) # remove RTs and cc
cleaned_tweet = re.findall(r"[a-zA-Z]+", tweet) 
cleaned_tweet = ' '.join(cleaned_tweet) # remove extra space
print(cleaned_tweet)

# Q5 Extract all the text portion between the tags from the following HTML page:
# http://raw.githubusercontent.com/selva86/datasets/master/sample.html

import requests
r = requests.get("http://raw.githubusercontent.com/selva86/datasets/master/sample.html")
html_text = r.text
cleaned_text = re.sub(r'<[^>]+>','',html_text)
for text in cleaned_text.splitlines():
    if text.strip():
        extracted_text = text.strip()
print(extracted_text)

# Q6 Given below list of words, identify the words that begin and end with same character.

import re
words = ["civic", "trust", "windows", "maximum", "musemums", "aa", "as"]
matched_words = []
for word in words:
    match = re.match(r"^(.)(.*?)\1$", word, re.IGNORECASE)
    if match:
        matched_words.append(word)
print(matched_words)