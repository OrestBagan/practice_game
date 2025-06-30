import random
import time
import threading
from db import db

user_input = None

def choose_word(word_list):
    return random.choice(word_list)

def specifik_word(word, saved_letters):
    result = ""
    for i in word:
        if i in saved_letters:
            result += i + " "
        else:
            result += "_ "
    return result.strip()

# Функція для окремого потоку — чекає на введення
def get_input():
    global user_input
    user_input = input("Введіть букву: ").strip()

def play_game():
    global user_input
    words = db()
    selected_word = choose_word(words)
    selected_word_len = len(selected_word)
    saved_letters = set()

    print("Привіт! Це гра 'Відгадай слово'")
    print(f"Cлово має {selected_word_len} літери")
    print("У вас є 30 секунд, щоб вгадати слово.")

    attempts = 6
    end_time = time.time() + 30  # 30 секунд на гру

    while attempts > 0 and time.time() < end_time:
        print("\nСлово:", specifik_word(selected_word, saved_letters))
        print(f"Залишилось спроб: {attempts}")
        print(f"Залишилось часу: {int(end_time - time.time())} сек.")

        user_input = None
        input_thread = threading.Thread(target=get_input)
        input_thread.start()

        # Чекаємо максимум 30 сек або менше
        remaining = end_time - time.time()
        input_thread.join(timeout=remaining)

        if user_input is None:
            print("\n⏰ Час вийшов! Ви не встигли ввести букву.")
            break

        guess = user_input.lower()

        if len(guess) != 1:
            print("Введіть лише одну букву!")
            continue

        if guess in saved_letters:
            print("Ви вже називали цю букву!")
            continue

        saved_letters.add(guess)

        if guess not in selected_word:
            attempts -= 1
            print("Неправильно!")
        else:
            print("Правильно!")

        if all(letter in saved_letters for letter in selected_word):
            print(f"\n🎉 Вітаємо! Ви відгадали слово: {selected_word}")
            return

    print(f"\n❌ Гру завершено. Слово було: {selected_word}")

if __name__ == "__main__":
    play_game()
