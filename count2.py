import itertools

data=[200,300,400,500]
daily_data=list(zip(itertools.count(),data))
print(daily_data)

#output:[(0,200),(1,300),(2,400),(3,500)]

counter=itertools.count(start=5)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

#output:
# 5
# 6
# 7
# 8

counter=itertools.count(start=5,step=2)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

#output:
# 5
# 7
# 9
# 11

counter=itertools.count(start=5,step=-2.5)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

#output:
# 5
# 2.5
# 0
# -2.5
