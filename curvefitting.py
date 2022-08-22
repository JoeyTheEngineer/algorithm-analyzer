# sandbox bs
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from scipy import stats

# #polynumial
# # create DataFrame
# df = pd.DataFrame({'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
#                    'y': [3, 14, 23, 25, 23, 15, 9, 5, 9, 13, 17, 24, 32, 36, 46]})

# polyline = np.linspace(1, 15, 50)
# model1 = np.poly1d(np.polyfit(df.x, df.y, 1))
# model2 = np.poly1d(np.polyfit(df.x, df.y, 2))
# model3 = np.poly1d(np.polyfit(df.x, df.y, 3))

# print(model3)
# plt.scatter(df.x, df.y)

# #add fitted polynomial lines to scatterplot 
# plt.plot(polyline, model1(polyline), color='green')
# plt.plot(polyline, model2(polyline), color='red')
# plt.plot(polyline, model3(polyline), color='purple')

#logarithmic
#create DataFrame
#y=xlog(x)
x=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
y=x*np.log(x)
df = pd.DataFrame({
    'x': [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
    'y': y
})
df.y=df.y/df.x
df.x=np.log(df.x)
polyline = np.linspace(0, 5, 50)

model4 =  np.poly1d(np.polyfit(df.x, df.y, 1))
slope, intercept, r, p, std_err = stats.linregress(df.x, df.y)
print(r)

plt.plot(polyline, model4(polyline), color='purple')
plt.scatter(df.x, df.y)
plt.show()
# model4 = np.polyfit(df.x, df.y, 1)

# model4 = np.poly1d(np.polyfit(df.x, df.y, 2))


# plt.scatter(df.x, df.y)
# print(model4)



# plt.show()