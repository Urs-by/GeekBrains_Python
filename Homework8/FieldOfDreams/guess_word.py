import coding_table

with open('q_and_a.txt', encoding="utf8") as qa:
    data = qa.readlines()
print(data[0])
# декоодируем ответ из файла
get_answer = data[1].split(" ")
answer = ''
for i in range(1, len(get_answer) - 1):
    answer = answer + coding_table.decoding(int(get_answer[i]))
# отображаем слово в виде ***
coding_word = "*" * len(answer)
print(coding_word)

count = 0
# count -  счетчик попыток
while "*" in coding_word:
    user_letter = input("Введите букву: ")
    list_coding_word = list(coding_word)
    if user_letter not in answer:
        print("Такой буквы нет в слове!")
    else:
        count += 1
        print("Есть такая буква!")
        for i in range(len(answer)):
            if user_letter == answer[i]:
                list_coding_word[i] = user_letter
    # переписываем зашифрованное слово с учетом новых букв
    coding_word = ''
    for i in list_coding_word:
        coding_word = coding_word + str(i)
    print(str(coding_word))

print(f"Вы отгадали слово за {count} ходов")