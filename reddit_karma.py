__author__ = 'bigm141414'
# Parsing reddit json data
# json data is dictionary -> dictionary -> List -> dictionary -> dictionary
# Compare latest posts of two users and evaluate who has the bigger score.
# Print out user with biggest sore and title of the thread.
#display upvotes and downvotes


import json
import urllib2

url = "http://www.reddit.com/u/"

name1 = raw_input("what is the first user name?")
name2 = raw_input("what is the second user name?")

url1 = url + name1 + ".json"
url2 = url + name2 + ".json"

print(url1)
data1 = json.load(urllib2.urlopen(url1))
data2 = json.load(urllib2.urlopen(url2))

print(data1["data"]["children"][0]["data"]["link_title"])
print(data1["data"]["children"][0]["data"]["score"])
print(data2["data"]["children"][0]["data"]["score"])
for index, item in data:
    print index, item