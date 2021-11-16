print()

US_Cities = ["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
print(US_Cities)

programming_languages = ["Python", "Java", "Ruby", "C++", "R", "Kotlin", "solidity", "Go", "Swift", "Rust", "Scala"]
print(programming_languages)

print()

print(US_Cities[2])
print(US_Cities[3])
print(US_Cities[7])

print()

print(programming_languages[0])
print(programming_languages[1])
print(programming_languages[-5])

print()
# Slicing 

last_4 = US_Cities[6:9]
print("Last 4 US Cities are : ", last_4)

first_4 = programming_languages[0:3]
print("First 4 Programming languages are : ", first_4)

# Changes

US_Cities[0] = "San Francisco"
US_Cities[2] = "Brooklyn"
US_Cities[-3] = "Hollywood"
US_Cities[5] = "Tampa"

print()

print("List after changes : ", US_Cities)

# Adding back

US_Cities.append("New Jersey")
US_Cities.extend(["New York City", "Los Angeles"])
US_Cities.insert(0, "Miami")

print()

print("List after adding the elements back : ", US_Cities)

# Removing

del US_Cities[6]
US_Cities.pop(-4)
US_Cities.remove("Memphis")

print()

print("List after removing : ", US_Cities)

print("\nFunctions, Looping and Operators")

print()

def show (list) :
    for item in list :
        print(item)

    return None

show(US_Cities)

print()

def city () :
    i = 0

    for citi in US_Cities  :

        if i < 10 :

            if len(US_Cities[i]) < len(US_Cities[i+1]) :
                print(US_Cities[i+1])
                i += 1

            else : 
                i += 1
                continue

            # When using WHILE LOOP, replace entire for statement with "While i < 10 :" and remove the first IF Conditional.

city()

print()

def order (list) :
    i = 0

    while i < (len(list) - 1) : 
        item1 = list[i]
        item2 = list[i + 1]

        if len(item1) >= len(item2) :
            i += 1
            continue

        else : 
            list.remove(item1)
            list.append(item1)
            i += 1

    return list

print(order(US_Cities))

print()

# Bonus 

a = [9, 13, 1, 8, 12, 4, 0, 5]

b = [3, 17, 4, 14, 6,]

t = 20

def close_sum (list1, list2, target) :
    i = 0
    j = 0

    while i < len(list1) :
        num1 = list1[i]

        while j < len(list2) :
            num2 = list2[j]

            if (num1 + num2 == target + 1) or (num1 + num2 == target -1) :
                print([num1, num2])
                j += 1

            else :
                j += 1

        j = 0        
        i += 1


close_sum(a, b, t)