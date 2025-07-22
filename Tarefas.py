tarefas = []
completas = []

while True:
    print("\nMenu do Gerenciador de lista de Tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar Tarefas")
    print("4. Completar Tarefa")
    print("5. Deletar Tarefas completadas")
    print("6. Sair")

    escolha = input("\n Digite a sua escolha: ")

    if escolha == "1":
        addname = input("\n Escolha a tarefa que desejas adicionar: ")
        tarefas.append(addname)
    
    if escolha == "2":
        print ("Suas tarefas : \n {}".format(tarefas))

    if escolha == "3":
        print (tarefas)
        atttarefa = input("Qual deseja atualizar? ")
        attarefa = input("Por qual ?")
        indice = tarefas.index(atttarefa)
        tarefas[indice] = attarefa

    if escolha == "4": 
        print (tarefas)
        completadas = input("Qual tarefa você ja completou? ")
        indice = tarefas.index(completadas)
        completas.append(indice)

    if escolha == "5":
        for i in sorted(completas, reverse=True):
         del tarefas[i]
         completas.clear()


    if escolha == "6":
        break

print ("Programa finalizado.")

  
   
