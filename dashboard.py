import textblob as tb
import matplotlib.pyplot as plt
import numpy as np
import csv
print("ENTER 1 TO SHOW POSITIVE TWEETS:\r\nENTER 2 TO SHOW NEGATIVE TWEETS:\r\nENTER 3 TO SHOW NEUTRAL TWEETS:\r\nENTER 4 TO SHOW THE GRAPH")
def main_sa():
    delimiters = ["[", "'", "]", "(", ")"]
    pos = 0
    neg = 0
    neu = 0
    y = []
    a = int(input())
    with open('Twitter_Data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data = row
            string_data = str(data)

            for i in delimiters:
                string_data = string_data.replace(i, '')
            input_to_textblob = tb.TextBlob(string_data)
            sentence_polarity = input_to_textblob.sentiment.polarity

            if (sentence_polarity > 0):
                y.append(sentence_polarity)
                pos += 1
            elif (sentence_polarity == 0):
                y.append(sentence_polarity)
                neu += 1
            elif (sentence_polarity < 0):
                y.append(sentence_polarity)
                neg += 1

    if a == 1:
        print("Total Positive", pos)
        main_sa()
    elif a == 2:
        print("Total Negative", neg)
        main_sa()
    elif a == 3:
        print("Total Neutral", neu)
        main_sa()
    elif a == 4:
        x = np.random.normal(min(y), max(y), len(y))
        plt.scatter(x, y)
        plt.savefig("sentiment_analysis.pdf")
        plt.show()
        main_sa()

main_sa()