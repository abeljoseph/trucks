import pandas as pd 
import matplotlib.pyplot as plt

data1 = pd.read_csv("1084067241.csv", delimiter="\t")
data2 = pd.read_csv("1084068051.csv", delimiter="\t")
data3 = pd.read_csv("1084068100.csv", delimiter="\t")
data4 = pd.read_csv("1084068111.csv", delimiter="\t")
data5 = pd.read_csv("1088214007.csv", delimiter="\t")
data6 = pd.read_csv("1088214013.csv", delimiter="\t")
data7 = pd.read_csv("1088214034.csv", delimiter="\t")
data8 = pd.read_csv("1088214042.csv", delimiter="\t")
data9 = pd.read_csv("1088214236.csv", delimiter="\t")
data10 = pd.read_csv("1088217018.csv", delimiter="\t")
data11 = pd.read_csv("1088217019.csv", delimiter="\t")


plt.scatter(data1['Latitude'], data1['Longitude'])
plt.show()
plt.scatter(data2['Latitude'], data2['Longitude'])
plt.show()
plt.scatter(data3['Latitude'], data3['Longitude'])
plt.show()
plt.scatter(data4['Latitude'], data4['Longitude'])
plt.show()
plt.scatter(data5['Latitude'], data5['Longitude'])
plt.show()
plt.scatter(data6['Latitude'], data6['Longitude'])
plt.show()
plt.scatter(data7['Latitude'], data7['Longitude'])
plt.show()
plt.scatter(data8['Latitude'], data8['Longitude'])
plt.show()
plt.scatter(data9['Latitude'], data9['Longitude'])
plt.show()
plt.scatter(data10['Latitude'], data10['Longitude'])
plt.show()
plt.scatter(data11['Latitude'], data11['Longitude'])
plt.show()

