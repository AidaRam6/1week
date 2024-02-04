def _words(sentence):
  words = sentence.split()
  reversed_words = words[::-1]
  reversed_sentence = " ".join(reversed_words)
  return reversed_sentence

sentence = input("Введите предложение: ")
reversed_sentence = _words(sentence)
print(f"Перевернутое предложение: {reversed_sentence}")
