if __name__ == '__main__':
    filetoWrite = open("data.csv","w")
    with open('modified.txt') as fileobject:
        for line in fileobject:
            lineArray = line.split(" ")
            lineArray = list(filter(None, lineArray))
            filetoWrite.write(",".join(lineArray)) 