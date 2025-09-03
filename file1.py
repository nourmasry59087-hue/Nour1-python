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
strnour = input("enter your string")
n = int(input("enter number of removed characters"))
print(strnour[n:])