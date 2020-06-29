dairy_section = ["milk", "cottage cheese", "butter", "yogurt"]
print(dairy_section)

# print first and last element

print("First : %s and Last %s" % (dairy_section[0], dairy_section[-1]))

milk_expiration = (10, 10, 2009)

print("This milk will expire on %d/%d/%d" % (milk_expiration[0], milk_expiration[1], milk_expiration[2]))


# create an empty dictionary empty_carton.  Add the following key/value pairs.  You can make up the values or use a real
# milk carton:
milk_carton = {}
milk_carton["expiration_date"] = milk_expiration
milk_carton["fl_oz"] = 32
milk_carton["cost"]= 1.50
milk_carton["brand_name"] = "Milk"

print(" The expiration date is %d %d %d" % (milk_carton["expiration_date"][0], milk_carton["expiration_date"][1], milk_carton["expiration_date"][2]))

# show how to calculate the cost of six cartons of milk based on the cost of milk_carton.

print("The cost for 6 cartons of milk is $%.02f" % (6*milk_carton["cost"]))

#create a list called cheese. Append this list to the dairy_section list, and look at the contents of the dairy section

cheeses = ["cheddar", ["american", "mozzarella"]]

dairy_section.append(cheeses)
print(dairy_section)
dairy_section.pop()
print(dairy_section)

print(len(dairy_section))
# print out the first five letters of the name of your first cheese.

print("Part of some cheese is %s" % cheeses[0][0:5])


omelet_ingredients = {"egg": 2, "mushroom" : 5, "pepper": 1, "cheese" : 1, "milk": 1}
fridge_contents = {"egg": 10, "mushroom": 20, "pepper": 3, "cheese": 2, "tomato": 4, "milk": 15}
have_ingredients = [False]
if fridge_contents["egg"] > omelet_ingredients["egg"]:
    have_ingredients[0] = True

have_ingredients.append("egg")

print(have_ingredients)

if fridge_contents["mushroom"] > omelet_ingredients["mushroom"]:
    if have_ingredients[0] ==  False:
        have_ingredients = True
    have_ingredients.append("mushroom")
print(have_ingredients)


if fridge_contents["pepper"] > omelet_ingredients["pepper"]:
    if have_ingredients == True:
        have_ingredients = False
    have_ingredients.append("pepper")
print(have_ingredients)


if fridge_contents["cheese"] > omelet_ingredients["cheese"]:
    if have_ingredients[0] == False:
        have_ingredients[0] = True
    have_ingredients.append("cheese")
print(have_ingredients)

if fridge_contents["milk"] > omelet_ingredients["milk"]:
    if have_ingredients[0] == True:
        have_ingredients[0] = False
    have_ingredients.append("milk")
print(have_ingredients)

if have_ingredients[0] == True:
    print("I have the ingredients to make an omelet!")



milk_price= 2.50
if milk_price < 1.25:
    print("Buy two cartons of milk, they're on sale")
elif milk_price < 2.00:
    print("Buy one carton of milk, prices are normal")
elif milk_price > 2.00:
    print(("Go somewhere else! Milk cost too much here"))


OJ_price = 2.50
if OJ_price < 1.25:
    print("Get one, I'm thirsty.")
elif OJ_price <= 2.00:
    print("Umm... sure,  but I'll drink it slowly.")
else:
    print(("I dont have enough money.  Never mind"))

import time
i = 10
while i > 0 :
    print("Lift off in :")
    print(i)
    time.sleep(35)
    i = i-1

for i in range(10,0,-1):
    print("T-minus:")
    print(i)
    time.sleep(15)



age = 0
while True:
    how_old = int(input("Enter your age:"))
    if how_old == "No":
        print("Done be ashamed of your age!")
        break

    num = int(how_old)
    age = age+num
    print("Your age is :", age)
    print("That is old!")


import time
for food in ("pate" , "cheese" , "rotten apples" , "crackers" , "whip cream" , "tomato soup" ):
    if food[0:6] == "rotten":
        continue
    print("Hey you can eat %s" % food)
    time.sleep(2)


fridge_contents = {"egg": 8,  "mushroom": 20, "pepper": 3, "cheese": 2, "tomato": 4, "milk": 13}
try:
    if fridge_contents["orange juice"] > 3:
        print("Sure, lets have some juice")
except (KeyError, TypeError) as error:
    print("Woah!  There is no %s" % error)



fridge_contents = {"egg": 8,  "mushroom": 20, "pepper": 3, "cheese": 2, "tomato": 4, "milk": 13}
try:
    if fridge_contents["orange juice"] > 3:
        print("Sure, lets have some juice")
except (KeyError) as error:
    print("Woah!  There is no %s" % error)
except(TypeError) as error:
    pass

if 0 :
    print("0 is True")
if 1:
    print("1 is True")
if 2:
    print("2 is True")

if 3:
    print("3 is True")

if 4:
    print("4 is True")

if 5:
    print("5 is True")

number =  3
if number >= 0 and number <= 9:
    print("The number is between 0 and 9: %d" % number)

''' Using if ..... elif.... and else, create a test for whether a value referred to by a name is in the
first two elements of a sequence.
Use the if to test for the first element of the list
Use the elif to test the second value referenced in the sequence,
and use the else clause to print a message indicating whether
the element being searched for is not in the list.
'''

test_tuple = ("this",  "little", " piggie", "went",  "to", "market")
search_string = "toes"
if test_tuple[0] == search_string:
    print("The first element matches")
elif test_tuple[1] == search_string:
    print("The second element matches")
elif test_tuple[2] == search_string:
    print("The Third element matches")
else:
    print("%s was not found in the three elements" % search_string)


import time
fridge = {"butter": "Dairy spread", "peanut butter": "non-dairy spread", "cola":"fizzywater"}
food_sought = "chicken"
for food_key in fridge.keys():
    if food_key == food_sought:
        print("Found what I was looking for: %s is %" % (food_sought,fridge[food_key]))
        break
    else:
        print("%s was not found in the fridge" % food_sought)
        time.sleep(3)


test_tuple = ("this",  "little", " piggie", "went",  "to", "market")
search_string = "toes"
if test_tuple[0] == search_string:
    print("The first element matches")
elif test_tuple[1] == search_string:
    print("The second element matches")
elif test_tuple[2] == search_string:
    print("The Third element matches")
else:
    print("%s was not found in the three elements" % search_string)






import time
fridge = {"butter": "Dairy spread", "peanut butter": "non-dairy spread", "cola":"fizzywater"}
fridge_list = fridge.keys()
current_key = fridge.popitem()
food_sought = "cola"
while len(fridge_list) > 0:
    if current_key == food_sought:
        print("Found what I was looking for:  %s is %s" % (food_sought,fridge[current_key]))
        break
        current_key = fridge.popitem()
    else:
        print("%s was not found in the fridge" % food_sought)

for food_key in fridge.keys():
    if food_key == food_sought:
        print("Found what I was looking for: %s is %" % (food_sought,fridge[food_key]))
        break
    else:
        print("%s was not found in the fridge" % food_sought)
        time.sleep(3)

