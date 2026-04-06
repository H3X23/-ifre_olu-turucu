import random
import string

# Sayıları rastgele seçiyoruz
sayi1 = random.randint(1, 100)
sayi2 = random.randint(1, 100)

# 8 karakterli rastgele harf dizileri oluşturuyoruz
harf1 = "".join(random.choice(string.ascii_letters) for _ in range(8))
harf2 = "".join(random.choice(string.ascii_letters) for _ in range(8))

#Sembol üretme
sembol1 = "".join(random.choice(string.punctuation) for _ in range(2))
sembol2 = "".join(random.choice(string.punctuation) for _ in range(2))
print("İşte şifren:")
print(f"{sayi1}{harf1}{sembol1}{sayi2}{sembol2}{harf2}")
