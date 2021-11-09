# monika
CONTRIBUTER: Nguyễn Gia Minh

PROGRAMING LANGUAGE: Python(version 3.10.0)

OS TESTED: Windows 10(updated to the last version)
### HOW TO RUN PROGRAM:

Download 2 files "monika.py" and "monika.png" to your computer, extract the winrar.

before run: make sure you have install package "open-cv" to you computer.

Run the file monika.py and then the translated version the meaning in the picture will be shown in 3 file txt.
### additional info:
This image is taken from the game name"DokiDoki Literarute Club" and this image is one of the easter eggs of the game. It represent the mail from a character name Monika sends to us. the original file names "Monika.chr" and after change it tail, we got this image.
### algorythms
    this code is hard to explain by document, but I hope you can understand it
first we see the image

![monika](https://user-images.githubusercontent.com/91204964/140948442-dd181bc7-dd91-4a4b-b710-69c0b8ac8445.png)

it is an 2D black and white code, looks similarly to a QR code but different in the way to translate.

the black pixel represent 0 and the white pixel represnt 1. So our idea at the beginning is to covert these binary into ascii characters and read it.

So we can convert it into a generator map of binary I will call it **image_binary**

But we can see the edge is full of black, and this data is unused. So we need to create another generator which does not have the edge and it name is **bit_resource**

From bit resource, we can convert that binary into a ascii code, after the converting, we will have the string like this:

    Q2FuIHlvdSBoZWFyIG1lPw0KDQouLi5XaG8gYXJlIH...

This is strange and we cannot read it but why. This is the point that the author of the image want to test us, the image is not fully converted, because this is just the input for another converting. Base64(6bit) to Ascii.

Every Base64 letters always have an corresponding integer. likes 'Q' means "010000", '2' means "000010", 'F' mean "000101". If we connect all these bit together, we will have a new bit string. and from this string, we can convert again into the ascii(8bit) letter:
likes we have the base 64 string:


'Q2Fu' means "010000 000010 000101 101110" means "01000000 00100001 01101110" means 'Can' in ascii

So after we converting 2 times, we will have a fully letter can easily read

### some constrast:

  * Because this is an quiz that the author made, so I can not explain clearly the program
  * I used a lot of generator so it losing ram and slow in speed
  * I wrote this program when I have just learnt python not to far, so I may not have a goo 'style' in coding (comments, using tools, loops, variables name)
