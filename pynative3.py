#exercise 6
#nournum = input('enter number')
#nournum=list(nournum)
#print(len(nournum))

#exercise 11 
#start = int (input('start:'))
#end = int (input('end :'))
#nourprime=set()
#for i in range (start , end+1) :
#    isprime=True
#    if i > 0 :
#        for n in range(2 , i) :
#            if i%n ==0 :
#                isprime=False
#                break
#        if isprime == True :
#            nourprime.add(i)
#nourprime=sorted(nourprime)
#print(nourprime)


#exercise 13
#num=int(input("enter number : "))
#for i in range(num-1,1,-1) :
#    num=num*i
#print(num)


#exercise 14 
#num = input("enter number :")
#num = list(num)
#num.reverse()
#num = "".join(num)
#print(num)


#exercise 17
num=int(input("num:"))
nour=num                           #storage
sum=num
terms=int(input("terms:"))
for i in range(0,terms-1) :
    num = (num*10)+nour
    sum+=num
print(sum)