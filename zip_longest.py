import itertools
data=[200,300,400,500]
daily_data=list(zip(itertools.count(),data))
print(daily_data)

#output:[(0,200),(1,300),(2,300),(3,400),(4,500)]

daily_data2=list(zip(range(10),data)
print(daily_data)

#output:[(0,200),(1,300),(2,300),(3,400),(4,500)]
                 
daily_data3=list(itertools.zip_longest(range(10),data))
print(daily_data3)

#output:[(0,200),(1,300),(2,300),(3,400),(4,500),(5,none),(6,none),(7,none),(8,none),(9,none)]
