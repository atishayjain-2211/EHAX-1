#IN MEMORY DATABS


database = {}

while True:

    command = input(">")
    parts = command.split()
    print(parts)

    if not parts:
        continue

    if parts[0] =="EXIT":
        break

    if parts[0] == "SET":
        if len(parts) != 3:
            print("Enter key and value")
        else:
            database[parts[1]] = parts[2]
            print("OK")

    elif parts[0] == "GET":
        if len(parts) != 2:
            print("Enter key")
        elif parts[1] in database:
            print(database[parts[1]])
        else:
            print("Key not found")

    elif parts[0] == "DEL":
        if len(parts) != 2:
            print("Enter key")
        elif parts[1] in database:
            del database[parts[1]]
            print("OK")
        else:
            print("Key not found")

    elif parts[0] == "EXISTS":
        if len(parts) != 2:
            print("Enter key")
        elif parts[1] in database:
            print("1")
        else:
            print("0")

    elif parts[0] == "SAVE":
        if len(parts) != 2:
            print("Enter filename")
        else:
            filename = parts[1]
            with open(filename, "w") as f:
                for key,value in database.items():
                    f.write(key + "=" + value +"\n")
            print("Saved successfully")

    elif parts[0] == "LOAD":
        if len(parts) != 2:
            print("Enter filename")
        else:
            filename = parts[1]

            try:
                with open(filename,"r") as f:
                    database.clear()
                    for line in f:
                        key, value = line.strip().split("=")
                        database[key] = value
                print("Loaded successfully")
            except FileNotFoundError:
                print("File not found")

    else:
        print("Unknown command")