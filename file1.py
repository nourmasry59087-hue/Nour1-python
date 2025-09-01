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
x=0
counter=1
storage=x
while counter<=10 :
    sum=x+storage
    print (f'current number {x} previous number {storage} sum ={sum}')
    x+=1
    storage=sum
    counter+=1