list1=["ST","BĐ","BTL","CG","DĐ","HBT"]
list2=[150300,247100,333300,266800,420900,318000]
m1=list2.index(max(list2))
m2=list2.index(min(list2))
print("Most populated:", list1[m1])
print("Least populated:", list1[m2])