import random

jogador_pontos = 0
computador_pontos = 0

opcoes = ["pedra", "papel", "tesoura"]


while True:
    escolha_jogador = input("Escolha (Pedra)/(Papel)/(Tesoura) ou Q para sair.").lower()

    if escolha_jogador == 'q':
        break
    
    if escolha_jogador not in opcoes:
        continue

    escolha_computador = random.randint(0, 2)
    #0: Pedra, 1: Papel, 2: Tesoura
    computador_opcao = opcoes[escolha_computador]

    print("O computador escolheu " + computador_opcao)

    if escolha_jogador == computador_opcao:
        print("Empate!")
    elif escolha_jogador == "pedra" and computador_opcao == "tesoura":
        print("Você ganhou!")
        jogador_pontos = jogador_pontos + 1

    elif escolha_jogador == "papel" and computador_opcao == "pedra":
        print("Você ganhou!")
        jogador_pontos = jogador_pontos + 1

    elif escolha_jogador == "tesoura" and computador_opcao == "papel":
        print("Você ganhou!")
        jogador_pontos = jogador_pontos + 1

    else:
        print("Você Perdeu!")
        computador_pontos = computador_pontos + 1

print("Sua Pontuacao: " + str(jogador_pontos))
print("Pontuacao do computador: " + str(computador_pontos))

if computador_pontos < jogador_pontos:
    print("Voce Venceu!!!!")
elif computador_pontos == jogador_pontos:
    print("Empate.")
else:
    print("Voce Perdeu.")
