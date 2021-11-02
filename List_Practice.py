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

print()