#mohammad haje forosh

#Find GCD & LCM

x = int(input("Enter a number1 :"))
y = int(input("Enter a number2 :"))

if x > y: 
    small = y 
else: 
    small = x 
for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            GCD = i
            
LCM = (x*y)/GCD

print("Greatest Common Divisor :",GCD)
print("Lowest common multiple :",LCM )

