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
     for i in range(x):
          print(k)
          k += "#"

print("\n")

# pyramida
def ukol_4(x):
     for i in range(x):
          print(k)
          k += "#"
