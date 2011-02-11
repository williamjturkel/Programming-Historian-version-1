# string-to-list.py

# some strings
s1 = 'hello world'
s2 = 'howdy world!'

# list of characters
charlist = []
for char in s1:
    charlist.append(char)
print charlist

# list of 'words'
wordlist = s2.split()
print wordlist