#input for user
user_in=int(input("Please enter the number : "))

num=user_in
result=0

#len is user for find string length
num_len=len(str(user_in))

while (user_in!=0):
    digit=user_in%10
    result+=digit**num_len
    user_in=user_in//10
    
if (num==result):
    print("Yes %d is a armstrong number"%(num))

else:
    print("No this is not a armstrong number")
