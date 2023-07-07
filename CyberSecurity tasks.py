import re
#Opening the pcap file and allocating the data to the variable "data"
Filename = 'CyberSecurity2022.pcap'
pcap = open(Filename, "rb")
data = pcap.read()
datastr = str(data)

# ------Task 3-----
print("---------- Task 3 ---------")
pattern1 = "((http|https)://)(www.)?[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\.top" # regex pattern to find the website ending with .top
# Using pattern to search for website
task3 = re.search(pattern1, datastr)
# printing search output formatted
print('The suspected website is: ', task3.group())

# ------Task 4-----
print("---------- Task 4 ---------")
# Pattern to find the search engine
pattern2 = "((http|https)://)(www.)?[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=])"
# Using pattern to search for the search engine
task4 = re.search(pattern2, datastr)
# Printing search output from regular expression formatted
print('Search engine used: ', task4.group())

# pattern to find the keyword by using q= parameter
pattern3 = "(q\=)[a-z]{2,256}\+[^.\&]*"
# Using pattern to search for the keywords
task41 = re.search(pattern3, datastr)
# Formatting result to make it easier to see the keywords
task41s = task41.group()
task41f = task41s.replace("+", ", ").replace("q=", "")
# Printing formatted result
print('With the search keywords: ', task41f)

# pattern to search for urls starting with url=
pattern4 = "((url=)(http|https)[^\s]+)"
# Using pattern to search
task42 = re.findall(pattern4, datastr)
# Print of search result
print('possible suggested websites: ', task42)

# Pattern to find url specifically clicked
pattern5 = "((url=)(http|https)(%3A%2F%2F)[^\s]+)"
# Using pattern to search for specific url
task43 = re.search(pattern5, datastr)
# formatting the url to make it easier to read
task43s = task43.group()
task43f = task43s.replace("url=http%3A%2F%2F", "")
# Prints the result from the regular expression search from above and formatted
print('Specific website clicked: ', task43f)
print("---------- End ---------")
