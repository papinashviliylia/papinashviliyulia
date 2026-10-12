text = input()
result = ""

for i in range(len(text)):
    if i == 0 or text[i - 1] == ' ':
        result += text[i].upper() 
    else:
        result += text[i].lower()

print(result)