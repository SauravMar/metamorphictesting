import random

with open("results/dictionary.txt", "r+") as infile:
    words = [word.strip() for word in infile.readlines()]


def split(word):
    word_list = list(word)
    random_index = random.randint(1, len(word_list) - 1)
    word_list.insert(random_index, ' ')

    return ''.join(word_list)


for word in words:
    print(f"{word}:{split(word)}")


# def insert_random_commas(word):
#     num_commas = random.randint(1, 3)
#     word_list = list(word)
#
#     for _ in range(num_commas):
#         random_index = random.randint(1, len(word_list) - 1)
#         word_list.insert(random_index, ',')
#
#     return ''.join(word_list)
#
#
# with open("results/dictionary.txt", "r+") as infile:
#     words = [word.strip() for word in infile.readlines()]
#
#
# def word_abbrv(word):
#     return word[0]
#
#
# for word in words:
#     print(f"{word}:{word_abbrv(word)}")


#
# with open("results/dictionary.txt", "r+") as infile:
#     words = [word.strip() for word in infile.readlines()]
#
#
# def interchange_middle(word):
#     length = len(word)
#     if length < 3:
#         return word
#
#     middle_index = length // 2
#     new_word = word[:middle_index] + word[middle_index + 1] + word[middle_index] + word[middle_index + 2:]
#
#     return new_word
#
#
# for word in words:
#     print(f"{word}:{interchange_middle(word)}")
