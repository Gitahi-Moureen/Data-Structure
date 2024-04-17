from collections import deque
a = deque()
print(type(a))

a.append(1)
a.append(2)
a.append(4)
a.append(6)
a.append(8)
a.append(7)
a.append(6)

#Removes first elemet
print(a.popleft())
print(a.popleft())
print(a.popleft())

print("Initial queue")
print(a)