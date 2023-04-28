import paho.mqtt.client as mqtt
import json

BROKER = "10.21.160.16"
PORT = 1883

TOPIC_PLAYER1 = "jokenpo/player1"
TOPIC_PLAYER2 = "jokenpo/player2"

jogada1 = None


def play_game(jogada1, jogada2):
    if jogada1 == jogada2:
        return "Empate"
    elif jogada1 == "Pedra":
        if jogada2 == "Tesoura":
            return "Jogador 1 venceu!"
        else:
            return "Jogador 2 venceu!"
    elif jogada1 == "Pedra":
        if jogada2 == "Papel":
            return "Jogador 2 venceu!"
        else:
            return "Jogador 1 venceu!"
    elif jogada1 == "Papel":
        if jogada2 == "Pedra":
            return "Jogador 1 venceu!"
        else:
            return "Jogador 2 venceu!"
    elif jogada1 == "Tesoura":
        if jogada2 == "Papel":
            return "Jogador 1 venceu!"
        else:
            return "Jogador 2 venceu!"


def on_message(client, userdata, message):
    global jogada1
    if message.topic == TOPIC_PLAYER1:
        jogada1 = message.payload.decode()
        print("Jogador 1 jogou!")
    elif message.topic == TOPIC_PLAYER2:
        jogada2 = message.payload.decode()
        print("Jogador 2 jogou!")
        if jogada1 is not None and jogada2 is not None:
            resultado = play_game(jogada1, jogada2)
            print("\nJogador 1 jogou {} e Jogador 2 jogou {}".format(jogada1, jogada2))
            print(resultado)
            print()
            print("<------------------------------------------------------------->")
            print()


client = mqtt.Client()
client.connect(BROKER, PORT)
client.subscribe(TOPIC_PLAYER1)
client.subscribe(TOPIC_PLAYER2)

client.on_message = on_message

client.loop_forever()
