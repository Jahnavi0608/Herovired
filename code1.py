s=0
for i in range(0,5):
    n=int(input())
    if(n>=0):
        s=s+n
    else:
        print("Do not enter negative inputs")
        break
else:
    print(s)
        

'''
output1:
9
8
6
5
7
35
output2:
7
8
5
-7
Do not enter negative inputs
'''
