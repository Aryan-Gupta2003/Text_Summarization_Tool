from flask import Flask, render_template, request
from summarizer import Summarizer

app = Flask(__name__)
summarizer = Summarizer()

@app.route('/', methods=['GET', 'POST'])
def home():
    summary = ""
    if request.method == 'POST':
        text = request.form['text']
        num_sentences = int(request.form.get('num_sentences', 3))
        summary = summarizer.summarize(text, num_sentences=num_sentences)
    
    return render_template('index.html', summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
