x = 5
k = "#"

# plny ctverec


def ukol_1(x):
     for i in range(x):
          print(x * "#")


print("\n")

# prazdny ctverec
o = " "
def ukol_2(x):
     for i in range(x):
          if i == 2 or  i == 3 or i == 1:
               print(k + (x-2) * o + k)
          else:
               print(k * x)

print("\n")

# pravouhly trojuhelnik
def ukol_3(x):
     m = 1
     for i in range(x):
          print(k * m)
          m += 1

print("\n")

# pyramida

def ukol_4(x):
     p = 1
     for i in range(x):
          print(((x-1) * o) + (p * "#") + ((x-1) * o))
          x = x - 1
          p = p + 2
print("\n")
# kříž

def ukol_5(x):
     h = x
     for i in range(x):
          print(" "*i + k + ((x+4)*" ") + k + " "*i)
          x = x-2
     for i in reversed(range(h)):
          print(" "*i + k + ((x+4)*" ") + k + " "*i)
          x = x+2


# diamant

def ukol_6(x):
     p = 1
     s = x
     for i in range(x):
          print(((x - 1) * " ") + (p * "#") + ((x - 1) * " "))
          x = x - 1
          p = p + 2

     for i in reversed(range(s)):
          print(((x - 1) * " ") + (p * "#") + ((x - 1) * " "))
          x = x + 1
          p = p - 2




print(ukol_1(x))
print(ukol_2(x))
print(ukol_3(x))
print(ukol_4(x))
print(ukol_5(x))
print(ukol_6(x))