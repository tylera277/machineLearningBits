
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
plt.xlim(-10, 10)
plt.ylim(-10, 10)

# this is the
x1 = 5 + np.random.randn(50)
y1 = 5 + np.random.randn(50)

list1 = np.zeros((len(x1), 2))
for j in range(len(x1)):
    list1[j][0] = x1[j]
for k in range(len(y1)):
    list1[k][1] = y1[k]

x2 = np.random.normal(scale=1, size=50) - 2
y2 = np.random.normal(scale=1, size=50) - 2
list2 = np.zeros((len(x2), 2))
for j in range(len(x2)):
    list2[j][0] = x2[j]
for k in range(len(y2)):
    list2[k][1] = y2[k]

x3 = np.random.normal(scale=2, size=50) -4
y3 = np.random.normal(scale=2, size=50) + 5
list3 = np.zeros((len(x3), 2))
for j in range(len(x3)):
    list3[j][0] = x3[j]
for k in range(len(y3)):
    list3[k][1] = y3[k]

pos = np.concatenate((list1, list2, list3))

# pos = [[9, 5], [0, 0], [-2, 0], [9, 6], [-3, 0], [0, 1],
# [-9, -6], [-7, -5], [-9, -9]]
mean = [[10, 0], [0, 0], [-3, -3]]

cluster1 = []
cluster2 = []
cluster3 = []
xU, yU = [[0,0],[0,0]]

ln0 = plt.plot(xU, yU)
ln1 = plt.plot(xU, yU)
ln2 = plt.plot(xU, yU)
plot = plt.scatter(0, 0, s=10, c='red')

for i in range(len(pos)):
    plt.scatter(pos[i][0], pos[i][1], s=10, c='blue')



# +the main part of the program that is trying to
# implement the k-means clustering algorithm
# + Right now I have it only working for a k value
# of three, so it is rather fixed at the moment.
# + It seems if you fiddle with the while loop change
# condition, it can be made more accurate in getting
# towards the center of the clusters

totalChange1 = totalChange2 = totalChange3 = 10
while (totalChange1 and totalChange2 and totalChange3) > 0.01:
#while True:

    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    for i in range(len(pos)):
        plt.scatter(pos[i][0], pos[i][1], s=10, c='blue')

    for j in range(len(mean)):
        plot = plt.scatter(mean[j][0], mean[j][1], s=10, c='red')
    plt.pause(3)
    for i in cluster1:
        xN, yN = [mean[0][0], pos[i][0]], [mean[0][1], pos[i][1]]
        ln0 = plt.plot(xN, yN, marker='o')
    for j in cluster2:
        xN, yN = [mean[1][0], pos[j][0]], [mean[1][1], pos[j][1]]
        ln1 = plt.plot(xN, yN, marker='o')
    for k in cluster3:
        xN, yN = [mean[2][0], pos[k][0]], [mean[2][1], pos[k][1]]
        ln2 = plt.plot(xN, yN, marker='o')
    plt.pause(20)


    plt.clf()

    #print(mean)
    cluster1 = []
    cluster2 = []
    cluster3 = []
    xSum1 = 0
    ySum1 = 0
    xSum2 = 0
    ySum2 = 0
    xSum3 = 0
    ySum3 = 0
    for i in range(len(pos)):
        dist1 = (pos[i][0]-mean[0][0])**2 + (pos[i][1]-mean[0][1])**2
        dist2 = (pos[i][0]-mean[1][0])**2 + (pos[i][1]-mean[1][1])**2
        dist3 = (pos[i][0]-mean[2][0])**2 + (pos[i][1]-mean[2][1])**2

        #print(dist1, dist2, dist3)

        # +this puts the data points into their closest
        # cluster mean
        if dist1 < (dist3 and dist2):
            cluster1.append(i)
        elif dist2 < (dist1 and dist3):
            cluster2.append(i)
        elif dist3 < (dist2 and dist1):
            cluster3.append(i)
    print(cluster1, cluster2, cluster3)

    for j in cluster1:
        xSum1 += pos[j][0]
        ySum1 += pos[j][1]
    length1 = len(cluster1)
    try:
        changeX1 = (xSum1/length1) - mean[0][0]
    except ZeroDivisionError:
        changeX1 = 0

    try:
        changeY1 = (ySum1/length1) - mean[0][1]
    except ZeroDivisionError:
        changeY1 = 0
    totalChange1 = (changeX1**2 + changeY1**2)**(1/2)

    try:
        div1 = xSum1/length1
    except ZeroDivisionError:
        div1 = 0
    try:
        div2 = ySum1/length1
    except ZeroDivisionError:
        div2 = 0
    mean[0] = [div1, ySum1/length1]

    for k in cluster2:
        xSum2 += pos[k][0]
        ySum2 += pos[k][1]
    length2 = len(cluster2)
    try:
        changeX2 = (xSum2/length2) - mean[1][0]
    except ZeroDivisionError:
        changeX2 = 0
    try:
        changeY2 = (ySum2/length2) - mean[1][1]
    except ZeroDivisionError:
        changeY2 = 0
    totalChange2 = (changeX2**2 + changeY2**2)**(1/2)
    try:
        div1 = xSum2/length2
    except ZeroDivisionError:
        div1 = 0
    try:
        div2=ySum2/length2
    except ZeroDivisionError:
        div2=0
    mean[1] = [div1, div2]

    for h in cluster3:
        xSum3 += pos[h][0]
        ySum3 += pos[h][1]
    length3 = len(cluster3)
    try:
        changeX3 = abs((xSum3/length3+0.01) - mean[2][0])
    except ZeroDivisionError:
        changeX3 = 0
    try:
        changeY3 = abs((ySum3/length3) - mean[2][1])
    except:
        changeY3 = 0
    totalChange3 = (changeX3**2 + changeY3**2)**(1/2)
    try:
        div1 = xSum3/length3
        div2 = ySum3/length3
    except ZeroDivisionError:
        div1 = 0
        div2 = 0
    mean[2] = [div1, div2]




