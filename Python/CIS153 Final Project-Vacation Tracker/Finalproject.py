pastvacations=[]
wishlist=[]
import matplotlib.pyplot as plt

def loadpastvacations():
    pastvacations.clear()
    try:
        with open("pastvacations.txt","r")as file:
            for line in file:
                place,year,score,memory=line.strip().split(",")

                vacation={
                    "place":place,
                    "year":year,
                    "score":score,
                    "memory":memory,
                }

                pastvacations.append(vacation)
            print("Your past vacations have been loaded!")
    except FileNotFoundError:
            print("There were no past vacations found, try again!")

def loadwishlist():
    wishlist.clear()
    try:
        with open("wishlist.txt","r")as file:
            for line in file:
                place,priority=line.strip().split(",")

                wish={
                    "place":place,
                    "priority":priority,
                }

                wishlist.append(wish)
            print("Your wish list has been loaded!")
    except FileNotFoundError:
            print("The wish list was not found, try again!")

def savepastvacations():
    with open ("pastvacations.txt","w") as file:
        for v in pastvacations:
            line=v["place"]+","+v["year"]+","+v["score"]+","+v["memory"]
            file.write(line+"\n")
        print("Your past vacations have been saved!")

def savewishlist():
    with open ("wishlist.txt","w")as file:
        for w in wishlist:
            line=w["place"]+","+w["priority"]
            file.write(line+"\n")
        print("Your wish list has been saved!")

def addnewvacation():
    print("\n**Add new vacation**")
    place=input("Place:")
    year=input("Year:")
    score=input("Enjoyment Score (1-10):")
    memory=input("Best Memory:")
    if place=="":
        print("Error: You must enter data to add a vacation!")
        return
    if year=="":
        print("Error: You must enter data to add a vacation!")
        return
    if score=="":
        print("Error: You must enter data to add a vacation!")
        return
    if memory=="":
        print("Error: You must enter data to add a vacation!")
        return
    vacation={
        "place":place,
        "year":year,
        "score":score,
        "memory":memory,
    }

    pastvacations.append(vacation)
    print("Your new vacation has been added!")

def addwish():
    print("\n**Add wish**")
    place=input("Destination:")
    priority=input("How badly do you want to go here? (1-10):")
    if place=="":
        print("Error: You must enter data to add a wish!")
        return
    if priority=="":
        print("Error: You must enter data to add a wish!")
        return
    wish={
        "place":place,
        "priority":priority,
    }

    wishlist.append(wish)
    print("Your new wish has been added!")

def viewpastvacations():
    print("\n***Past Vacations***")
    if not pastvacations:
        print("There are no past vacations, go on vacation!")
        return
    pastvacations.sort(key=lambda v:v["place"])
    for v in pastvacations:
        print("Destination:",v["place"],"/","Year of trip:",v["year"],"/","Enjoyment Score:",v["score"],"/","Best Memory:",v["memory"])
    print()      
              

def viewwishlist():
    print("\n***Wish List***")
    if not wishlist:
          print("The wish list is empty, make a wish!")
          return
    wishlist.sort(key=lambda v:v["place"])
    for w in wishlist:
          print("Destination:",w["place"],"/","Priority Score:",w["priority"])
    print()

def searchpastvacations():
    search=input("Enter a search term:").strip().lower()
    if search=="":
        print("Error: You must enter a search term to search!")
        return
    print("\n**Search Results**")
    found=False
    for v in pastvacations:
        if (search in v["place"].strip().lower() or
            search in v["year"].strip().lower() or
            search in v["score"].strip().lower() or
            search in v["memory"].strip().lower()):
            print("Destination:",v["place"],"/","Year of trip:",v["year"],"/","Enjoyment Score:",v["score"],"/","Best Memory:",v["memory"])
            found=True
    if not found:
        print("No matches were found!")

