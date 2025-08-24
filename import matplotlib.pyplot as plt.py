import matplotlib.pyplot as plt

x = ['mon' , 'tues' , 'wed' , 'thur' , 'fri'] 
y = [18,15,7,20,12]

plt.plot(x,y)
plt.title('Bakery Sales this Week')
plt.xlabel('Day of the week')
plt.ylabel('Sales per day')

# plt.show()

Months = [1,2,3,4]
Sales = [1000, 1500 , 1200 , 1800]

plt.plot(Months , Sales , color='blue' , linestyle= '--', linewidth= 2 , marker = 'o', label = '2025 sales data')
plt.xlabel('months')
plt.ylabel('sales')
plt.title('Monthly sales data report')
plt.legend(loc = 'upper left', fontsize=12)
plt.grid(color ='gray' , linestyle = ':' , linewidth= 1)
plt.xlim(1,4)
plt.ylim(0, 2000)
plt.xticks([1,2,3,4], ['M1','M2','M3', 'M4'])
plt.show()

# # Bar chart

product = ['A', 'B', 'C' , 'D']
sales = [1000, 1500 , 800 , 1200]

plt.bar(product, sales ,  color = 'orange' , label = 'sales 2025')
plt.xlabel('Product')
plt.ylabel('sales')
plt.title('Product sales comparision')
plt.legend()
plt.show()

#Pie Chart 

Region = ['North' , 'South', 'East', 'West']
Revenue = [3000 , 2000, 1500 , 1000]

plt.pie(Revenue , labels=Region , autopct='%1.1f%%', colors= ('gold', 'skyblue', 'lightgreen' , 'coral') )
plt.title('Revenue Contribution by region')
plt.show()

#Hist.

scores = [45,67,89,56,78,88,92,60,74,81,59,66,75,82,90,85,70,73,68,77]
plt.hist(scores, bins=5 , color='purple' ,edgecolor='black')
plt.xlabel('Score range')
plt.ylabel('Number of students')
plt.title('Score Distribution')
plt.show()


#Scatter plots

Hours_studies = [1,2,3,4,5,6,7,8]
exam_scores = [50 , 55,60,65,70,75,80,85]

plt.scatter(Hours_studies , exam_scores , color='green' , marker='o' , label= 'student data')
plt.xlabel('Hours studies')
plt.ylabel('Exam scores')
plt.title('Relationship between study time and exam score')
plt.legend()
plt.grid(True)
plt.show()

x= [1,2,3,4]
y = [10,20,30,40]

plt.subplot(1,2,1)
plt.plot(x,y)

plt.subplot(1,2,2)
plt.bar(x,y)
plt.title('Bar chart')

plt.tight_layout()
plt.show()