# Text Summarization Tool

## Overview

This tool summarizes large textual data using the TextRank algorithm, with a focus on efficiency and scalability through the use of Data Structures and Algorithms (DSA).

## Features

- Extractive summarization using TF-IDF and TextRank.
- Preprocessing: tokenization, stopword removal, stemming.
- Scalable and optimized for performance.

## Algorithms Used

This project employs multiple algorithms and techniques to achieve text summarization:

1. **TF-IDF (Term Frequency-Inverse Document Frequency)**:

   - **Purpose**: To quantify the importance of words in each sentence relative to the document.
   - **Usage**: It generates TF-IDF vectors for each sentence, which are then used to compute the similarity between sentences.

2. **Cosine Similarity**:

   - **Purpose**: To measure the similarity between sentences based on their TF-IDF vectors.
   - **Usage**: The similarity matrix is constructed by calculating the cosine similarity between every pair of sentences.

3. **PageRank**:
   - **Purpose**: To rank sentences based on their importance within the similarity graph.
   - **Usage**: The similarity matrix is treated as a graph where sentences are nodes, and the similarities between them are edges. The PageRank algorithm is applied to this graph to rank sentences, identifying the most important ones to include in the summary.

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

- Replace `https://github.com/Aryan-Gupta2003/Text_Summarization_Tool.git` with your actual GitHub repository link.
- Adjust the descriptions or add any additional instructions specific to your project setup.
