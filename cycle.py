import itertools
counter=itertools.cycle([1,2,3])
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

#output:
# 1
# 2
# 3
# 1
# 2
# 3

counter=itertools.cycle(("On","Off"))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

#output:
#On
#Off
#On
#Off
#On
#Off
