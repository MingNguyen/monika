import cv2
'''
Part 1 of the code:
we will import the into our program, then we'll convert the image into binary 
and store it in variable name "image_binary".
'''
image = cv2.imread('monika.png',0)
image_binary = [[]]
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image[i][j] == 0:
            image_binary[i].append(0b0)
        else:
            image_binary[i].append(0b1)
    if  i == image.shape[0] - 1 and j == image.shape[1] - 1:
        break
    image_binary.append([])
'''
Part 2:
the image have the unused edge(full of black), to delete that edge, we need to 
find the index that limit the value of the "image_binary".
I will call it "length_max", "length_min", "depth_max", "depth_min"
'''
length_max, length_min, depth_max,  depth_min = 0,image.shape[0] , 0, image.shape[1]
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image_binary[i][j] == 0b1:
            if  length_max < i:
                length_max = i
            if length_min > i:
                length_min = i
            if depth_max < j:
                depth_max = j
            if depth_min > j:
                depth_min = j
'''
Part 3:
we need to create a new generator to convert "image_binary" to represent
the bit of the image, this generator is different from "image_binary" because I
have reduced the edge. I will call it the "bit_resource"
'''
bit_resource = [[]]
for i in range(length_min,length_max+1):
    for j in range(depth_min,depth_max+1):
        bit_resource[i - length_min].append(image_binary[i][j])
    if i == length_max and j == depth_max:
        break
    bit_resource.append([])
b = ''
'''
to end part 3, I will store the bit value to the file name "binary.txt"
'''
for i in range(len(bit_resource)):
    for j in range(len(bit_resource[0])):
        b += str(bit_resource[i][j])
    b += '\n'
c = open('binary.txt','w+')
c.write(b)
c.close()
'''
Part 4
Now we convert the binary into Ascii(8bit) characterm And I will store it in
the file name "base64.txt", However, if you open that txt file, we can not
understand anything, because I is representing in the base 64 letters(6bit).
This is the quiz from the author of the image. we have to covert it again from
base64 to ascii for reading

'''
base64_char,output,k,l = [''],[0],1,0
for i in range(len(bit_resource)):
    for j in range(len(bit_resource[0])):
        base64_char[l] += str(bit_resource[i][j])
        if k % 8 !=0:
            k += 1
        else:
            m = int(base64_char[l],2)
            x = chr(m)
            base64_char[l] = x
            #a letter in ascii have an correspoding letter in base64
            #these code are to convert the 8bit to the 6bit in the same character
            if x in '0123456789': output[l] = m + 4
            elif x == '+': output[l] = 62
            elif x == '/': output[l] = 63
            elif x == '=' : output[l] = 13
            elif 65<=m<=90: output[l] = m - 65
            else: output[l] = m - 71
            base64_char.append('')
            output.append(0)
            k += 1
            l += 1
    pass
e = ''
# These code are to store the base64 code in txt file
for i in range(len(base64_char)):
    e += base64_char[i]
f = open('base64.txt','w+')
f .write(e)
f.close()
del f
'''
The last part, we connect all the 6bit together and have a string of bit, translate 
those bit into ascii character and we have the understandable letter
'''
output_text,output_bit,flag,bit = '','',0,''
for i in output:
        bit = "{0:b}".format(i)
        output_bit += (6-len(bit))*'0' + bit
for i in range(len(output_bit)):
    if i %8 == 0 and i != 0: 
        a = output_bit[i-8:i]
        if int(a,2) < 0: break
        output_text += chr(int(a,2))
        i = 0
    else: i += 1
g = open('ouput letter.txt','w+')
g.write(output_text)
g.close()