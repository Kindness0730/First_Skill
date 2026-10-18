# for i in range(0,101):
#     print(i,end=' ')
#     if i%10==0 :print()
# for i in range(0,101):
#     if(i%7==0):print(i," ",end='')
# print()
# for i in range(0,101):
#     if(i%5==0 and i%3!=0): print(i," ",end='')
def divide(x):
    print(f"{x}的因子有：")
    for i in range(2,int(x/2+1)):
        if(x%i==0) :print(i,end=' ')
    print()
for i in range (2,21):
    divide(i)
