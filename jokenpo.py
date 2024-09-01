from random import randint
choices = ["pedra", "papel", "tesoura"]
print("Pedra, Papel ou Tesoura.")
print("")
# Escolha do player
while True:
    playerChoice = str(input("Eu escolho: ")).lower()
    if playerChoice in choices:
        break
# Escolha do bot
botChoice = choices[randint(0,2)]
# Mostrar escolhas
def showChoices():
    print("")
    print(f'Player escolheu {playerChoice}')
    print(f'Bot escolheu {botChoice}')
    print("")
    result()
    print("")
def result():
    # Pedra e tesoura
    if playerChoice == choices[0] and botChoice == choices[2]:
        print("Player venceu a partida!")
    elif playerChoice == choices[2] and botChoice == choices[0]:
        print("Bot venceu a partida!")
    # Papel e pedra
    if playerChoice == choices[1] and botChoice == choices[0]:
        print("Player venceu a partida!")
    elif playerChoice == choices[0] and botChoice == choices[1]:
        print("Bot venceu a partida!")
    # Tesoura e papel
    if playerChoice == choices[2] and botChoice == choices[1]:
        print("Player venceu a partida!")
    elif playerChoice == choices[1] and botChoice == choices[2]:
        print("Bot venceu a partida!")
    elif playerChoice == botChoice:
        print("Empate!")
showChoices()
