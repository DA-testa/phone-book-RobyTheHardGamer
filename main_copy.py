n = int(input()) ##ievadītās vērtības kā n Integer tipa
phonebook = {} ##definēta tukša direktorija

for i in range(n):
    query = input().split()

    if query[0] == "add":
        phonebook[query[1]] = query[2]
    elif query[0] == "del":
        if query[1] in phonebook:
            del phonebook[query[1]]

    elif query[0] == "find":
        if query[1] in phonebook:
            print(phonebook[query[1]])
        else:
            print("not found")