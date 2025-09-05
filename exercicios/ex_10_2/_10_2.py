name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

horas = list()
for line in handle:
    line = line.strip()
    if line.startswith("From "):
        words = line.split()
        if len(words) > 6:
            hora = words[5].split(":")
            h = hora[0]
            horas.append(h)

dicionario = dict()
for w in horas:
    dicionario[w] = dicionario.get(w,0)+1
for hora in sorted(dicionario):
    print(hora,dicionario[hora])
#10.2 Write a program to read through the mbox-short.txt and 
#figure out the distribution by hour of the day 
#for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and 
#then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.