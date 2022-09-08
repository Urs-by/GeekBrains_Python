import coding_table

question = input("Введите вопрос: ")
answer = input("Введите ответ: ")
answer = answer.lower()

coding_answer = ''
for i in answer:
    new_letter = coding_table.coding(i)
    coding_answer = coding_answer + str(new_letter) +' '


with open('q_and_a.txt', 'w', encoding="utf8") as qa:
    qa.writelines("Вопрос: " + question+"\n")
    qa.write("Ответ: " + coding_answer)