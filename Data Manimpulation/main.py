while True:

    addViewData = input("Would you like to ADD or VIEW a File: ")
    viewInformation = None
    anotherQuestion = None

    def whenExit():
        ex = input("Would you like to exit this program now? Y = Yes, N = No: ")
        if ex == "Y":
            exit()

    if addViewData == "add":
        fileName = input("What would you like file to be named as: ")
        f = open(fileName, "a")
        info = input("Enter the info for the record: ")
        f.write(info)
        f.close()
        anotherQuestion = input("Would you like to view the information. Y for YES, N for NO: ")
        whenExit()

    if anotherQuestion == "Y":
        f = open(fileName, "r")
        print(f.read())
            
    if addViewData == "view":
        whatRecord = input("What record would you like to view: ")
        f = open(whatRecord, "r")
        print(f.read())
        whenExit()