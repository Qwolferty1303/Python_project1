meme_dict = {
    "ЛОЛ": "очень смешно",
    "КРИНЖ": "что-то странное, стыдное",
    "РОФЛ": "шутка",
    "ЩИЩ": "одобрение или восторг",
    "КРИПОВЫЙ": "страшный, пугающий",
    "АГРИТЬСЯ": "злиться",
    "ШАРИТЬ": "Знат что-то, разбираться в чем-то",
}


def add_word(word, meaning):
    meme_dict[word] = meaning
    print('Слово "', word, '" и его значение успешно добавлены в словарь!')


def explainer():
    print("Добро пожаловать в программу объяснялку современных слов!")

    while True:
        word = input("Введите непонятное слово: ")
        word_upper = word.upper()

        if word_upper == "СТОП":
            print("Программа завершена.")
            break

        if word_upper in meme_dict:
            print('Значение слова "', word_upper, '" - ', meme_dict[word_upper])
        else:
            print('Слово "', word_upper, '" не найдено в словаре. Чтобы добавить его, введите "Добавить".')
            action = input("Введите действие (Добавить): ")

            if action == "Добавить":
                value = input("Введите значение для слова " + word_upper + ": ")
                add_word(word_upper, value)
            else:
                print("Неправильное действие. Попробуйте еще раз.")


explainer()
