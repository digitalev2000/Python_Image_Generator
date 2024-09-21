import os
import subprocess
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Configure upload folder and output folder inside static directory
UPLOAD_FOLDER = 'static/input_images'
OUTPUT_FOLDER = 'static/output_images'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed image file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def clear_folder(folder):
    # Delete all files in the folder
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

@app.route('/')
def index():
    return render_template('index.html')

# Handle image upload
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'
    
    if file and allowed_file(file.filename):
        # Clear previous files in input_images and output_images folders
        clear_folder(UPLOAD_FOLDER)
        clear_folder(OUTPUT_FOLDER)

        # Save the new file to input_images folder
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        # Call the generate images script
        subprocess.run(['python', 'generate_images.py'], check=True)
        
        return redirect(url_for('show_gallery'))
    
    return 'File not allowed'

@app.route('/gallery')
def show_gallery():
    # Fetch files from the static/output_images directory
    image_files = [f for f in os.listdir(OUTPUT_FOLDER) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return render_template('image_gallery.html', images=image_files)

if __name__ == '__main__':
    app.run(debug=True)