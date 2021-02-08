#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open('text', 'r') as f:
        text = f.read()

    # Заменить символы конца предложения.
    text = text.replace("!", ".")
    text = text.replace("?", ".")

    # Удалить все многоточия.
    while ".." in text:
        text = text.replace("..", ".")

    # Разбить текст на предложения.
    sentences = text.split(".")

    # Вывод предложений с запятыми.
    for sentence in sentences:
        if "," in sentence:
            with open('text', 'r')as s:
                f_text = s.read()
                if sentence in f_text:
                    print(f'{sentence}{f_text[f_text.rfind(sentence) + len(sentence)]}')