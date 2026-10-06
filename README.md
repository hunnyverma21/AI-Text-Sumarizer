# AI Text Summarizer

## Project Overview

AI Text Summarizer is a beginner-friendly Python project that creates a short summary from a longer piece of text.

This project uses **extractive summarization**. It analyzes word frequency, scores sentences, and selects the most relevant sentences.

## Features

- Accepts multi-line text
- Finds frequently used meaningful words
- Scores sentences
- Generates a short summary
- Lets the user choose summary length
- Requires no API key
- Uses Python standard libraries

## How to Run

```bash
python ai_text_summarizer.py
```

## Example

Input:

```text
Python is a popular programming language.
Python is widely used for data analysis.
Data analysts use Python to clean and analyze datasets.
Python also has many machine learning libraries.
```

The program selects the most important sentences based on word frequency.

## Concepts Used

- Functions
- Strings
- Lists
- Dictionaries
- Loops
- Regular expressions
- Counter
- Sentence scoring
- Text processing
- User input

## Project Files

- `ai_text_summarizer.py` - Main Python program
- `README.md` - Project documentation
- `problem_statement.txt` - Problem statement

## Important Note

This is an **AI-style extractive summarizer**. It does not use a large language model or external AI API.

## Future Improvements

- Use Hugging Face Transformers
- Add an AI API
- Add a Streamlit interface
- Support PDF and DOCX files
- Add multilingual summarization
- Add summary length controls
