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

#------------------------------------------------------
# x=int(input("Enter an positive Integer:"))
# y=int(input("Enter an positive Integer:"))
# m=max(x,y)
# n=min(x,y)
# if m%n==0:
#     print("B.M.M = %d \nK.M.M = %d"%(n,m))
# else:       
#     divisor=[]
#     for i in range (1,(n//2)+1):
#         if n%i==0:
#             divisor.append(i)
#     while(1):
#         j=divisor.pop()
#         if m%j==0:
#             print("B.M.M = %d \nK.M.M = %d"%(j,m*n/j))
#             break