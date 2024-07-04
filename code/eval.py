from openai import OpenAI
import os
import csv

API_SECRET_KEY = "**"
BASE_URL = "**"  # Base URL for OpenAI API

command = '''
There are four possible answers, A, B, C, and D. Choose the one correct answer.
Give your response in the format "{answer}:{reason}"
you should give your answer firstly.
let's think step by step.
'''

import base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def gpt4ov(query, img_path):
    base64_image = encode_image(img_path)
    client = OpenAI(api_key=API_SECRET_KEY, base_url=BASE_URL)
    response = client.chat.completions.create(
      model="gpt-4o",
      messages=[
        {
          "role": "user",
          "content": [
            {"type": "text", "text": query},
            {"type": "image_url", "image_url": {
                "url": f"data:image/png;base64,{base64_image}"}
            }
          ],
        }
      ],
      max_tokens=300,
    )

    return response.choices[0].message.content

folder_path = './2021'
output_csv_path = 'cot_2021.csv'
file_names = os.listdir(folder_path)

with open(output_csv_path, mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write the header row to the CSV file (optional)
    csv_writer.writerow(['File Path', 'Result'])
    
    # Iterate through the file names
    for file_name in file_names:
        # Get the full path of each file
        file_path = os.path.join(folder_path, file_name)
        
        # Ensure only files are processed, ignore subdirectories
        if os.path.isfile(file_path):
            # Pass the file path to function gpt4ov for processing
            try:
                result = gpt4ov(command, file_path)
            except Exception as e:
                result = f"Error processing data {file_path}: {e}"
            
            # Write the file path and the processing result to the CSV file
            csv_writer.writerow([file_name, result])
        
print("Processing completed, results saved to", output_csv_path)
