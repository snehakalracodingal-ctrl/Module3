#all prime having 2 digits
num=int(input("Enter a number: "))
for i in range(10,100):
    if i>1:
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)