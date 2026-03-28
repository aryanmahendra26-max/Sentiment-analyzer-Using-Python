#  Sentiment Analyzer
### CSA2001 – Fundamentals of AI and ML | BYOP Project

---

##  Project Description

A simple Python program that analyzes the sentiment of any text and tells you whether it is **Positive**, **Negative**, or **Neutral**. Built using the TextBlob NLP library as part of the BYOP (Bring Your Own Project) capstone for CSA2001.

---

##  How to Run

**Step 1 – Install the library:**
```
pip install textblob
python -m textblob.download_corpora
```

**Step 2 – Run the program:**
```
python sentiment_analyzer.py
```

---

##  Sample Output

```
===== Sentiment Analyzer =====
Type 'quit' to exit

Enter any text: This movie was absolutely fantastic!
Sentiment : POSITIVE
Score     : 0.80
-----------------------------------

Enter any text: The food was terrible.
Sentiment : NEGATIVE
Score     : -0.55
-----------------------------------

Enter any text: The product is okay.
Sentiment : NEUTRAL
Score     : 0.00
-----------------------------------
```

---

##  Tools Used

| Tool | Purpose |
|------|---------|
| Python 3.x | Main programming language |
| TextBlob | NLP library for sentiment analysis |

---

##  Course Outcome Covered

| CO | Description |
|----|-------------|
| CO5 | Sentiment Analyzer – directly listed as a Case Study in CSA2001 |
| CO3 | TextBlob uses Naive Bayes classifier internally |
| CO1 | Demonstrates AI/ML capabilities on real-world text data |

---

##  File Structure

```
sentiment-analyzer/
│
├── sentiment_analyzer.py   # Main Python program
├── README.md               # Project documentation
└── BYOP_Report.docx        # Project report
```

---
