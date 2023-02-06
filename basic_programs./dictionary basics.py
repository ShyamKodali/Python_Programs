# Dict Basics 

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Using get method to get value 

print(car.get("model"))

# Updating the value of key and Printing

car["year"] = 2020
print(car.get("year"))

# Adding New Key/Value pair to the Dict

car["color"]= "red"
print(car)

# Using pop method

car.pop("model")

# Using clear method

car.clear()
print(car)

# Using update method

car.update({
  "brand": "Mazda",
  "model": "CX5",
  "year": 2015
})
car_details = {"color":"blue"}
car.update(car_details)
print(car)

# Using pop method 

print(car.pop("year"))
print(car)
