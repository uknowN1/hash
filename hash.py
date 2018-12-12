word = ""
pord = ""
key = 0
letters = []
petters = []
crypt = []
meny = 0

print("***Välkommen till krypteringsprogramet***")
print("1. Kryptera")
print("2. Dekryptera")
print("3. Avsluta")

while meny != 3:

    try:
        meny = int(input("Gör ett val: "))
    except:
        print("Du måste göra ett korekt val")

    if meny == 1:
        key = (int(input("Välj en nyckel: ")))
        word = input("Skriv in de ord du vill kryptera: ")
        for letter in word:
            letters.append(ord(letter) + key)
        print(letters)
    elif meny == 2:
        for l in letters:
            crypt.append(chr(l -key))
        print(crypt)            
    else:
        print("")