import datetime
import time


def mainPage():
    while True:
        print("""============ Crowd-Funding Main Page =========== 
            1) create raise campaign
            2) view all campaigns
            3) edit Your projects
            4) delete his own projects
            5) search for a project using date""")
        choice = MainInputValidation()
        if (choice == 1):
            createProject()
        elif (choice == 2):
            listALL()
        elif (choice == 3):
            editProject()
        elif (choice == 4):
            deleteProject()
        elif (choice == 5):
            search_by_Date()
        elif (choice == 'done'):
            break


def MainInputValidation():
    x = input("Enter Your Choice: ")
    if (x.isdigit() and int(x) in range(1, 5)):
        return int(x)
    return MainInputValidation()


def projectName():
    x = input("Project Name: ")
    if (x.isalpha()):
        return x
    else:
        return projectName()


def projectDeatils():
    x = input("project details: ")
    return x


def totalTarget():
    x = input("Totaltarget: ")
    if (x.isdigit() and x != 0):
        return x
    else:
        return totalTarget()


def enterdate():
    inputDate = input("Enter the date in format 'dd/mm/yy' : ")
    day, month, year = inputDate.split('/')
    isValidDate = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        isValidDate = False

    if (isValidDate):
        return inputDate
    else:
        return enterdate()


def inputProject():
    Title = projectName()
    Details = projectDeatils()
    Totaltarget = totalTarget()
    startDate = enterdate()
    endDate = enterdate()
    project_id = round(time.time())
    data = f"{project_id}:{Title}:{Details}:{Totaltarget}:{startDate}:{endDate}\n"
    return data


def createProject():
    data = inputProject()
    file = open("projects.txt", 'a')
    file.writelines(data)
    file.close()


def listALL():
    file = open("projects.txt", 'r')
    data = file.readlines()
    print(f"our campaigns :{data}")


def editProject():
    name = input("enter your project name: ")
    file = open("projects.txt", 'r')
    data = file.readlines()
    file.close()
    index = 0
    for i in data:
        d = i.split(":")
        if (d[1] == name ):
            data[index] = inputProject()

        index += 1
    file = open("projects.txt", 'w')
    file.writelines(data)
    file.close()


def deleteProject():
    name = input("enter your project name: ")
    file = open("projects.txt", 'r')
    data = file.readlines()
    file.close()
    index = 0
    for i in data:
        d = i.split(":")
        if (d[1] == name):
            del data[index]
        index += 1
    file = open("projects.txt", 'w')
    file.writelines(data)
    file.close()


def search_by_Date():
    date = input("Enter the start date in format 'dd/mm/yy' : ")
    file = open("projects.txt", 'r')
    data = file.readlines()
    file.close()
    
    for i in data:
        d = i.split(":")
        print("enter start time for the campaign")
        if (date == d[4]):
            print(f"campaign Title is :{d[1]} \n campaign Details is :{d[2]} \n Total target : {d[3]}")

mainPage()