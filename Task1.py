import re
import pyuca

def read_and_sort_sentence(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

            sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
            if sentences:
                first_sentence = sentences[0]

                words = re.findall(r'\b\w+\b', first_sentence)

                words.sort(key=lambda x: x.lower())

                ukrainian_words = [word for word in words if re.match(r'^[А-Яа-яІіЇїЄєҐґ]+$', word)]
                english_words = [word for word in words if re.match(r'^[A-Za-z]+$', word)]

                collator = pyuca.Collator()

                sorted_ukrainian_words = sorted(ukrainian_words, key=collator.sort_key)

                sorted_words = sorted_ukrainian_words + english_words

                print("Перше речення:")
                print(first_sentence)
                print("\nСлова першого речення в алфавітному порядку:")
                print(sorted_words)
                print("\nКількість слів у першому реченні:", len(words))
            else:
                print("Файл не містить речень.")

    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print("Виникла помилка:", str(e))


read_and_sort_sentence("text.txt")
