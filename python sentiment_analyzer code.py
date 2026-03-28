from textblob import TextBlob

print("===== Sentiment Analyzer =====")
print("Type 'quit' to exit\n")

while True:
    text = input("Enter any text: ")
    
    if text.lower() == 'quit':
        break

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        result = "POSITIVE 😊"
    elif polarity < -0.1:
        result = "NEGATIVE 😞"
    else:
        result = "NEUTRAL 😐"

    print(f"Sentiment : {result}")
    print(f"Score     : {polarity:.2f}  (-1 = very negative, +1 = very positive)")
    print("-" * 35)
    
