import pickle

M_Candidatos = {}
M_Presidente = {}
M_Eleitores = {}
voto = []
votos_Registrados = {}
voto_final = []
nova_votacao = "S"
resultado_apuracao = {}
UF = ""
eleitores_uf = {}


def menu():
    print("\nMenu\n")
    print("1 - Ler o arquivo de candidatos")
    print("2 - Ler o arquivo de eleitores")
    print("3 - Iniciar votação")
    print("4 - Apurar votos")
    print("5 - Mostrar resultados")
    print("6 - Fechar programa\n")


def votar_federal(Dic_Candidatos):
    print(Dic_Candidatos)

    voto_F = input("Informe o voto para Deputado Federal: ")

    if voto_F.upper() == "B":
        print(f"Votar em branco?")
        confirmacao = input("Confirma (S ou N)? ")

        if confirmacao.upper() == 'S':
            return "B"
        else:
            return False
    else:
        while len(voto_F) != 4:
            print("O número do candidato deve conter 4 dígitos.")
            voto_F = input("Informe o voto para Deputado Federal: ")

        if voto_F not in Dic_Candidatos.keys():
            print("Candidato não cadastrado em seu estado.")
            confirmacao = input("Deseja anular seu voto (S ou N)? ")

            if confirmacao.upper() != 'S':
                return False  # False -> indica para quem chamou algum erro interno
            else:
                # Mensagem de indicação de voto anulado
                return "N"
        else:
            print(f"Candidato {Dic_Candidatos[voto_F][0]} | {Dic_Candidatos[voto_F][1]}")
            confirmacao = input("Confirma (S ou N)? ")

            if confirmacao.upper() == 'S':
                return voto_F
            else:
                return False


def votar_estadual(Dic_Candidatos):
    print(Dic_Candidatos)

    voto_E = input("Informe o voto para Deputado Estadual: ")

    if voto_E.upper() == "B":
        print(f"Votar em branco?")
        confirmacao = input("Confirma (S ou N)? ")

        if confirmacao.upper() == 'S':
            return "B"
        else:
            return False
    else:
        while len(voto_E) != 5:
            print("O número do candidato deve conter 5 dígitos.")
            voto_E = input("Informe o voto para Deputado Estadual: ")

        if voto_E not in Dic_Candidatos.keys():
            print("Candidato não cadastrado em seu estado.")
            confirmacao = input("Deseja anular seu voto (S ou N)? ")

            if confirmacao.upper() != 'S':
                return False  # False -> indica para quem chamou algum erro interno
            else:
                # Mensagem de indicação de voto anulado
                return "N"
        else:
            print(f"Candidato {Dic_Candidatos[voto_E][0]} | {Dic_Candidatos[voto_E][1]}")
            confirmacao = input("Confirma (S ou N)? ")

            if confirmacao.upper() == 'S':
                return voto_E
            else:
                return False


def votar_senador(Dic_Candidatos):
    print(Dic_Candidatos)

    voto_S = input("Informe o voto para Senador: ")

    if voto_S.upper() == "B":
        print(f"Votar em branco?")
        confirmacao = input("Confirma (S ou N)? ")

        if confirmacao.upper() == 'S':
            return "B"
        else:
            return False
    else:
        while len(voto_S) != 3:
            print("O número do candidato deve conter 3 dígitos.")
            voto_S = input("Informe o voto para Senador: ")

        if voto_S not in Dic_Candidatos.keys():
            print("Candidato não cadastrado em seu estado.")
            confirmacao = input("Deseja anular seu voto (S ou N)? ")

            if confirmacao.upper() != 'S':
                return False  # False -> indica para quem chamou algum erro interno
            else:
                # Mensagem de indicação de voto anulado
                return "N"
        else:
            print(f"Candidato {Dic_Candidatos[voto_S][0]} | {Dic_Candidatos[voto_S][1]}")
            confirmacao = input("Confirma (S ou N)? ")

            if confirmacao.upper() == 'S':
                return voto_S
            else:
                return False


def votar_governador(Dic_Candidatos):
    print(Dic_Candidatos)

    voto_G = input("Informe o voto para Governador: ")

    if voto_G.upper() == "B":
        print(f"Votar em branco?")
        confirmacao = input("Confirma (S ou N)? ")

        if confirmacao.upper() == 'S':
            return "B"
        else:
            return False
    else:
        while len(voto_G) != 2:
            print("O número do candidato deve conter 2 dígitos.")
            voto_G = input("Informe o voto para governador: ")

        if voto_G not in Dic_Candidatos.keys():
            print("Candidato não cadastrado em seu estado.")
            confirmacao = input("Deseja anular seu voto (S ou N)? ")

            if confirmacao.upper() != 'S':
                return False  # False -> indica para quem chamou algum erro interno
            else:
                # Mensagem de indicação de voto anulado
                return "N"
        else:
            print(f"Candidato {Dic_Candidatos[voto_G][0]} | {Dic_Candidatos[voto_G][1]}")
            confirmacao = input("Confirma (S ou N)? ")

            if confirmacao.upper() == 'S':
                return voto_G
            else:
                return False


