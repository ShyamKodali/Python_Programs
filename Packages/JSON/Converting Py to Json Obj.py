import json

# x is Python Dictionary 

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# Python Obj(x == Dict) converts into json string using json.dumps() 

py_to_json = json.dumps(x, indent=2, separators=(". ", " = "), sort_keys=True) # indent , separators, sort_keys --> Optional

print(py_to_json)