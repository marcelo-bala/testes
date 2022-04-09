dtAtual = 2022
Nome = input('Qual o seu nome?')
dtNasc = input('Digite o ano que vc nasceu' )
idade = int(dtAtual) - int(dtNasc)
print(Nome,', Voce tem',idade ,'anos')
if idade > 17:
	print('vc é Maior de idade')
else: 
	print('vc é Menor de idade')
