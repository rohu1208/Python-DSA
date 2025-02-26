"""Keep Asking char from user until he press Q/q """

result = ""
while True:
    ch = input("Enter A character")
    if ch == "q" or ch == "Q":
        break
    result += ch
print(result)
