def countWord():
    file=input("Enter the file path/name: ")
    counter = 0
    data = open(file,'r')

    for lines in data:
        words = lines.split()
        counter = counter+len(words)

    print("Number of words = ")
    print(counter)

countWord()



