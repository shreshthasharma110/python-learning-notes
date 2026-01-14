age = 19
#if age<1:
#   print('newborn')
#elif age<10:
#    print('young')
#elif age<20:
 #   print("teen")
#else:
 #   print("adult")
#print("end")
if (age>=1) and (age<=10):  # and operator m ek chiz bhi false hui to vo false ho jayegi
    print('newborn')        #is liye and m ya to dono true ho tb jake true statement ayegi
elif (age>=13) and (age<=20):
    print('teenage')
else:
    print("adult")
print("end")