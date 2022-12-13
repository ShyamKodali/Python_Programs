dict1 = {"1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight"," 9":"nine", "0":"zero"}
phone = input("Phone: ")

res = ""
for key in phone:
    res += dict1.get(key," ! ") + " "
print(res)
