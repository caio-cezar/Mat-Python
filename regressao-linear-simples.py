import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,2,3])
y = np.array([1,1,4])

p1 = np.polyfit(x,y,1)  

yfit = p1[0] * x + p1[1]
yresid = y - yfit
SQresid = sum(pow(yresid,2))
SQTotal = len(y) * np.var(y)
R2 = 1 - SQresid/SQTotal

print(p1)
print(R2)

plt.plot(x,y,'o')
plt.plot(x, np.polyval(p1,x),'r--')
plt.xlabel('x')
plt.ylabel('y')
plt.show()