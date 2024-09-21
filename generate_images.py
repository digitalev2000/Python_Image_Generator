from PIL import Image, ImageEnhance, ImageFilter
import os

# Define the input and output directories
input_dir = 'static/input_images'
output_dir = 'static/output_images'

# Ensure output folder exists
if not os.path.exists(output_dir):
   # Ensure output directory exists
   os.makedirs(output_dir, exist_ok=True)  

def generate_variations(image_path):
    # Open an image file
    with Image.open(image_path) as img:
        filename = os.path.basename(image_path).split('.')[0]

        # Example 1: Resize the image
        img_resized = img.resize((img.width // 4, img.height // 4))
        img_resized.save(os.path.join(output_dir, f'{filename}_resized.png'))

        # Example 2: Apply a filter (BLUR)
        img_blur = img.filter(ImageFilter.BLUR)
        img_blur.save(os.path.join(output_dir, f'{filename}_blur.png'))

        # Example 3: Change brightness
        enhancer = ImageEnhance.Brightness(img)
        img_bright = enhancer.enhance(3.8)  # Increase brightness by 50%
        img_bright.save(os.path.join(output_dir, f'{filename}_bright.png'))

        # Example 4: Convert to grayscale
        img_gray = img.convert('LA')
        img_gray.save(os.path.join(output_dir, f'{filename}_gray.png'))

        # Example 5: Adjust contrast
        contrast_enhancer = ImageEnhance.Contrast(img)
        img_contrast = contrast_enhancer.enhance(-4.2)  # Increase contrast by 80%
        img_contrast.save(os.path.join(output_dir, f'{filename}_contrast.png'))

        # Example 6: Adjust color
        color_enhancer = ImageEnhance.Color(img)
        img_color = color_enhancer.enhance(5.7)  # Increase color saturation by 70%
        img_color.save(os.path.join(output_dir, f'{filename}_color.png'))


def process_images():
    for image_name in os.listdir(input_dir):
        if image_name.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_dir, image_name)
            generate_variations(image_path)
            print(f"Processed {image_name}")

if __name__ == '__main__':
    process_images()