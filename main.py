import random

def choose_word(word_list):
    return random.choice(word_list)

def specifik_word(word, saved_letters):
     result = ""
     for i in word:
         if i in saved_letters:
             result += i + ""
         else:
             result += "_"

def play_game():
    words = ["Максим", "Орест", "Олег"]
    selected_word = choose_word(words)
    selected_word_len = len(selected_word)
    saved_letters = set()

    print("Привіт! Це гра 'Відгадай слово'")
    print("Cлово має" + str(selected_word_len) + "літери")
