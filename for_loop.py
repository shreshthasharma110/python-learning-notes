grocery_list=["apple","banana","pineapple"]
grocery_list.append(["4",'5'])

# difernet way of using (for loop) in python

#for iteam in grocery_list:
 #   print(iteam)

#for i in [0,1,2,3,]:
  #  print(grocery_list[i])
    
#for i, iteam in enumerate(grocery_list):
   # print(i, iteam)

for i in range(len(grocery_list)):
    print(grocery_list[i])
