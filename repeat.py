import itertools
counter=itertools.repeat(2)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

#output:
# 2
# 2
# 2
# 2
# 2

a=pow(x,y,z)
print(a)
#(x^y)%z=a
counter=itertools.repeat(2,times=3)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

#output: 
# 2
# 2
# 2
# 2
# error

counter=itertools.repeat(2,times=3)
square=map(pow,range(10),itertools.repeat(2))
print(list(squares))

#output:[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
