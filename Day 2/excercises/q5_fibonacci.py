# initialize the first two terms
a = 0
b = 1

# print the first 10 terms of the sequence
for i in range(10):
    print(a)
    c = a + b
    a = b
    b = c
