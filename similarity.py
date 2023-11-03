from fuzzywuzzy import fuzz

text1 = "This is a sample text for similarity calculation."
text2 = "Here is another text for similarity testing."

similarity_ratio = fuzz.ratio(text1, text2)
print(f"Similarity Ratio: {similarity_ratio}")
