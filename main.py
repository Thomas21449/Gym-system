from gym_manager import GymManager
from facial_recognition import FacialRecognition
from cactous_controller import CactousController

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada inválida. Digite um número.")

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Digite um número.")

def confirmar_acao(mensagem):
    """
    Solicita confirmação do usuário para uma ação.
    :param mensagem: Mensagem de confirmação
    :return: True se o usuário confirmar, False caso contrário
    """
    resposta = input(f"{mensagem} (s/n): ").strip().lower()
    return resposta == "s"

def verificar_esc():
    """
    Verifica se o usuário digitou 'ESC' para voltar ao menu principal.
    :return: True se o usuário digitou 'ESC', False caso contrário
    """
    resposta = input("\nPressione ENTER para continuar ou digite 'ESC' para voltar ao menu principal: ").strip().lower()
    return resposta == "esc"

def main():
    gm = GymManager()
    fr = FacialRecognition()
    catraca = CactousController()

    while True:
        print("\n--- Sistema de Gestão de Academia ---")
        print("1. Cadastrar Aluno")
        print("2. Registrar Venda")
        print("3. Verificar Acesso Facial e Liberar Catraca")
        print("4. Adicionar Produto")
        print("5. Listar Produtos")
        print("6. Listar Alunos")
        print("7. Sair")
        print("\nDigite 'ESC' a qualquer momento para voltar ao menu principal.")

        choice = input("Escolha uma opção: ")

        if choice.lower() == "esc":
            print("\nVoltando ao menu principal...")
            continue

        if choice == "1":
            name = input("Nome: ")
            email = input("Email: ")
            plan = input("Plano (Mensal/Semestral/Anual): ")
            access_frequency = input("Frequência de Acesso (2x por semana/3x por semana/Diário): ")
            if confirmar_acao("Confirmar cadastro do aluno?"):
                member_id = gm.add_member(name, email, plan, access_frequency)
                fr.capture_face(member_id)
                print(f"Aluno cadastrado com ID: {member_id}")
            else:
                print("Cadastro cancelado.")

        elif choice == "2":
            product_id = get_int_input("ID do Produto: ")
            member_id = get_int_input("ID do Aluno: ")
            quantity = get_int_input("Quantidade: ")
            payment_method = input("Método de Pagamento (Cartão/PIX/Dinheiro): ")
            if confirmar_acao("Confirmar venda?"):
                if gm.sell_product(member_id, product_id, quantity, payment_method):
                    print("Venda registrada!")
                else:
                    print("Estoque insuficiente.")
            else:
                print("Venda cancelada.")

        elif choice == "3":
            member_id = get_int_input("ID do Aluno: ")
            if fr.verify_face(member_id):
                if gm.liberar_catraca(member_id):
                    print("Acesso liberado!")
                    if catraca.liberar_catraca():
                        print("Catraca liberada com sucesso!")
                else:
                    print("Limite de acessos atingido.")
            else:
                print("Acesso negado.")

        elif choice == "4":
            name = input("Nome do Produto: ")
            price = get_float_input("Preço do Produto: ")
            stock = get_int_input("Quantidade em Estoque: ")
            if confirmar_acao("Confirmar adição do produto?"):
                gm.add_product(name, price, stock)
            else:
                print("Adição de produto cancelada.")

        elif choice == "5":
            gm.list_products()

        elif choice == "6":
            print("\n--- Listar Alunos ---")
            print("1. Listar todos os alunos")
            print("2. Listar apenas alunos ativos")
            print("3. Listar apenas alunos inativos")
            print("4. Buscar aluno por ID")
            print("5. Buscar aluno por nome")
            list_choice = input("Escolha uma opção: ")

            if list_choice.lower() == "esc":
                print("\nVoltando ao menu principal...")
                continue

            if list_choice == "1":
                gm.list_members(filter_type="todos")
            elif list_choice == "2":
                gm.list_members(filter_type="ativos")
            elif list_choice == "3":
                gm.list_members(filter_type="inativos")
            elif list_choice == "4":
                member_id = get_int_input("Digite o ID do aluno: ")
                gm.list_members(filter_type="especifico", member_id=member_id)
            elif list_choice == "5":
                name = input("Digite o nome do aluno: ")
                gm.list_members(filter_type="especifico", name=name)
            else:
                print("Opção inválida.")

        elif choice == "7":
            if confirmar_acao("Deseja realmente sair?"):
                print("Saindo...")
                break
            else:
                print("Retornando ao menu principal.")

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()