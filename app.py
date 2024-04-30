from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_data():
    if request.method == 'POST':
        file = request.files['file']
        # Save the uploaded file
        file.save('data.txt')
        return 'File uploaded successfully'
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)