largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        inum = int(num)
    except:
        print("Invalid input")
        continue

    print(num)

    # atualização simples de maior e menor
    if largest is None or inum > largest:
        largest = inum
    if smallest is None or inum < smallest:
        smallest = inum

print("Maximum", largest)
print("Minimum", smallest)

#codigo mais direto sem precisar do elif e só com 2 if e 2 is none or