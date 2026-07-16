'''
Questão 1 – Cadastro simples 

Crie um programa que: 

 - Armazene o nome de uma pessoa em uma variável name. 
 - Armazene a idade em outra variável age.
 - Exiba a seguinte mensagem, em que os valores devem vir das variáveis:  

Olá João, você tem 20 anos. 
 
'''
name = "Raphael da Conceição"

age = 27

print('Olá' , name, "você tem" , age , "anos de idade."  )

print(f'Olá {name} você tem {age} anos de idade.')

print('Olá' + name + ', você tem ' + str(age) + 'anos de idade.')