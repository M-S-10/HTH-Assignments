Food_Prices = {'Chicken' : '$1.59', 'Beef' : '$1.99', 'Cheese': '$1.00', 'Milk' : '$2.50'}

Country_Capitals = {'Finland' : 'Helsinki', 'Hungary' : 'Budapest', 'Greece' : 'Athens', 'France' : 'Paris', 'Germany' : 'Berlin' }

Finland_Capital = Country_Capitals['Finland']
Hungary_Capital = Country_Capitals['Hungary']
Greece_Capital = Country_Capitals['Greece']
France_Capital = Country_Capitals['France']
Germany_Capital = Country_Capitals['Germany']


Chicken_Price = Food_Prices['Chicken']
print(Chicken_Price)

Beef_Price = Food_Prices['Beef']
print(Beef_Price)

Cheese_Price = Food_Prices['Cheese']
print(Cheese_Price)

Milk_Price = Food_Prices['Milk']
print(Milk_Price)

print()

print(Finland_Capital)

print(Hungary_Capital)

print(Greece_Capital)

print(France_Capital)

print(Germany_Capital)

print()

Country_Capitals['Netherlands'] = 'Amsterdam'
print(Country_Capitals)

print ()

Shoe_Count = {"Jordan 13" : 1 , "Yeezy" : 8 , "Foamposite" : 10 , "Air Max" : 5 , "SB Dunk" : 20}
print(Shoe_Count)

print()

Shoe_Count['SB Dunk'] -= 2
print("SB Dunks count after purchase :", Shoe_Count['SB Dunk'])

Shoe_Count['Yeezy'] += 1
print("Yeezys count after return :", Shoe_Count['Yeezy'])

Shoe_Count['Jordan 13'] += 7
Shoe_Count['Yeezy'] += 7
Shoe_Count['Foamposite'] += 7
Shoe_Count['Air Max'] += 7
Shoe_Count['SB Dunk'] += 7

print("Count after new shipmentt :", Shoe_Count)

# Shoe_Count = Shoe_Count.setdefault("Jordan 13", "Yeezy", "Foamposite", "Air Max", "SB Dunk", -=3 )

Shoe_Count['Jordan 13'] -= 3
Shoe_Count['Yeezy'] -= 3
Shoe_Count['Foamposite'] -= 3
Shoe_Count['Air Max'] -= 3
Shoe_Count['SB Dunk'] -= 3
print("Count after special sale :", Shoe_Count)