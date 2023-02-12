def py_str_up(word:str):
    """
    Функцию принимает на вход строку и возвращает ее со всеми заглавными буквами
    :param word: Строка
    :return: Строка
    """
    return word.upper()


def py_str_tit(word:str):
    """
    Функция делает заглавными первые буквы каждого слова в строке
    :param word: Строка или слово
    :return: Строка
    """
    return word.title().strip()