def votar_presidente(M_Presidente):
    print(M_Presidente)

    voto_P = input("Informe o voto para Presidente: ")

    if voto_P.upper() == "B":
        print(f"Votar em branco?")
        confirmacao = input("Confirma (S ou N)? ")

        if confirmacao.upper() == 'S':
            return "B"
        else:
            return False
    else:
        while len(voto_P) != 2:
            print("O número do candidato deve conter 2 dígitos.")
            voto_P = input("Informe o voto para Presidente: ")

        if voto_P not in M_Presidente.keys():
            print("Candidato não cadastrado.")
            confirmacao = input("Deseja anular seu voto (S ou N)? ")

            if confirmacao.upper() != 'S':
                return False
            else:
                # Mensagem de indicação de voto anulado
                return "N"
        else:
            print(f"Candidato {M_Presidente[voto_P][0]} | {M_Presidente[voto_P][1]}")
            confirmacao = input("Confirma (S ou N)? ")

            if confirmacao.upper() == 'S':
                return voto_P
            else:
                return False


def salvar_votos_arquivo(votos_Registrados):
    with open("votos.pkl", "wb") as arquivo:
        pickle.dump(votos_Registrados, arquivo)


def apurar_votos(votos_final):
    apuracao = {
        "F": {},
        "E": {},
        "S": {},
        "G": {},
        "P": {}
    }

    for votos in votos_final:
        for cargo, voto in votos.items():
            if voto == "B":
                apuracao[cargo]["Branco"] = apuracao[cargo].get("Branco", 0) + 1
            elif voto == "N":
                apuracao[cargo]["Nulo"] = apuracao[cargo].get("Nulo", 0) + 1
            else:
                apuracao[cargo][voto] = apuracao[cargo].get(voto, 0) + 1
    print(apuracao)
    return apuracao

def gerar_boletim_urna(resultado_apuracao, total_eleitores):
    # Cálculo dos totais
    total_votos_nominais = len(resultado_apuracao)  # sum([sum(opcoes.values()) for opcoes in resultado_apuracao.values() if isinstance(opcoes, dict)])

    # Contagem de brancos e nulos
    brancos = resultado_apuracao.get('Branco', 0)
    nulos = resultado_apuracao.get('Nulo', 0)

    # Criação e escrita do Boletim de Urna em um arquivo
    with open("Boletim_de_Urna.txt", "w") as bu_file:
        bu_file.write("Apuração dos votos:\n")
        bu_file.write(f"Eleitores Aptos: {total_eleitores}\n")
        bu_file.write(f"Total de Votos Nominais: {total_votos_nominais}\n")
        bu_file.write(f"Brancos: {brancos}\n")
        bu_file.write(f"Nulos: {nulos}\n\n")
       # Exibição dos resultados por cargo e candidato
        for cargo, resultados in resultado_apuracao.items():
            # if cargo not in ['Branco', 'Nulo']:
            bu_file.write(f"Cargo: {cargo}\n")
            for candidato, votos in resultados.items():
                if candidato not in ['Branco', 'Nulo'] and cargo != "P":
                    total_votos_candidato = sum(resultados.values())
                    percentual_votos = (votos / total_votos_candidato) * 100
                    bu_file.write(f"Candidato: {M_Candidatos[UF][candidato][0]} | Cargo: {M_Candidatos[UF][candidato][3]} | Estado: {M_Candidatos[UF][candidato][2]} | Votos: {votos} ({percentual_votos:.2f}%)\n")
                elif cargo == "P":
                    total_votos_candidato = sum(resultados.values())
                    percentual_votos = (votos / total_votos_candidato) * 100
                    bu_file.write(f"Candidato: {M_Presidente[candidato][0]} | Cargo: {M_Presidente[candidato][2]} | Votos: {votos} ({percentual_votos:.2f}%)\n")

print("\nBem-vindo à central de votação!\n")
menu()
opcao = int(input("Digite a opção desejada: "))

