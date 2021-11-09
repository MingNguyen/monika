import cv2
import base64
monika = cv2.imread('monika.png',0)
a = [[]]
for i in range(monika.shape[0]):
    for j in range(monika.shape[1]):
        if monika[i][j] == 0:
            a[i].append(0b0)
        else:
            a[i].append(0b1)
    if  i == monika.shape[0] - 1 and j == monika.shape[1] - 1:
        break
    a.append([])
b = ''
length_max, length_min, depth_max,  depth_min = 0,monika.shape[0] , 0, monika.shape[1]
for i in range(monika.shape[0]):
    for j in range(monika.shape[1]):
        if a[i][j] == 0b1:
            if  length_max < i:
                length_max = i
            if length_min > i:
                length_min = i
            if depth_max < j:
                depth_max = j
            if depth_min > j:
                depth_min = j
bit_resource = [[]]
for i in range(length_min,length_max+1):
    for j in range(depth_min,depth_max+1):
        bit_resource[i - length_min].append(a[i][j])
    if i == length_max and j == depth_max:
        break
    bit_resource.append([])

for i in range(len(bit_resource)):
    for j in range(len(bit_resource[0])):
        b += str(bit_resource[i][j])
    b += '\n'
c = open('monika.txt','w+')
c.write(b)
c.close()
d,k,l = [''],1,0
for i in range(len(bit_resource)):
    for j in range(len(bit_resource[0])):
        d[l] += str(bit_resource[i][j])
        if k % 8 !=0:
            k += 1
        else:
            d[l] = chr(int(d[l],2))
            d.append('')
            k += 1
            l += 1
    pass
e = ''
for i in range(len(d)):
    e += d[i]
e = str(base64.urlsafe_b64decode(e.encode('utf-8')))
e = e.strip('b').strip('\"')
f = open('output.txt','w+')
f .write(e)
f.close()