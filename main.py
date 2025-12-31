import pyttsx3

# 1. Configuração do motor de voz
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)


# 2. Definição das Classes
class Paciente:
    def __init__(self, nome, data_nascimento, cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Consulta:
    def __init__(self, paciente, medico, consultorio):
        self.paciente = paciente
        self.medico = medico
        self.consultorio = consultorio
        self.status = "Aguardando"


# 3. Listas (Banco de Dados em memória)
fila_de_espera = []
atendidos = []  # Adicionada a lista que faltava aqui!


# 4. Funções do Sistema
def agendar_consulta():
    print("\n--- Cadastro de Paciente ---")
    nome = input("Nome do paciente: ")
    nascimento = input("Data de nascimento: ")
    cpf = input("CPF: ")

    # Criando o objeto com os dados digitados
    novo_paciente = Paciente(nome, nascimento, cpf)

    print("\n--- Detalhes da Consulta ---")
    medico = input("Nome do medico: ")
    sala = input("Número do Consultório: ")

    nova_consulta = Consulta(novo_paciente, medico, sala)

    fila_de_espera.append(nova_consulta)
    print(f"\n✅ Consulta de {nome} agendada com sucesso!")


def ver_lista():
    if not fila_de_espera:
        print("\n📭 A lista de espera está vazia.")
        return

    print("\n--- LISTA DE ESPERA ATUAL ---")
    for i, consulta in enumerate(fila_de_espera, 1):
        p = consulta.paciente
        print(f"{i}. Paciente: {p.nome} | Médico: {consulta.medico} | Sala: {consulta.consultorio}")


def chamar_proximo():
    if not fila_de_espera:
        print("\n⚠️ Não há ninguém na fila de espera!")
        return

    # Remove o primeiro da fila e move para atendidos
    consulta_atual = fila_de_espera.pop(0)
    atendidos.append(consulta_atual)

    p = consulta_atual.paciente

    print("\n" + "=" * 30)
    print(f"SALA: {consulta_atual.consultorio}")
    print(f"PACIENTE: {p.nome}")
    print("=" * 30)

    # Voz do sistema
    texto_chamada = f"Atenção: {p.nome}, compareça ao consultório {consulta_atual.consultorio}"
    engine.say(texto_chamada)
    engine.runAndWait()


def ver_atendidos():
    if not atendidos:
        print("\n📑 Nenhum atendimento realizado ainda.")
        return
    print("\n--- LISTA DE ATENDIDOS HOJE ---")
    for consulta in atendidos:
        p = consulta.paciente
        print(f"Paciente: {p.nome} | Médico: {consulta.medico} | CPF: {p.cpf}")


# 5. Menu Principal (Loop infinito)
while True:
    print("\n" + "=" * 20)
    print("SISTEMA DA CLÍNICA 🏥")
    print("1 - Agendar Consulta 📝")
    print("2 - Ver Lista de Espera 📋")
    print("3 - Chamar Próximo (Painel) 📺")
    print("4 - Ver Histórico de Atendidos 📑")
    print("0 - Sair ❌")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        agendar_consulta()
    elif opcao == "2":
        ver_lista()
    elif opcao == "3":
        chamar_proximo()
    elif opcao == "4":
        ver_atendidos()
    elif opcao == "0":
        print("Saindo... Até logo!")
        break
    else:
        print("Opção inválida, tente novamente.")