import base64
a = open('monika.txt','r')
data = a.read()
re_data = ""
for i in data:
    if i != '\n': re_data += i
code = ""
character = ""
for i in range(len(re_data)):
    if i % 8 != 1:
        character += re_data[i-1]
    else:
        code += chr(int(character,2))
        character = ""
decode = str(base64.urlsafe_b64decode(code.encode('utf-8')))
decode = decode.strip('b').strip('\"')
print(str(decode))
