#! python3
#programa para testar se algo é um padrão devido a seu formato.
#aqui usamos numero de telefone padrão americano xxx-zzz-tttt

import re
def verificaSeETelefone(expressaoTeste):
    if len(expressaoTeste)!=12:
        return False
    for i in range(0,3):
        if not expressaoTeste[i].isdecimal():
            return False
    if expressaoTeste[3]!='-':
        return False
    for i in range(4,7):
        if not expressaoTeste[i].isdecimal():
            return False
    if expressaoTeste[7]!='-':
        return False
    for i in range(8,12):
        if not expressaoTeste[i].isdecimal():
            return False
    return True

print('415-555-4545 é um numero de telefone?')
print(verificaSeETelefone('415-555-4545'))
print('Moshi moshi é um numero de telefone?')
print(verificaSeETelefone('moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
print('Frase de teste para testar se o programa encontra os numeros de telefone')
print(message) 
for i in range(len(message)):
    #print(i)#aqui é so para demonstrar que ele percorre ate o numero
    testeMensagem = message[i:i+12]
    if verificaSeETelefone(testeMensagem):
        print('Numero de telefone encontrado na frase: ' + testeMensagem)
print('Done')

telefoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
fraseTeste = 'My number is 115-555-4242.'#se alterar o numero aqui o else acontece
mo = telefoneNumRegex.search(fraseTeste)
if telefoneNumRegex.search(fraseTeste):
    print('Telefone foi encontrado: ' + mo.group())
else:
    print(f'Padrão criado {telefoneNumRegex} não foi encontrado no texto')
