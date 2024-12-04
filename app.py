from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
import os
from utils.ocr_processing import process_document

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['OUTPUT_FOLDER'] = 'outputs/'

# Ensure folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    filename = secure_filename(file.filename)
    upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(upload_path)

    try:
        # Process the document
        output_file_path = process_document(upload_path, filename)
        return send_file(
            output_file_path,
            mimetype='application/pdf',
            as_attachment=False
        )
    except Exception as e:
        return str(e), 500
    finally:
        # Clean up uploaded file
        if os.path.exists(upload_path):
            os.remove(upload_path)

if __name__ == "__main__":
    app.run(debug=True)
