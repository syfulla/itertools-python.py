import itertools
letters=['a','b','c','d']
numbers=[1,2,3]
names=['cooley','billy']
result=itertools.combinations(letters,2)
for i in result:
    print(i)

#output:
#('a', 'b')
#('a', 'c')
#('a', 'd')
#('b', 'c')
#('b', 'd')
#('c', 'd')

result=itertools.permutations(letters,2)
for i in result:
    print(i)
#output:
#('a', 'b')
#('a', 'c')
#('a', 'd')
#('b', 'a')
#('b', 'c')
#('b', 'd')
#('c', 'a')
#('c', 'b')
#('c', 'd')
#('d', 'a')
#('d', 'b')
#('d', 'c')
