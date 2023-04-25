import random
import requests
from logic import *


def play_nutella():
    print("Welcome to the {} Nutella {} mode!".format(color['yellowz'], color['r']))
    print("You have 10 lives and hints available.\n")
    print("Hint: It's a computer language!")

    word_list = ["python", "java", "csharp", "go", "javascript", "php", "mysql", "rust", "ruby", "kotlin"]
    word = word_list[random.randint(0, len(word_list) - 1)]

    hint_nutella = "Hint: It's a back-end language!"

    play_game(word, 9999, 6, hint_nutella)


def play_cafe_com_leite():
    print("Welcome to {} Café com Leite {} mode! You have 30 seconds to guess a computer-related word."
          .format(color['bluez'], color['r']))
    hint_cafe = "Hint: It's a computer hardware component."

    word_list = ["mouse", "keyboard", "monitor", "printer", "scanner", "speaker", "router", "server", "cpu", "laptop",
                 "ram", "motherboard", "joystick", "gamepad", "microphone", "headphones", "webcam"]
    word = word_list[random.randint(0, len(word_list) - 1)]

    play_game(word, 30, 6, hint_cafe)


def play_raiz():
    print("Welcome to the {} Raiz {} mode!".format(color['cyanz'], color['r']))
    print("You have 20 seconds to guess the word.\n")

    word = str
    definition = str
    while True:
        try:
            url = "https://random-word-api.herokuapp.com/word?number=1"
            response = requests.get(url)
            word = response.json()[0]

            url2 = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
            response2 = requests.get(url2)
            definition = response2.json()[0]['meanings'][0]['definitions'][0]['definition']
            break
        except KeyError:
            continue

    play_game(word, 20, 6, definition)