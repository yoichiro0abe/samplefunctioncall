def getFirstNameInJapanese(name:str)->str:
    name_dic = dict()
    name_dic["大谷"] = "翔平"
    name_dic["熊田"] = "ショウ"
    name_dic["Furuyama"] = "Sho"
    return f"{name}さんの名前は {name_dic.get(name)}です"


def getFirstNameinEnglish(name:str)->str:
    name_dic = dict()
    name_dic["Trout"] = "Mike"
    name_dic["Gate"] = "Bill"
    name_dic["Fusco"] = "Sho"

    return f"Hi, {name}'s fisrt name is {name_dic.get(name)}."


