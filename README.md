# Text Summarization Tool

## Overview

This tool summarizes large textual data using the TextRank algorithm, with a focus on efficiency and scalability through the use of Data Structures and Algorithms (DSA).

## Features

- Extractive summarization using TF-IDF and TextRank.
- Preprocessing: tokenization, stopword removal, stemming.
- Scalable and optimized for performance.

## Installation

### Prerequisites

- Python 3.x

### Step-by-Step Guide

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/text-summarization-tool.git
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Download NLTK Data**:
   ```bash
   python -m nltk.downloader punkt stopwords
   ```

## Usage

1. **Command-Line Interface**:
   You can summarize a text file by running:

   ```bash
   python src/main.py
   ```

2. **Flask Web Interface**:
   To use the web interface with Flask:

   1. Run the Flask app:
      ```bash
      python src/app.py
      ```
   2. Open your web browser and go to http://127.0.0.1:5000/.

   - Input: Enter the text in the provided text area and specify the number of sentences for the summary.
   - Output: The summarized text is displayed on the same page after submission.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

### Customization

- Replace `https://github.com/your-username/text-summarization-tool.git` with your actual GitHub repository link.
- Adjust the descriptions or add any additional instructions specific to your project setup.
