import AFD
from AFD import tipo_estado

#variaveis de controle:
control_loop = 's' #variavel de controle para o loop

def menu():
    print("Selecione o tipo de autômato:")
    print("1 - AFD")
    print("0 - Sair")
    resposta = int(input("Digite sua opção: "))
    return resposta

def requisitar_transicoes(alfabeto:list, estados:list):
    for i in range(len(estados)):
        transicoes = {}

        for j in range(len(alfabeto)):
            transicao = input(f"({estados[i]}, {alfabeto[j]}): ")
            while not transicao in estados:
                transicao = input(f"Transição inválida. Digite novamente \n({estados[i]}, {alfabeto[j]}): ")
            transicoes[alfabeto[j]] = transicao

        if estados[i] == estado_inicial:
            if estados[i] in estados_finais:
                AFD.cria_estado(estados[i], tipo_estado.INICIAL_FINAL, transicoes)
                continue
            AFD.cria_estado(estados[i], tipo_estado.INICIAL, transicoes)
            continue
        if estados[i] in estados_finais:
            AFD.cria_estado(estados[i], tipo_estado.FINAL, transicoes)
            continue
        AFD.cria_estado(estados[i], tipo_estado.COMUM, transicoes)

opcao = menu()
match opcao:
    case 0:
        print("Saindo...")

    case 1:    
        tipo_entrada = int(input("Digite o tipo de entrada (1 - arquivo planilha/tabela, 2 - Teclado): "))

        if tipo_entrada == 1:
            # leitura via arquivo de planilha/tabela
            pass #será futuramente implementada
            
        elif tipo_entrada == 2:
            alfabeto = input("Digite o alfabeto (ex: a b c): ").split()
            estados = input("Digite os estados (ex: q0 q1 q2): ").split()
            estado_inicial = input("Digite qual deles é o estado inicial: ")
            estados_finais = input("Digite quais são os estados finais (ex: q1 q2): ").split()

            AFD = AFD.AFD(alfabeto)
            print("Envie as transições enviando o estado de destino para cada associação (estado, simbolo):")
            a = requisitar_transicoes(alfabeto, estados)
            print(a)
        print("AFD criado com sucesso!")
        while control_loop == 's' or control_loop == 'S':
            cadeia = input("Digite a cadeia a ser lida: ")
            resultado, estado_final = AFD.leitura(cadeia)

            if resultado:
                print(f"A cadeia '{cadeia}' é aceita pelo AFD. Estado final: {estado_final.id}")
            else:
                print(f"A cadeia '{cadeia}' não é aceita pelo AFD. Estado final: {estado_final.id}")
            control_loop = input("Deseja testar outra cadeia? (S/N): ")