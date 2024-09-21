Running the Script
......................
Step 1: Go to workspace
cd "to your project directory\pod-image-variation"


Step 2: Activate the evironment and run the app.y file
Scripts\activate
python app.py 


Step 3: Install > 
pip install Pillow glob2
pip install flask


Step 4:Run > 
python app.py

Step 5:
......................
Upload the image on the first page you would like to see variations for and click upload.
......................


Step 6:
......................
Change code in the generate_images.py file to enhance the image contrast, grayscale, color inside of the "def generate_variations(image_path):"  block of code in the generate_images.py file save then rerun the app.py file
......................


Issues:
......................
If issues occur try reinstalling (pip install Pillow) then try restarting the CPU or re-downloading the .zip file
pip install --upgrade Pillow
pip install --upgrade pip
