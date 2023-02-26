words = set()
for _ in range(int(input())):
    words.add(input())
mod_words = list(words)
mod_words.sort()
mod_words.sort(key=lambda word: len(word))
for sorted_word in mod_words:
    print(sorted_word)