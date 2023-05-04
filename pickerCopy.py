# import section - remember to add to Mu/IDE
import random

def remove_items(lst, choice):
    newlst= []

    for x in lst:
        if x != choice:
            newlst.append(x)

    return newlst


def percentages(lst):
    newlst = []
    for x in lst:
        split = x.split(" ")
#         print(split)
        for y in range(round(float(split[1]))):
            newlst.append(split[0])

    return newlst


def randomChoice(lst, lens):
    choiceNum = 20000
    while (choiceNum > lens + 1):
        choiceNum = int(input("You can pick up to " + str(lens) + " options. how many options would you like to pick from?"))

    for x in range(int(choiceNum)):
        item = random.choice(lst)
        print(str(x+1) + ": " + item.split(" ")[0])
        lst = remove_items(lst, item)


def cleanLists(lst, members):
    newlst = []
    for x in lst:
        dontAdd= False

        splits = x.replace("\t", " ").split(" ")
        name = splits[0]
        splits.remove(name)

        #averaging score:
        num = 0
        for y in range(len(members)):
            if ((splits[y] == '0') and members[y] == True):
                dontAdd = True
            if (members[y]== True):
                num += float(splits[y])
        string = name + " " + str(num)
        if not (dontAdd):
            newlst.append(string)

#     print(newlst)
    return newlst



def whoisHere():
    Amanda = input("is Amanda present? [Y] or [N]").upper()
    Tyler = input("is Tyler present? [Y] or [N]").upper()
    Andrew = input("is Andrew present? [Y] or [N]").upper()
    Sam = input("is Sam present? [Y] or [N]").upper()



    #Inputs to determine who is present
    while (Amanda != "Y" and Amanda != "N"):
        Amanda = input("is Amanda present? [Y] or [N]").upper()
    while (Tyler !="Y" and Tyler != "N"):
        Tyler = input("is Tyler present? [Y] or [N]").upper()
    while (Andrew !="Y" and Andrew != "N"):
        Andrew = input("is Andrew present? [Y] or [N]").upper()
    while (Sam !="Y" and Sam != "N"):
        Sam = input("is Sam present? [Y] or [N]").upper()

    members = [Amanda, Tyler, Andrew, Sam]

    #true/false
    present = []
    for x in members:
        if x == 'Y':
            present.append(True)
        else:
            present.append(False)
    return present




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
    members = whoisHere()
    lst = cleanLists(lst, members)

    #fixing percentages
    lstnums = len(lst)
    lst = percentages(lst)


    #final random choice
    randomChoice(lst,lstnums)



if __name__ == "__main__":
    main()
# Write your code here :-)
