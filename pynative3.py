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
nour+=1
print(num)
sum=0
z=0
terms=int(input("terms:"))
for i in range(0,terms) :
    z = (z*10)+nour
    sum+=z
    print(nour)
    print(z)
    print('#'*50)
print(sum)


#exercise 19
#num=int(input("multiplication table of "))