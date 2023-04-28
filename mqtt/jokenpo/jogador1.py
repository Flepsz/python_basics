import inquirer
import paho.mqtt.publish as publish

BROKER = "10.21.160.16"
PORT = 1883

TOPIC_PLAYER1 = "jokenpo/player1"

questions = [
    inquirer.List('size',
                  message="Jogador 1, faça sua jogada!",
                  choices=['Pedra', 'Papel', 'Tesoura'],
                  ),
]
slc = inquirer.prompt(questions)
jogada = slc['size']

publish.single(TOPIC_PLAYER1, jogada, hostname=BROKER, port=PORT)
print("Jogada enviada com sucesso!")

