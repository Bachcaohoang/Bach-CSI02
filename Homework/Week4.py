most_common_100 = input('100 từ thông dụng trong tiếng anh: ')
words = most_common_100.split()

sorted_words = sorted(words, key=lambda word: (len(word), word))

sorted_string = ' '.join(sorted_words)

print(sorted_string)