# import section - remember to add to Mu/IDE
import random

def remove_items(lst, choice):
    res = [i for i in lst if i != choice]
    return res


def randomChoice(lst):
    choiceNum = int(input("how many options would you like to pick from?"))

    # randomly select three restaurant options
    options = random.sample(lst, choiceNum)

    for i, option in enumerate(options):
        split = option.split(" ")
        print(f"{i+1}. {split[0]}")
        lst = remove_items(lst, option)
        lst = remove_items(lst, option)




def whoisHere(lst):
    Amanda = ""
    Tyler = ""
    Andrew = ""
    Sam = ""
    newlst = []


    #Inputs to determine who is present
    while (Amanda != "Y" and Amanda != "N"):
        Amanda = input("is Amanda present? [Y] or [N]").upper()
    while (Tyler !="Y" and Tyler != "N"):
        Tyler = input("is Tyler present? [Y] or [N]").upper()
    while (Andrew !="Y" and Andrew != "N"):
        Andrew = input("is Andrew present? [Y] or [N]").upper()
    while (Sam !="Y" and Sam != "N"):
        Sam = input("is Sam present? [Y] or [N]").upper()


    #uses values to determine numofpeople / eliminates options at a '0'
    for x in lst:

        numofPeople = 0

        if (Amanda == 'N'):
            amandaChoice = 0
        else:
            numofPeople += 1;

        if (Tyler == 'N'):
            tylerChoice = 0
        else:
            numofPeople += 1;

        if (Andrew =='N'):
            andrewChoice = 0
        else:
            numofPeople += 1;

        if (Sam == 'N'):
            samChoice = 0
        else:
            numofPeople += 1;


        #eliminating items
        splits = (x.split())
        amandaChoice = float(splits[1])
        tylerChoice = float(splits[2])
        andrewChoice = float(splits[3])
        samChoice = float(splits[4])
        if (Amanda == 'Y' and amandaChoice < 2) or (Tyler == 'Y' and tylerChoice <2) or (Andrew == 'Y' and andrewChoice <2) or (Sam == 'Y' and samChoice <2):
            lst.remove(x)

        #new list for new probabilities
        finalNum = round((amandaChoice + tylerChoice + andrewChoice + samChoice)/numofPeople)
        for z in range(finalNum):
            newlst.append(x)

 #   print(newlst)
    return newlst


def inputSets(foodDict):
    choice = ""
    lst = []

    for x in foodDict.keys():
        while choice != "Y" and choice != "N":
            choice = input("Please type [Y] or [N] to include " + x + "\n")
            choice = choice.upper()
        if choice == "Y":
            for y in foodDict[x]:
                lst.append(y)
            choice = ""
        elif choice == "N":
            choice = ""
    return lst


def sort_options(contents):
    # dictionary section
    foodDict = {}
    curType = ""
    foodPool = []

    # cleaning up blanks
    while "" in contents:
        contents.remove("")
    for x in contents:
        if x[0] == "*":
            curType = x[1:]
            lst = []
            foodDict[curType] = None
        else:
            lst.append(x)
        foodDict[curType] = lst
    return foodDict


def main():
    # opening files
    f = open("choices.txt", "r")
    content = f.read()

    # creating and cleaning list
    contents = content.split("\n")
    foodDict = sort_options(contents)
    f.close()

    # final list of chosen options
    lst = inputSets(foodDict)

    # updating based on people present
    lst = whoisHere(lst)

    #final random choice
    randomChoice(lst)



if __name__ == "__main__":
    main()
