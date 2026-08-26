# =========================
# IF / ELIF / ELSE
# =========================

age = 27

# if (<condition>):
if age > 18:
    print("You are an adult")
    print("You can enter")
    
    if age == 27:
        print("You are 27 years old")
    
    print("Another line inside the first if")

# elif
elif age == 40:
    print("You are exactly 40")

# else
else:
    print("You are under 18")


# =========================
# WHILE LOOP
# =========================

count = 0

while count < 25:
    count = count + 1
    print("Count is", count)


# =========================
# FOR LOOP WITH RANGE
# =========================

# range(start, stop, step)

for number in range(1, 6, 1):
    print("Number is", number)


# =========================
# LOOPING THROUGH A LIST
# =========================

items = [12, "python", 85, 33, 51]

# Using an index
for index in range(0, len(items)):
    single_item = items[index]
    print("Item:", single_item)


# =========================
# FOR...IN LOOP
# Similar to JavaScript:
# for (let item of items)
# =========================

for single_item in items:
    print("Single item:", single_item)