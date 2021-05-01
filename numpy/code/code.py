import numpy as np

a_1 = np.zeros(10)
a_1[4] = 1
print(a_1)

a_2 = np.arange(10,50)
print(a_2)

a_3 = a_2[::-1]
print(a_3)

a_4 = np.random.random((10,10))
print(a_4.max())
print(a_4.min())

a_5 = np.zeros((10,10))
a_5[[0,-1],:] = 1
a_5[:,[0,-1]] = 1
print(a_5)

a_6 = np.random.randint(0,5,(5,5))
print(a_6)

a_7 = np.linspace(0,1,12)
print(a_7)

a_8 = np.random.random((10))
print(np.sort(a_8))

a_9 = np.random.random((10,2))
Max = np.where(a_9 == a_9.max())
a_9[Max] = 0
print(a_9)

a_10 = np.random.randint(1,101,(5,5))
a_10 = a_10[np.argsort(a_10[:,2])]
print(a_10)

a_11_1 = np.arange(1,6)
a_11_2 = np.zeros(17)
a_11_2[::4] = a_11_1
print(a_11_2)

a_12 = np.arange(4).reshape(2,2)
print(a_12[[1,0]])

a_13_1 = np.random.randint(1,10,(5,3))
a_13_2 = np.random.randint(1,10,(3,2))
print(np.dot(a_13_1,a_13_2))

a_14_1 = np.arange(4).reshape(2,2)
a_14_2 = np.mean(a_14_1,axis=1).reshape(2,1)
print(a_14_1-a_14_2)

a_15 = np.random.randint(1,10,(5,5))
Min = a_15.min()
Max = a_15.max()
print((a_15-Min)/(Max-Min))

a_16 = np.random.randint(1,10,(10,10))
Min = a_16.min()
Max = a_16.max()
print((a_16-Min)/(Max-Min))
