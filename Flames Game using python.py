import random

name_1 = str(input("Enter your name")) #Getting input from user.
name_2 = str(input("Enter your crush name")) #Getting input from user.
 
a = list(name_1.lower().replace(" ","")) #converting the input as list and replace that as without sapce.
b = list(name_2.lower().replace(" ","")) #converting the input as list and replace that as without sapce.

c = []

for i in a:
    for j in b:
        if(i == j):
            c += i
            
        else:
            continue

for i in range(len(c)):
    try:
        a.remove(c[i])
        b.remove(c[i])
    except ValueError:
        pass

d = len(a) + len(b)

flames = ["F","L","A","M","E","S"]

while len(flames) > 1:
    formula = d % len(flames) - 1
    if(formula >= 0):
        left = flames[formula + 1:]
        right = flames[:formula]
        flames = left + right
    else:
        flames = flames[:len(flames) -1]

def friends():
    q = ['Your are the bestfriends ever',"Friends Forever"]
    print(random.choice(q))

def love():
    e = ["Your are the best couples", "You both have something in your heart that seems to be love"]
    print(random.choice(e))

def affection():
    print("You both have affection on eachOther")

def marriage():
    print("You will get Married soon...")

def enemy():
    print("You both don't have chemistry")

def siblings():
    print("You both are siblings")

print(flames)

if flames == ["F"]:
    friends()
elif flames == ["L"]:
    love()
elif flames == ["A"]:
    affection()
elif flames == ["M"]:
    marriage()
elif flames == ["E"]:
    enemy()
elif flames == ["s"]:
    siblings()
