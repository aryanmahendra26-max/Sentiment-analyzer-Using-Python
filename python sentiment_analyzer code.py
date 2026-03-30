from textblob import TextBlob

print("hey! welcome to my sentiment analyzer project")
print("just type any sentence and i'll tell you if it's positive, negative or neutral")
print("type 'exit' when you're done")
print()

def analyze(text):
    b = TextBlob(text)
    pol = b.sentiment.polarity
    return pol

while True:

    txt = input("enter text here -> ")

    if txt.lower() == "exit":
        print("ok bye!!")
        break

    if txt.strip() == "":
        print("bro you didn't type anything lol, try again")
        print()
        continue

    result = analyze(txt)

    print()

    # i used 0.1 and -0.1 as cutoff because 
    # anything too close to 0 is basically neutral
    if result > 0.1:
        print("this looks POSITIVE to me :)")
    elif result < -0.1:
        print("this looks NEGATIVE to me :(")
    else:
        print("hmm this seems NEUTRAL, not really positive or negative")

    # showing the score so the user knows how strong the sentiment is
    # -1 means very negative, +1 means very positive
    print("polarity score:", round(result, 2))
    print("(score goes from -1.0 to +1.0 where -1 is worst and +1 is best)")
    print()
