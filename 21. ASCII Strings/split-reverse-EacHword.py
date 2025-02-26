""" 
we are happy
ew era yppah
"""

string = "WE are happy"
words = string.split()
print(words)

result = " ".join(w[::-1] for w in words)
print(result)
