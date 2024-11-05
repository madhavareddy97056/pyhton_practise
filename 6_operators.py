# arthemetic operators
x = 8
y = 4

total = x + y
print(total)     #12

total = x - y
print(total)    #4

total = x * y
print(total)  #32

total = x/y
print(total)  #2.0

total = x % y
print(total)  #0

total = x**y
print(total)  #4096
#----------------------------------------------
# Comparision operator
a = 30
b = 50

c = (a > b)
print(c)  # false

c = (a < b)
print(c)  # True

c = (a >= b)
print(c) # false

c = (a <= b)
print(c) # true

c = (a != b)
print(c)  # true
#----------------------------------------------
# logical operator (and, or)
p = 40
q = 50
r = (p < q) or (p > q)
print(r)

r = (p < q) and (p > q)
print(r)
#----------------------------------------------
# membership operator (in)
sports = ["carrom", "cricket", "tennis", "running",["chess", "badminton", "tt", "koko"], "hockey", "volleyball", "football"]
game = "koko" in sports[4]
print(game)  # true

hero_tuple = ("prabhas", "ntr", "ram charan", "allu arjun", "rajini", "rana")
actor = "venky" in hero_tuple
print(actor)
