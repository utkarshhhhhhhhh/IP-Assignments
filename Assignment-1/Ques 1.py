def unit_digit(n):
    list_1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    list_2=["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    index=list_1.index(n)
    return list_2[index]

def ten_digit(n,temp):
    list_3=[20,30,40,50,60,70,80,90]
    list_4=["Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    index=list_3.index(temp)
    return list_4[index]

n=int(input())
if n<20:
    word=unit_digit(n)
    print(word)
else:
    rem=n%10
    temp=(n//10)*10
    word=ten_digit(n,temp) + " " + unit_digit(rem)
    print(word)
