class SistemaLogin:
    def __init__(self):
        self.usuarios = {}
        self.consultas = {}

    def cadastrar_usuario(self, username, password):
        if username in self.usuarios:
            print("Usuário já existe. Tente outro nome de usuário.")
        else:
            self.usuarios[username] = password
            self.consultas[username] = []  
            print("Usuário cadastrado com sucesso.")

    def login(self, username, password):
        if username not in self.usuarios or self.usuarios[username] != password:
            print("Credenciais inválidas. Tente novamente.")
            return False
        else:
            print("Login bem-sucedido! Bem-vindo,", username)
            return True

    def agendar_consulta(self, username, consulta):
        if username in self.consultas:
            self.consultas[username].append(consulta)
            print("Consulta agendada com sucesso para", username)
        else:
            print("Usuário não encontrado.")

    def consultar_agenda(self, username):
        if username in self.consultas:
            if self.consultas[username]:
                print(f"Consultas agendadas para {username}:")
                for consulta in self.consultas[username]:
                    print("-", consulta)
            else:
                print("Nenhuma consulta agendada para", username)
        else:
            print("Usuário não encontrado.")

    def cancelar_consulta(self, username, consulta):
        if username in self.consultas:
            if consulta in self.consultas[username]:
                self.consultas[username].remove(consulta)
                print("Consulta cancelada com sucesso para", username)
            else:
                print("Consulta não encontrada.")
        else:
            print("Usuário não encontrado.")


def main():
    sistema = SistemaLogin()

    while True:
        print("\nOpções:")
        print("1. Criar Conta")
        print("2. Login")
        print("3. Agendar Consulta")
        print("4. Consultar Agenda")
        print("5. Cancelar Consulta")
        print("6. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            username = input("Digite o nome de usuário: ")
            password = input("Digite a senha: ")
            sistema.cadastrar_usuario(username, password)
        elif choice == '2':
            username = input("Digite o nome de usuário: ")
            password = input("Digite a senha: ")
            if sistema.login(username, password):
                break
        elif choice == '3':
            username = input("Digite o nome de usuário: ")
            consulta = input("Digite os detalhes da consulta: ")
            sistema.agendar_consulta(username, consulta)
        elif choice == '4':
            username = input("Digite o nome de usuário: ")
            sistema.consultar_agenda(username)
        elif choice == '5':
            username = input("Digite o nome de usuário: ")
            consulta = input("Digite os detalhes da consulta a ser cancelada: ")
            sistema.cancelar_consulta(username, consulta)
        elif choice == '6':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
