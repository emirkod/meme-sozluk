import random

karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk=int(input("şifre uzunluğunu giriniz : "))
sifre = random.sample(uzunluk)

print(sifre)
