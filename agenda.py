contatos = [{"nome": "Xarabacaia", "telefone": "11999999999", "email": "xaolindegolador@gmail.com"}, {"nome": "Aroldo", "telefone": "11959659999", "email": "otorrino@gmail.com"}]
favctt = []

def mostrarContatos(contatos):
    index = 0
    for contato in contatos:
        print(f"[{index}] {contato['nome']}")
        index = index + 1

while True:

    print ("\nMenu da Agenda:")
    print ("1. Adicionar contato.")
    print ("2. Visualizar lista de contatos.")
    print ("3. Editar contato.")
    print ("4. Remover contato como favorito.")
    print ("5. Visualizar contatos favoritos.")
    print ("6. Remover contato.")
    print ("7. Sair")

    escolha = int(input("Qual a sua escolha? "))
    
    if escolha == 1:
        namectt = input("\nQual o nome do contato que você deseja adicionar? ")
        telctt = input("\nQual o numero de telefone? ")
        emailctt = input("\nQual o email do contato? ")
        resposta_fav = input("\n Quer colocar na lista de Favoritos? (S/N) ")
        
        ctt = {"nome": namectt, "telefone": telctt, "email": emailctt}
        contatos.append(ctt)
               
        if resposta_fav.lower() == "s":
            favctt.append(ctt)
        
        
    
    if escolha == 2:
        print ("Seus contatos: \n{}".format(contatos))


    if escolha == 3:
        mostrarContatos(contatos)
        atualizar = int(input("Qual deseja atualizar? "))
        namectt = input("\nQual o nome do contato que você deseja adicionar? ")
        telctt = input("\nQual o numero de telefone? ")
        emailctt = input("\nQual o email do contato? ")
        resposta_fav = input("\n Quer colocar na lista de Favoritos? (S/N) ")

        ctt = {"nome": namectt, "telefone": telctt, "email": emailctt}

        if resposta_fav.lower() == "s":
            favctt.append(ctt)

        contatos[atualizar] = ctt

    if escolha == 4:
        mostrarContatos(favctt)
        remover = int(input("Qual deseja remover? "))
        del favctt[remover]


    if escolha == 5:
        mostrarContatos(favctt)

    if escolha == 6:
        mostrarContatos(contatos)
        remover = int(input("Qual deseja remover? "))

        if contatos[remover] in favctt:
            favctt.remove(contatos[remover])


        del contatos[remover]

    if escolha == 7:
        print('Programa finalizado')
        break

    