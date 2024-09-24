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

