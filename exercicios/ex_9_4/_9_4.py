name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

lista = list()
for line in handle:
    line = line.strip()
    if line.startswith("From "):
        line = line.split()
        lista.append(line[1])
        
counts = {}
for name in lista:
    counts[name] = counts.get(name,0)+1

wv = None
wk = None
for name,value in counts.items():
    if wv is None or value > wv:
        wv = value
        wk = name
print(wk,wv)

#9.4 Write a program to read through the mbox-short.txt and 
# figure out who has sent the greatest number of mail messages. 
#The program looks for 'From ' lines and 
# takes the second word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address to a
# count of the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary using a
# maximum loop to find the most prolific committer.