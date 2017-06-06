import operator
from functools import reduce

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
print("gcd(2,10) =",gcd(2,10))

def lcm(a, b):
    return (a * b) // gcd(a, b)
print("lcm(3,10) =",lcm(3,10))

def fact(n):
    return n > 1 and n * fact(n - 1) or 1

print ("fact(5) =", fact(5))  
print ("fact(7) =", fact(7))  

def alpha_score(upper_letters):
    return sum(map(lambda l: 1 + ord(l) - ord('A'), upper_letters))

print ("alpha_score('ABC') =",alpha_score('ABC'))  

def two_best(words):
    words.sort(key=lambda word: alpha_score(filter(str.isupper, word)), reverse=True)
    return words[:2]

print (two_best(['hEllO', 'wOrLD', 'i', 'aM', 'PyThOn']))


def generate_triangles():
    n = 0
    total = 0
    while True:
        total += n
        n += 1
        yield total

print("Triangles: ",generate_triangles())
