import io
import os
import re
# Imports the Google Cloud client library
from google.cloud import vision_v1p1beta1 as vision

class Process_CBG():
    def __init__(self):
        pass
    
    # returns numerical reading (float) and measurement unit (string)
    def get_Reading(self, image_path):
        # Instantiates a client
        client = vision.ImageAnnotatorClient()

        # The name of the image file to annotate
        file_name =  os.path.abspath(image_path)

        # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()
        image = vision.types.Image(content=content)

        # Performs text detection on the image
        response = client.text_detection(image=image)
        texts = response.text_annotations

        # find and write reading on image
        found_Reading = False
        found_Measurement = False
        for text in texts:
            if found_Reading and found_Measurement:
                break
            elif not found_Reading and (re.match("\d+\.\d+", text.description) or re.match("^\d+$", text.description)):
                reading = text.description
                found_Reading = True
            elif not found_Measurement and (re.match("^mg$", text.description) or re.match("^mmol$", text.description)):
                measurement = text.description
                if measurement == 'mg':
                    measurement += 'dL'
                else:
                    measurement += 'L'
                found_Measurement = True
        
        return float(reading), measurement
