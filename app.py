from flask import Flask, request, render_template
from model import preprocess_data, answer_question

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_data():
    if request.method == 'POST':
        file = request.files['file']
        
        file.save('data.txt')
        return 'File uploaded successfully'
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/ask', methods=['POST'])
def ask_question():
    question = request.form['question']
    with open('data.txt', 'r') as f:
        data = f.read()
    answer = answer_question(question, data)
    return answer