while opcao != 6:

    if opcao < 1 or opcao > 6:
        print("\nEscolha uma opção entre 1 e 6!\n")
    else:
        if opcao == 1:
            cand = input("\nInforme a localização dos dados dos candidatos: ")
            arq = open(cand, "r")
            texto = arq.read()
            print(texto)
            arq.close()

            if texto:
                for linha in texto.split('\n'):
                    dados = linha.strip().split(',')

                    if len(dados) >= 5:
                        nome = dados[0]
                        numero = dados[1]
                        partido = dados[2]
                        estado = dados[3]
                        cargo = dados[4]

                        if estado == "-":
                            M_Presidente[numero] = [nome, partido, cargo]
                        else:
                            if estado not in M_Candidatos.keys():
                                M_Candidatos[estado] = {}

                            M_Candidatos[estado][numero] = [nome, partido, estado, cargo]

                print(M_Candidatos)

        elif opcao == 2:
            eleit = input("Informe a localização dos dados dos eleitores: ")
            arq = open(eleit, "r")
            texto = arq.read()
            print(texto)
            arq.close()

            if texto:
                for linha in texto.split('\n'):
                    dados = linha.strip().split(',')

                    if len(dados) >= 5:
                        nome = dados[0]
                        RG = ''.join(filter(str.isdigit, dados[1]))
                        titulo = dados[2].strip()
                        cidade = dados[3]
                        estado = dados[4]

                        M_Eleitores[titulo] = {
                            'Nome': nome,
                            'RG': RG,
                            'Título': titulo,
                            'Cidade': cidade,
                            'Estado': estado
                        }

        elif opcao == 3:
            votos_Registrados = {}
            if not M_Candidatos or not M_Eleitores:
                print("Você deve ler os arquivos de candidatos (opção 1) e eleitores (opção 2) primeiro.")
            else:
                UF = input("UF onde está localizada a urna: ").upper()
                candidatos_uf = M_Candidatos[UF]

                while nova_votacao.upper() == "S":
                    votos_Registrados = {}  # Inicialize um novo dicionário para cada iteração
                    titulo = input("Informe o Título de Eleitor: ")

                    while titulo not in M_Eleitores:
                        print("Título não encontrado!")
                        titulo = input("Informe o Título de Eleitor: ")

                    eleitor_uf = M_Eleitores[titulo]['Estado'].strip()
                    if eleitor_uf != UF.strip():
                        print("Título não cadastrado nesse estado!")
                        continue  # Reinicie o loop, peça um novo Título

                    print(f"Eleitor: {M_Eleitores[titulo]['Nome']}")
                    print(f"Estado: {eleitor_uf}\n")

                    voto_federal = False
                    while not voto_federal:
                        voto_federal = votar_federal(candidatos_uf)
                        if not voto_federal:
                            voto_federal = votar_federal(candidatos_uf)
                        else:
                            votos_Registrados["F"] = voto_federal

                    voto_estadual = False
                    while not voto_estadual:
                        voto_estadual = votar_estadual(candidatos_uf)
                        if not voto_estadual:
                            voto_estadual = votar_estadual(candidatos_uf)
                        else:
                            votos_Registrados["E"] = voto_estadual

                    voto_senador = False
                    while not voto_senador:
                        voto_senador = votar_senador(candidatos_uf)
                        if not voto_senador:
                            voto_senador = votar_senador(candidatos_uf)
                        else:
                             votos_Registrados["S"] = voto_senador

                    voto_governador = False
                    while not voto_governador:
                        voto_governador = votar_governador(candidatos_uf)
                        if not voto_governador:
                            voto_governador = votar_governador(candidatos_uf)
                        else:
                            votos_Registrados["G"] = voto_governador

                    voto_presidente = False
                    while not voto_presidente:
                        voto_presidente = votar_presidente(M_Presidente)
                        if not voto_presidente:
                            voto_presidente = votar_presidente(M_Presidente)
                        else:
                            votos_Registrados["P"] = voto_presidente

                    salvar_votos_arquivo(votos_Registrados)
                    voto_final.append(votos_Registrados)
                    print("Voto registrado com sucesso\n")
                    nova_votacao = input("Deseja realizar uma nova votação (S ou N)? ").upper()

        elif opcao == 4:
            if not voto_final:
                print("Nenhuma votação realizada ainda.")
            else:
                resultado_apuracao = apurar_votos(voto_final)
                print("\nResultado da Apuração:")
                for cargo, resultados in resultado_apuracao.items():
                    print(f"\nCargo: {cargo}")
                    for opcao, votos in resultados.items():
                        print(f"{opcao}: {votos} votos")

        elif opcao == 5:
            total_eleitores = len(M_Eleitores)
            print("Gerando Boletim de Urna!")
            gerar_boletim_urna(resultado_apuracao, total_eleitores)

            BU = "Boletim_de_Urna.txt"
            arq = open(BU, "r")
            texto = arq.read()
            print(texto)
            arq.close()

        menu()
        opcao = int(input("Digite a opção desejada: "))

    if opcao == 6:
        print("Eleição encerrada")

# EXTRA _ GERAR GRÁFICOS

from pylab import *

def gerar_grafico_cargo(cargo, resultado_apuracao):
    votos_candidatos = resultado_apuracao.get(cargo, {})

    if not votos_candidatos:
        print(f"Não há resultados para {cargo}.")
        return

    candidatos = list(votos_candidatos.keys())
    votos = list(votos_candidatos.values())

    bar(candidatos, votos, color='blue')
    xlabel(f'Candidatos para {cargo}')
    ylabel('Número de Votos')
    title(f'Resultado da Votação para {cargo}')
    show()

cargos_para_gerar = ['F', 'E', 'S', 'G', 'P']  # Cargos desejados

for cargo in cargos_para_gerar:
    gerar_grafico_cargo(cargo, resultado_apuracao)