'''
1-Crie um dicionário contendo dias da semana sendo dia1,dia2,dia3...as chaves e o dia seu valor. Ex: “dia1”: “domingo”.
2-Remova dois dos últimos dias da semana.
3-Remova segunda-feira pela sua chave.4-Imprima chaves e valores do dicionário.
5-Imprima o dicionário final.
'''

dias_semana = {"dia1":"Domingo", "dia2":"Segunda", "dia3":"Terça", "dia4":"Quarta", "dia5":"Quinta", "dia6":"Sexta", "dia7":"Sabado",} 

dias_semana.popitem()
dias_semana.popitem()

del(dias_semana["dia2"])

print(dias_semana.keys())
print(dias_semana.values())

print(dias_semana)


