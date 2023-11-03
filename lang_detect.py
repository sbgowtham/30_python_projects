from langdetect import detect

text = "தமிழ்" #தமிழ்
language = detect(text)
print("Detected language:", language)