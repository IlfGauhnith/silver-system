from process import Process
from queue import Queue

ready = {1: Queue(), 2: Queue(), 3: Queue(), 4: Queue()}
preemption_time = 5


def create_process(name, priority, bound_type):
    process = Process(name, priority, bound_type)
    ready[process.priority].put(process)


if __name__ == '__main__':
    print("Bem-vindo ao simulador de processos.")
    menu_input = ''

    while menu_input != 'exit':
        menu_input = input("Digite um comando: ")
        command = menu_input.split()

        if command[0] == "CRIAR":
            create_process(command[1], int(command[2]), command[3])
            print("Processo " + str(command[1]) + " criado e alocado com sucesso.")

        elif command[0] == "MOSTRAR":
            if len(command) == 1:
                for key in ready:
                    msg = "Fila " + str(key) + "-> "
                    for process in ready[key].queue:
                        msg = msg + str(process)
                    msg = msg + "\n"
                    print(msg)

            elif len(command) == 2:
                id = int(command[1])
                print([str(process) for process in ready.get(process.priority).queue if process.id == id])

            else:
                print("Digite um comando válido.")

        elif command[0] == "SET":
            if command[1] == "PREEMPCAO":
                preemption_time = int(command[2])
            else:
                print("Digite um comando válido.")

        else:
            print("Digite um comando válido.")

        print()
