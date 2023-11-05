from flask import Flask, request, jsonify
import openai
import os
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
handler = logging.FileHandler('server.log')  # Log to a file
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
handler.setFormatter(formatter)
app.logger.addHandler(handler)

openai.api_key = os.getenv('OPENAI_API_KEY')  # Better practice is to get the API key from the environment

@app.route('/process-images', methods=['POST'])
def process_images():
    # Log the request details
    app.logger.info('Received a request with headers: %s', request.headers)
    app.logger.info('Received a request with files: %s', request.files.keys())

    # Here you would handle the actual image processing...
    # For now, let's assume you're sending a JSON response back
    response = {
        'status': 'success',
        'message': 'Images received and being processed'
    }
    if 'original' not in request.files or 'mask' not in request.files:
        return jsonify({'error': 'Missing images'}), 400

    original_image = request.files['original']
    mask_image = request.files['mask']

    # It's generally a good idea to validate the file extensions,
    # file sizes, and content types to make sure they are images.

    # Save the images temporarily or process them in-memory
    original_path = '/Users/student/Desktop/Interior-Shuffle/newtestpics/bedroom.png'
    mask_path = '/Users/student/Desktop/Interior-Shuffle/newtestpics/bedroom_chandlier_hole.png'
    original_image.save(original_path)
    mask_image.save(mask_path)
    print("reaches")
    # Now call the OpenAI API
    try:
        response = openai.Image.create_edit(
            image=open(original_path, "rb"),
            mask=open(mask_path, "rb"),
            prompt="put a big blue couch with the theme old-fashioned",
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']

        # Clean up the images after processing if they were saved
        os.remove(original_path)
        os.remove(mask_path)

        return jsonify({'image_url': image_url})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Runs the server on port 5000
