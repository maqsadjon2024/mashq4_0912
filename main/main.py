#16
scores = [65, 85, 45, 95, 70]
high_scores = [score for score in scores if score > 70]
print(high_scores)

#17
words = ["hello", "123", "world", "456"]
letters_only = [word for word in words if word.isalpha()]
print(letters_only)

#18
sonlar = range(1, 21)

natija = [son for son in sonlar if son % 3 == 1]
print(natija)

#19
prime_sonlar = [
    n for n in range(2, 51)
    if all(n % i != 0 for i in range(2, int(n**0.5) + 1))
]

print(prime_sonlar)

#20
sonlar = [1, 2, 3, 4, 5]

natija = ["even" if son % 2 == 0 else "odd" for son in sonlar]
print(natija)
