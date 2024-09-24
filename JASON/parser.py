import json

mylist_1 :str = "['mario' , 'gino' , 'lucrezia']"
mylist_2 :list = ['mario' , 'gino' , 'lucrezia']

def SerializzaLista(lVar:list) -> str:
    sVar = str(lVar)
    return sVar, type(sVar)

def DeserializzaLista(sVar:str) -> list:
    lVar = eval(sVar)
    return lVar ,type(lVar)

print(SerializzaLista(mylist_2))
print(DeserializzaLista(mylist_1))

###############################################################################

mydict_1 = { "brand": "Ford",
"electric": False,
"year": 1964,
"colors": ["red", "white", "blue"]}

mydict_2 = "{ 'brand':   'Ford'," + \
"'electric': False," + \
"'year': 1964," + \
"'colors': ['red', 'white', 'blue']}"

# json.dump()
# str1 = json.dumps(mydict_1)

# json.load
# dict_1 = json.loads(mydict_2)

def SerializzaJson(dData:dict , file_path :str) -> bool:
    try:
        with open(file_path,"w") as file:
            file.write(json.dumps(dData))
        return True
    except:
            return False

print(SerializzaJson(mydict_1, "JASON/dict.json"))


def DeserializzaJson(file_path :str) -> dict:
    dict1 = {}
    with open(file_path,"r") as file:
        dict1 = json.loads(file.read())
    return dict1


print(DeserializzaJson("JASON/dict.json"))



