from cv2 import cv2
import random
import PIL
import matplotlib.pyplot as plt
import numpy as np

def naturals(n):
    yield n
    yield from naturals(n+1)


def prime(n):
    res = next(n)
    yield res
    yield from prime(i for i in n if i % res != 0)

def count(x):
    res = [x]
    steps = 1
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = x * 3 + 1
        res.append(x)
        steps = steps + 1
    return res, steps
plot = plt.figure(1)
plt.xlabel('Steps')
plt.ylabel('Path')
plt.title('3N + 1 function behivior on prime numbers')
steps = 0
p = prime(naturals(2))
for i in range(50):
    y, steps = count(next(p))
    x = [i for i in range(steps)]
    plt.plot(x, y)
    #print(x)
plt.show()

col, row = 1920, 1080
data = np.zeros((row, col, 3), dtype=np.uint8)

for i in range(0, row):
    for j in range(0, col):
        data[i][j] = [int(i), int(j), int(i+j)]

#data[0:256, 0:256] = [10, 0, 255] # red patch in upper left
img = PIL.Image.fromarray(data, 'RGB')
img.save('C:/Users/Yunix/Desktop/Rafael.png')
img.show()

#plt.show()
#cv2.imshow('Frame', frame)
#print(rect)
#cap.release()
#cv2.waitKey(0)
#
#cv2.destroyAllWindows()