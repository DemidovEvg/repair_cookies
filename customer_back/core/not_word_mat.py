def search_word_mat(my_str: str):
    word_mat_source = []
    # откроем файл словаря матов и считаем его содержимое в список
    with open("./core/word_mat_file.py", "r") as file_word:
        print(file_word)
        for line in file_word:
            # удалим заключительный символ перехода строки
            current_word = line[:-1]
            # добавим элемент в конец списка
            word_mat_source.append(current_word)

    my_str = my_str.lower()
    for str_mat_one in word_mat_source:
        if str_mat_one in my_str:
            return True
    return False
