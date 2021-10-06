import pywhatkit

file = open("stocks.txt", 'r')
txt = ""

for line in file:
    txt = txt + line

pywhatkit.text_to_handwriting(txt, rgb=(0, 0, 255))
