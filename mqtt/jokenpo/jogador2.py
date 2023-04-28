import inquirer
import paho.mqtt.publish as publish

BROKER = "10.21.160.16"
PORT = 1883

TOPIC_PLAYER2 = "jokenpo/player2"

questions = [
  inquirer.List('size',
                message="Jogador 2, faça sua jogada!",
                choices=['Pedra', 'Papel', 'Tesoura'],
            ),
]
slc = inquirer.prompt(questions)
jogada = slc['size']

publish.single(TOPIC_PLAYER2, jogada, hostname=BROKER, port=PORT)
print("Jogada enviada com sucesso!")