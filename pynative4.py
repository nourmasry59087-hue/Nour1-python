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
#list1 = [34, 54, 67, 89, 11, 43, 94]
#print("List After removing element at index 4")
#nour = list1[4]
#del list1[4]
#print(list1)
#print("List after Adding element at index 2")
#list1.insert(2,nour)
#print(list1)
#print("List after Adding element at last")
#list1.insert(len(list1),nour) # or append
#print(list1)


#exercise 3 
#nourlist = [11, 45, 8, 23, 14, 12, 78, 45, 89]
#nourlist2 = nourlist.copy()  #storage
#print("chunck 1 :")
#nourlist2=nourlist[0:3]
#print(nourlist2)
#print("After reversing it")
#nourlist2.reverse()
#print(nourlist2)
#print("chunck 2 :")
#nourlist2=nourlist[3:6]
#print(nourlist2)
#print("After reversing it")
#nourlist2.reverse()
#print(nourlist2)
#print("chunck 3 :")
##nourlist2=nourlist[6:9]
#print(nourlist2)
#print("After reversing it")
#nourlist2.reverse()
#print(nourlist2)


#exercise 4
#sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
#nourdict = {}
#for i in sample_list :
#    nourcount= sample_list.count(i)
#    nourdict.update({i : nourcount})
#print(nourdict)


#exercise 5
#list1 = [2, 3, 4, 5, 6, 7, 8]
#list2 = [4, 9, 16, 25, 36, 49, 64]
#nour=zip(list1,list2)
#print(list(nour))


#exercise 6
set1 = {23, 42, 65, 57, 78, 83, 29}
set2 = {57, 83, 29, 67, 73, 43, 48}
nour=set1.intersection(set2)
print("intersecrtion is :",nour)
nour = set1 - nour
print("First Set after removing common element",nour)