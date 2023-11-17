from time import sleep

print("****************************************")
print("|| BEM VINDO A SUA LISTA DE TAREFAS! ||")
print("****************************************")

lista_de_tarefas = []

def adicionar(tarefa):
    lista_de_tarefas.append(tarefa)
    print("Nova tarefa adicionada: " " " f"{tarefa}")
    
def listar_tarefas():
    if not lista_de_tarefas:
        print('Nenhuma tarefa a pendente')
    else:
        for i, tarefa in enumerate(lista_de_tarefas):
            print(f'{i + 1}. {tarefa}')
            
def tarefa_concluida():
    if not lista_de_tarefas:
        print("Você não possui tarefas.")
    else:
        concluida = int(input("Digite o número da tarefa que queira marcar como concluída: "))
        if concluida <= len(lista_de_tarefas):
            tarefa_excluida = lista_de_tarefas.pop(concluida - 1)
            print(f'Tarefa {concluida} marcada como concluída.')
            return tarefa
        else:
            print('Número de tarefa inválido.')
            
while True:
   print("---------------------------------------- \n O que você gostaria de fazer? \n---------------------------------------- \n1. Adicionar nova tarefa \n2. Marcar tarefa como concluída \n3. Listar tarefas pendentes \n4. Sair \n----------------------------------------")
   
   opcao = input("Escolha uma opção: ")
   if opcao == '1':
        tarefa = input("Digite a tarefa que deseja adicionar: ")
        adicionar(tarefa)
   elif opcao == "2":
       tarefa_concluida()
   elif opcao == "3":
        listar_tarefas()
   elif opcao == "4":
       print("Saindo...")
       sleep(1)
       break
   else:
        print("Digite um número válido")

   sleep(1)