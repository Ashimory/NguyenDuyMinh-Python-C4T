list1=["ST","BĐ","BTL","CG","DĐ","HBT"]
list2=[150300,247100,333300,266800,420900,318000]
list3=[117.43,9.224,43.35,12.04,9.96,10.09]
list4=[]
x=0
for i in range(0,len(list2)):
  pd= list2[x] / list3[x]
  x += 1
  list4.append(pd)
avg = sum(list4) / len(list4)
print("The average population density is", avg)