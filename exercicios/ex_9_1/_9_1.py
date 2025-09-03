fname = input("Enter file: ")
if len(fname) < 1 : fname = "clown.txt"

fhand = open(fname)

many = dict()

for line in fhand:
	line = line.rstrip()
	wds=line.split()
	# print(wds)
	
	for w in wds:
		#print("===>",w)
		
		#oldvalue = 0
		#if w in many : oldvalue = many[w]
		#oldvalue = many.get(w,0)
		#many[w] = oldvalue + 1

		many[w] = many.get(w,0) + 1

		#print("after",many)

print(many)

# FIND THE EORD WITH THE LARGEST COUNT

x = None
y = None
for cle, valeur in many.items() :
	print(cle,valeur)
	if x is None or valeur>x: 
		x = valeur
		y = cle

print(x,y)		