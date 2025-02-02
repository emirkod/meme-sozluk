import random
import string

length=int(input("merhaba,şifrenin uzunluğunu yazın"))
letters=list(string.ascii_letters)
numbers=list(range(10))
length2=length // 2
length3=length - length2
a=random.sample(letters , length2)
b=random.sample(numbers , length3)
sifre=a+list(map(str , b))
random.shuffle(sifre)
print("sifreniz " + "".join(sifre))
