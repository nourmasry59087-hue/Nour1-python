#exercise 6
#nournum = input('enter number')
#nournum=list(nournum)
#print(len(nournum))

#exercise 11 
start = int (input('start:'))
end = int (input('end :'))
nourprime=set()
for i in range (start , end+1) :
    isprime=True
    if i > 0 :
        for n in range(2 , i) :
            if i%n ==0 :
                isprime=False
                break
        if isprime == True :
            nourprime.add(i)
nourprime=sorted(nourprime)
print(nourprime)