l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l.remove(5)
print(l)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l.remove(5))

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l.insert(5, 6)
print(l)

l = {1, 2, 3, 'hi', 4, 5}
l.pop()
print(l)

l = {1, 2, 3, 4, 5}
l.add(6)
print(l)

l = {1, 2, 3, 4, 5, 6, 7, 8}
l.remove(5)
print(l)

l = [1, 2, 3, 4, 5]
l.insert(7, 6)
print(l)

l = {2, 25, 5, 8}
l1 = {1, 2, 3}
l.intersection(l1)
print(l)

l = {2, 25, 5, 8}
l1 = {1, 2, 3}
print(l.intersection(l1))

l = {2, 24, 4, 5}
l.discard(6)
print(l)

l = {2, 24, 4, 5}
l1 = {1, 2, 3, 4}
s = l1.union(l)
print(len(s))
