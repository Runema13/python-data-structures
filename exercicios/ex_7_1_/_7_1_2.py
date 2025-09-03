fh = open("mbox-short.txt")

for li in fh:
    ly = li.strip()
    print(ly.upper())