fname = input('Enter file: ')
if len(fname) <1 : fname = "clown.txt"

fhand = open(fname)

many = dict ()

for line in fhand :
    line = line.rstrip()
    wds = line.split ()
    
    for w in wds:
        many [w] = many.get(w, 0) + 1
            
# Find the top 5 word by frequency

newList = list()
for k,v in many.items() :
    tup = (v,k)
    newList.append(tup)
cool = sorted(newList,reverse=True)

for v,k in cool[:5]:
    print(k,v)