import numpy as np

# Question_2
#loads lab2-data.txt
data = np.loadtxt("lab2-data.txt")

#array - Data Preprocessing
all_x = data[:, 0] #frist axis is 0
all_y = data[:, 1] #seacond axis 1

#gets the average
x_ = np.average(all_x)
y_ = np.average(all_y)

#sum of averages / sum of average ^2
#Xi all_x and x_  is the anoter x same for y
b1 = np.sum((all_x - x_) * (all_y - y_))/np.sum((all_x - x_)**2)
print("\nb1 =", b1)

b0 = y_ - b1*x_
print("\nb0 =", b0)

#prints b0 answer

y_pred = b0 + b1*all_x

SS_tot = np.sum((all_y - y_)**2)
SS_res = np.sum((all_y - y_pred)**2)

R2 = 1 - SS_res/SS_tot
print("\nR^2 =", R2)
#prints r2 answer