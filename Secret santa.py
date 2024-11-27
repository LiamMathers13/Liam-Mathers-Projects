import random
def getNames():
    names = []
    while True:
        Temp = input("What name would you like to add, OR type N to stop entering names: ")
        if Temp.upper() == "N":
            break
        names.append(Temp)
    return names
def choosePairings(names):
    newNames = names.copy()
    pairings = {}
    for elem in names:
        length = len(newNames) - 1
        index = random.randint(0, length)
        while elem == newNames[index]:
            index = random.randint(0, length)
        pairings[elem] = newNames[index]
        newNames.pop(index)
    return pairings
def showPairings(elves):
    while True:
        temp = input("Who's wondering who they are giving a gift to? Or type N to exit: ").strip()
        if temp.upper() == "N":
            break
        if temp not in elves:
            print(f"{temp} is not included in the secret santa, please try again.")
        else:
            print(f"{temp} is giving a gift to {elves[temp]}.")
def main():
    names = getNames()
    if len(names) < 2:
        print("You need at least two names to create pairings.")
        return
    pairings = choosePairings(names)
    showPairings(pairings)
main()