def searchwishlist():
    search=input("Enter a search term:").strip().lower()
    if search=="":
        print("Error: You must enter a search term to search!")
        return
    print("\n**Search Results**")
    found=False
    for w in wishlist:
        if (search in w["place"].strip().lower()or
            search in w["priority"].strip().lower()):
            print("Destination:",w["place"],"/","Priority Score:",w["priority"])
            found=True
    if not found:
        print("No matches were found!")

def deletepastvacation():
    erase=input("Enter a vacation destination to delete an entry: ").strip().lower()
    for v in pastvacations:
        if v["place"].strip().lower()==erase:
            pastvacations.remove(v)
            print("That vacation has been deleted!")
            return
    print("Entry not found!")

def deletewish():
    erase=input("Enter a wish destination to delete an entry: ").strip().lower()
    for w in wishlist:
        if w["place"].strip().lower()==erase:
            wishlist.remove(w)
            print("That wish has been deleted!")
            return
    print("Entry not found!")

def barchart():
    place=[]
    priority=[]

    for w in wishlist:
        place.append(w["place"])
        priority.append(int(w["priority"]))
        
    plt.figure(figsize=(10,5))
    plt.bar(place,priority,color="blue",edgecolor="yellow")
    plt.title("Wish List Priority Score",fontsize=20,fontweight="bold",color="darkblue",family="monospace")
    plt.xlabel("Destination Name",fontsize=14,color="darkblue")
    plt.ylabel("Priority Score (1-10)",fontsize=14,color="darkblue")
    plt.xticks(color="darkblue")
    plt.yticks(color="darkblue")
    plt.show()

def piechart():
    yearcount={}
    for v in pastvacations:
        year=v["year"]
        if year in yearcount:
            yearcount[year]=yearcount[year]+1
        else:
            yearcount[year]=1

    years=[]
    counts=[]

    for year in yearcount:
        years.append(year)
        counts.append(yearcount[year])
        
    plt.figure(figsize=(8, 6))
    plt.pie(counts,labels=years,colors=["cyan","turquoise","pink","violet"],autopct="%1.1f%%",startangle=90,textprops={"fontweight":"bold","color":"purple"})
    plt.title("Trips Per Year",fontsize=20,color="magenta",fontweight="bold")
    plt.show()

def lineplot():
    years=[]
    scores=[]

    for v in pastvacations:
        years.append(int(v["year"]))
        scores.append(int(v["score"]))

    plt.figure(figsize=(10,5))
    plt.plot(years,scores,marker="o",color="lightgreen")
    plt.title("Enjoyment Score Over Time",fontweight="bold",fontsize=20,family="serif",color="darkgreen")
    plt.xlabel("Year",color="green",fontweight="bold")
    plt.ylabel("Enjoyment Score (1-10)",color="green",fontweight="bold")
    plt.xticks(range(2013,2026),color="green")
    plt.yticks(color="green")
    plt.ylim(0,11)
    plt.grid(True)
    plt.show()

def menu():
    loadpastvacations()
    loadwishlist()

    while True:
        print("\n***********Vacation Tracker Menu***********")
        print("1. View past vacations")
        print("2. Add a new vacation")
        print("3. Search past vacations")
        print("4. Delete a past vacation")
        print("5. View wish list")
        print("6. Add a new wish")
        print("7. Search wish list")
        print("8. Delete a wish")
        print("9. Save all data")
        print("10. View bar chart")
        print("11. View pie chart")
        print("12. View line plot")
        print("13. Quit")
        choice=input("Choose an option: ")

        if choice=="1":
            viewpastvacations()
        elif choice=="2":
            addnewvacation()
        elif choice=="3":
            searchpastvacations()
        elif choice=="4":
            deletepastvacation()
        elif choice=="5":
            viewwishlist()
        elif choice=="6":
            addwish()
        elif choice=="7":
            searchwishlist()
        elif choice=="8":
            deletewish()
        elif choice=="9":
            savepastvacations()
            savewishlist()
        elif choice=="10":
            barchart()
        elif choice=="11":
            piechart()
        elif choice=="12":
            lineplot()
        elif choice=="13":
            print("Thanks for visiting, goodbye!")
            break
        else:
            print("Not a valid choice, try again!")
menu()

            
                
