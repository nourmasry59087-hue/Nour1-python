#first exercise
#num1 = int (input('number 1 :'))
#num2 = int ( input('number 2 :'))
#product = num1 * num2
#sum = num1 + num2
#if product <= 1000 :
#   print(f'the result is {product}')
#else :
#   print(f'the result is {sum}')


#second exercise
#x=0
#counter=1
#storage=x
#while counter<=10 :
#    sum=x+storage
#    print (f'current number {x} previous number {storage} sum ={sum}')
#    x+=1
#    storage=x-1
#    counter+=1
    
#mohamed's additional exercise
#x=0
#counter=1
#storage=x
#while counter<=10 :
#    sum=x+storage
#    print (f'current number {x} previous number {storage} sum ={sum}')
#    x+=1
#    storage=sum
#    counter+=1


#mohamed unneeded exercise 
#n=10
#sum=n * (n + 1) // 2
#print(sum)


#exercise 3
#strnour = input ("enter your string")
#print(f"original string is {strnour}")
#print('printing only even index chars')
#count =0
#while count<len(strnour) :
#   if count%2==0 :
#        print(strnour[count])
#   count+=1


#exercise 4
#strnour = input("enter your string")
#n = int(input("enter number of removed characters"))
#print(strnour[n:])


#exercise 5
#nourlist = []
#istrue = True
#n = int(input("what's the number of entered numbers"))
#while n>0 :
#    nourlist.append(int(input("enter number")))
#    n-=1    
#if nourlist[0] == nourlist[-1] :
#    print(istrue)
#else :
#    istrue=False
#    print(istrue)


#exercise 6
#nourlist = []
#n = int(input("what's number of list numbers"))
#for i in range(n) :
#    nourlist.append(int(input("enter number")))
#    if nourlist[i]%5==0 :
#        print(nourlist[i])


#exercise 7
#nourstring = input('enter your string')
#nourstring.split()
#print(nourstring.count('emma'))


#exercise 10
#list1 = [10, 20, 25, 30, 35]
#list2 = [40, 45, 60, 75, 90]
#nourlist = []
#for i in list1 :
#    if i % 2 !=0 :
#        nourlist.append(i)
#for n in list2 :
#    if n % 2 ==0 :
#        nourlist.append(n)
#print(nourlist) 


#exercise 16
#nourpalindrome = input('enter your number')
#nourpalindrome=list(nourpalindrome)
#nour2=nourpalindrome.copy()
#nour=nourpalindrome.reverse()
#print(nourpalindrome)
#print(nour2)
#if nourpalindrome == nour2:
#         print('palindrome')
#else :
#         print('not palindrome')


#exercise 17
#nour1=0
#nour2 =1
#print(nour1)
#print(nour2)
#for i in range(10) :
#        sum = nour1+nour2
#        print(sum)
#        nour1=nour2
#        nour2=sum
        
        
        


#exercise 19
isprime = True
nourprime =set()
for i in range(1,20) :
    if i > 1 :
        for n in range (2,i) :
            if i%n ==0 :
                break
            else :
                nourprime.add(i)
print(nourprime)                
            