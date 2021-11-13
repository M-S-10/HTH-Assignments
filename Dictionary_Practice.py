Food_Prices = {'Chicken' : 1.59, 'Beef' : 1.99, 'Cheese': 1.00, 'Milk' : 2.50}

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

print()

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

Food_Prices['Food_item2read'] = '$2.25'
Food_Prices['Apples'] = '$1.74'
Food_Prices['Food_item2ananas'] = '$0.85'

del Food_Prices['Apples']
del Food_Prices['Food_item2ananas']

print(Food_Prices)

print("\nFunctions, Looping and Operators")

print()

def total_price (Food_item1, Food_item2) :

    if (Food_item1 or Food_item2) not in Food_Prices :
        print("Either {} or {} are not in the dictionary".format(Food_item1, Food_item2))

    else :  
        total = Food_Prices[Food_item1] + Food_Prices[Food_item2]
        
        statement = "The total price of {} and {} is ${}".format(Food_item1, Food_item2, total)
        
        return statement

print(total_price("Beef", "Cheese"))

print()

def price_difference (Food_item1, Food_item2) :

    if (Food_item1 or Food_item2) not in Food_Prices :
        print("Either {} or {} are not in the dictionary".format(Food_item1, Food_item2))

    else : 
        difference = Food_Prices[Food_item1] - Food_Prices[Food_item2]

        statement = "The difference between {} and {} is ${}".format(Food_item1, Food_item2, abs(difference))
        
        return statement

print(price_difference("Beef", "Cheese"))

print()

def restock (Shoe_name, multiple) :

    if Shoe_name not in Shoe_Count :
        print("{} is not in dictionary".format(Shoe_name))

    else : 
        Shoe_Count[Shoe_name] *= multiple
        
        return Shoe_Count

print(restock("Yeezy", 3))

print()

def clearance_sale (Shoe_name, factor) :

    if Shoe_name not in Shoe_Count :
        print("{} is not in dictionary".format(Shoe_name))

    else :
        Shoe_Count[Shoe_name] //= factor

        return Shoe_Count

print(clearance_sale("SB Dunk", 2))

print()

def capital (country) :

    country = country.capitalize()

    if country not in Country_Capitals :
        print("{} is not a valid country name")

    else :
        return Country_Capitals[country]

print(capital("Finland"))

    