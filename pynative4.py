#exercise 1
#list1 = [3, 6, 9, 12, 15, 18, 21]
#list2 = [4, 8, 12, 16, 20, 24, 28]
#list3 = [] 
#print("Element at odd-index positions from list one")
#for i in range(0,6+1) :
#    if i % 2 ==0 :  
#        del list1 [i]
#print(list1)
#print("Element at even-index positions from list two")    
#for i in range(0,6+1) :
#    if i % 2 !=0 :
#        del list2 [i]
#print(list2)
#print("Printing Final third list")
#list3.extend(list1)
#list3.extend(list2)
#print(list3)

#exercise 1 better version
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
list3 =[]
print("Element at odd-index positions from list one")
list1=list1[1::2]
print(list1)
print("Element at even-index positions from list two")    
list2=list2[0::2]
print(list2)
print("Printing Final third list")
list3.extend(list1)
list3.extend(list2)
print(list3)