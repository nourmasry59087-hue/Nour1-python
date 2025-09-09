#exercise 1 
#list1 = [3, 6, 9, 12, 15, 18, 21]
#list2 = [4, 8, 12, 16, 20, 24, 28]
#list3 =[]
#print("Element at odd-index positions from list one")
#list1=list1[1::2]
#print(list1)
#print("Element at even-index positions from list two")    
#list2=list2[0::2]
#print(list2)
#print("Printing Final third list")
#list3.extend(list1)
#list3.extend(list2)
#print(list3)


#exercise 2
list1 = [34, 54, 67, 89, 11, 43, 94]
print("List After removing element at index 4")
nour = list1[4]
del list1[4]
print(list1)
print("List after Adding element at index 2")
list1.insert(2,nour)
print(list1)
print("List after Adding element at last")
list1.append(nour)
print(list1)