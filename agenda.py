from os import system

print('Bemv-vindo a agenda.')
lista_de_contatos = []

def add_contato(): #Funcao que adiciona os contatos na angenda.
    name = str(input('Digite o nome do contato: ')).title()
    numero = int(input('Digite o numero: '))
    system ('clear')
    lista_add = {}
    lista_add['Nome'] = name
    lista_add['Numero'] = numero
    lista_de_contatos.append(lista_add)
    print('##########################')
    print('Adicionado com sucesso !!')
    print('##########################')
    

def mostra_contatos():
    system ('clear')
    print('##########################')
    for contato in lista_de_contatos:
        for chave, valor in contato.items(): 
            print(f'{chave}: {valor}')
        print('\n')
    print('##########################')     

def remove_contato():
    nome = str(input('Digite o nome que deseja remover: ')).lower()
    for c in lista_de_contatos:
        if c['Nome'].lower() == nome.lower():
            i = lista_de_contatos.index(c)
            lista_de_contatos.pop(i)
            break
        else:
            print('Esse contato nao existe')
    return         

def edita_contato():
    nome = str(input('Digite o nome que deseja editar: ')).lower()
    for c in lista_de_contatos:
        if c['Nome'].lower() == nome.lower():
            opc=int(input('Deseja alterar o nome ?\n1-Sim\n2-Nao '))
            if opc == 1:
                system ('clear') 
                novo = str(input('Digite o novo nome : '))
                c['Nome'] = novo  
            opc=int(input('Deseja alterar o numero ?\n1-Sim\n2-Nao '))
            if opc == 1:
                system ('clear') 
                num = int(input('Digite o novo numero: '))
                c['Numero'] = num
            system ('clear')    
            print('##########################')
            print('Atualizado com sucesso !!')
            print('##########################')
        else:
            print('Esse contato nao existe')
            break

while True:
    
    print('1-Adicinar contato.')
    print('2-Mostrar contato.')
    print('3-Remover contato.')
    print('4-Editar contato.')
    print('5-Sair.')
    
    
    op = int(input('Digite sua opcao: '))
    system ('clear')
    if op == 1:
        add_contato()
    if op == 2:
        mostra_contatos()
    if op == 3:
        remove_contato()
    if op == 4:
        edita_contato()
    if op == 5:
        break    

system ('clear')
print('Obrigado por usar , esse foram os seus contatos:')    
mostra_contatos()