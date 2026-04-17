#Comparisons of vacation destinations and their safety rating.
destination= []
safety= []
with open('vacation.txt', 'r') as file:
    for line in file:
        place,sscore= line.strip().split(',')
        destination.append(place)
        safety.append(int(sscore))
#Bar Chart
import matplotlib.pyplot as plt
plt.figure(figsize=(15,6))
plt.bar(destination,safety, color='violet')
plt.title('Vacation Destinations')
plt.xlabel('Country Name')
plt.ylabel('Safety Score')
plt.show()
#Pie Chart
plt.figure(figsize=(8, 6))
plt.pie(safety,labels=destination,startangle=90)
plt.title('Vacation Destinations')
plt.show()

#Short Explanation:
#Where you found the project or tutorial (include a link if possible):
#I used the 'Intro to Data Visualization' assignment in the Canvas modules to guide my mini project.

#Why you picked it (how it connects to your final project idea):
#I picked this assignment because I tried to use Real Python to find a tutorial and I could not do one completely for free.
#Rather than searching the Internet and running into the same issue everywhere else, I dedcided to just stick with what I knew I could do for free.
#This connects to my final idea because I will use maplotlib to visualize data in my final project so it was good to play around with it.

#What you learned or found challenging:
#I learned how to visualize data and create labels and adjust sizing on the graphs.

#What you want to try next when building your final project:
#For my final project I will continue to use different colors, sizes, and compare more thn two things.

