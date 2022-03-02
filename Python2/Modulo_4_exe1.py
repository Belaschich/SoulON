'''
Criando uma base de dados com todos os dados necessários transmitindo os 
dados para o Mongo DB via VS Code! 
'''

from pymongo import collection

def get_database():
    from pymongo import MongoClient

    CONNECTION_STRING = "mongodb+srv://Schick:Bela1986@schick.t7zh5.mongodb.net/aula_Python?retryWrites=true&w=majority"
    
    client = MongoClient(CONNECTION_STRING)
    print("Conectado com sucesso...")
    return client['aula_Python']
    
dbname = get_database()
collection_name = dbname["Jornais"]

item_1 = {"_id":"001",
"Nome":"Folha de São Paulo ",
"Ano":{"$numberLong":"2010"},
"edição":"-"
}

item_2 = {"_id":"002",
"Nome":"Jornal Atribuna",
"Ano":{"$numberLong":"2000"},
"edição":"00282"

}

item_3 = {"_id":"003",
"Nome":"Folha de São Paulo",
"Ano":{"$numberLong":"1972"},
"edição":"-"
}

item_4 = {"_id":"004",
"Nome":"Correio da Manhã Brasil",
"Ano":{"$numberLong":"2021"},
"edição":"23.894"
}

item_5 = {"_id":"005",
"Nome":"Jornal correio do Amanhã",
"Ano":{"$numberLong":"2021"},
"edição":"23.895"
}

item_6 = {"_id":"006",
"Nome":"Jornal expresso Popular",
"Ano":{"$numberLong":"2001"},
"edição":"300"
}

item_7 = {"_id":"007",
"Nome":"Jornal da Orla",
"Ano":{"$numberLong":"2010"}, 
"edição":"5026"
}

item_8 = {"_id":"008",
"Nome":"Jornal Atribuna",
"Ano":{"$numberLong":"2022"},  
"edição":"190"
}

item_9 = {"_id":"009",
"Nome":"O Globo",
"Ano":{"$numberLong":"2005"},  
"edição":"2653"
}

item_10 = {"_id":"0010",
"Nome":"Estadão",
"Ano":{"$numberLong":"2019"},  
"edição":"1873"
}

item_11 = {"_id":"0011",
"Nome":"Joral de Negócios",
"Ano":{"$numberLong":"2018"},  
"edição":"0918"
}

item_12 = {"_id":"0012",
"Nome":"A Orla",
"Ano":{"$numberLong":"2015"},  
"edição":"927"
}

item_13 = {"_id":"0013", 
"Nome":"Jornal a Tribuna",
"Ano":{"$numberLong":"2020"},  
"edição":"9217"
}

item_14 = {"_id":"0014", 
"Nome":"Estadão",
"Ano":{"$numberLong":"2014"},  
"edição":"817"
}

item_15 = {"_id":"0015", 
"Nome":"O Globo",
"Ano":{"$numberLong":"2018"},  
"edição":"9273"
}