# Extractive Text Summarization System

This project implements an extractive text summarization pipeline using spaCy and frequency-based sentence scoring. It selects the most important sentences from source text and returns a concise summary.

## Features

- **Extractive summarization** using NLP sentence scoring
- **SpaCy tokenization** and stop-word filtering
- **Frequency-based ranking** for sentence importance
- **Reproducible notebook** and Python script implementation
- **Simple setup** with `requirements.txt`

## Project Structure

```
Extractive_Text_Summarization_System/
├── README.md
├── requirements.txt
├── extractive_text_summarization.ipynb
├── extractive_summarizer.py
└── (optional source text files)
```

## Requirements

- Python 3.7+
- spaCy
- numpy
- pandas
- matplotlib

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Install the spaCy English model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

## Usage

### Notebook
1. Open the notebook:
   ```bash
   jupyter notebook extractive_text_summarization.ipynb
   ```
2. Run the notebook cells sequentially.

### Script
1. Run the script:
   ```bash
   python extractive_summarizer.py
   ```

## Summary Logic

- Load the input text
- Tokenize sentences and words
- Remove stop words and punctuation
- Build normalized word frequency scores
- Score each sentence by summing the frequencies of constituent words
- Select the top sentences to form the summary

## Notes

- The notebook includes a sample text example.
- The script can be extended to load text from files or user input.
- This is an extractive summarizer, so it uses sentences from the original text.

