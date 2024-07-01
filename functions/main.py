# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn, options
from firebase_admin import initialize_app
import json
import os

initialize_app()

@https_fn.on_request(cors=options.CorsOptions(cors_methods="*", cors_origins="*"))
def process_image(req: https_fn.Request) -> https_fn.Response:
    # Extract text parameter
    text_param = req.form.get('text')
    
    # Extract image parameter
    image = req.files.get('image')
    
    # Get image name and size
    if image:
        image_name = image.filename
        image_size = len(image.read())  # Get the size in bytes
        image.seek(0)  # Reset the file pointer to the beginning
    else:
        image_name = None
        image_size = None
    
    # Create HTML content
    html_content = f"""
    <html>
    <head><title>Pilates Image Analysis Result</title></head>
    <body>
        <h1>Pilates Image Analysis Result</h1>
        <p><strong>Text:</strong> {text_param}</p>
        <p><strong>Image Name:</strong> {image_name}</p>
        <p><strong>Image Size:</strong> {image_size} bytes</p>
    </body>
    </html>
    """

    return https_fn.Response(html_content, mimetype='text/html')
