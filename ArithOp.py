# write a program to accept integer numbers and perform all arithmatic operation including exponent and floor division

a=int(input("enter first number :"))
b=int(input("enter second number :"))
c=0

op=input("choose your operation :")
match op:
    case '+':
        c=a+b
        
    case '-':
        c=a-b
    
    case '*':
        c=a*b
    
    case '%':
        c=a%b
    
    case '/':
        c=a/b
    
    case '//':
        c=a//b
    
    case '**':
        c=a**b
        
print(f" {a} {op} {b} is:", c)
        
    


        
        