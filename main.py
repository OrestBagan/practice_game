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


attempts = 6

    while attempts > 0:
        print("\nСлово: " + specifik_word(selected_word, saved_letters))
        print(f"Залишилось спроб: {attempts}")

        guess = input("Введіть букву: ").strip()
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
            print(f"Вітаємо! Ви відгадали слово: {selected_word}")
            break
    else:
        print(f"На жаль, ви програли. Слово було: {selected_word}")

if __name__ == "__main__":
    play_game()
