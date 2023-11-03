from textblob import Word

text = "Yourr text with misspelled wrds goes here."
corrected_text = " ".join(Word(word).correct() for word in text.split())
print(corrected_text)