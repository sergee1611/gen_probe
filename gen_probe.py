# Напишите функцию-генератор all_variants(text),
# которая принимает строку text и возвращает объект-генератор,
# при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
def all_variants(text):
    # letters = [ch for ch in text]
    # result = [x + y for x in text for y in text]

    for ch in text:
        yield ch
        if ch is text[-1]:
            for i in range(len(text)):
                if i < len(text) - 1:
                    new_text = list(text).copy()
                    new_text.remove(text[i-1])
                    new_text = ''.join(new_text)
                else:
                    new_text = list(text).copy()
                    new_text = ''.join(new_text)
                yield new_text


a = all_variants("abc")
for i in a:
    print(i)

# Вывод на консоль:
# a
# b
# c
# ab
# bc
# abc
