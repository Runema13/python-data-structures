fh = open("mbox-short.txt")

for line in fh:
    line = line.rstrip()
    sx = line.split()
    #guardião em uma frase composta, a ordem importa, ser for veradeiro o primeiro
    #nem vai para o segund oque tem risco de dar traceback
    if len(sx) < 3 or sx[0] != "From":
        continue
    print(sx[2])