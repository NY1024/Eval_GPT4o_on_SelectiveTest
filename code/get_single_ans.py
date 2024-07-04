from openai import OpenAI
import os
import csv

API_SECRET_KEY = "**";
BASE_URL = "**"  




command = '''
There are four possible answers, A, B, C, and D. Choose the one correct answer.
Give your response in the format "{answer}:{reason}"
you should give your answer firstly.
let's think step by step.
'''

path = './2021/29.png'
import base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def gpt4ov(query,img_path):
    base64_image = encode_image(img_path)
    client = OpenAI(api_key=API_SECRET_KEY, base_url=BASE_URL)
    response = client.chat.completions.create(
      model="gpt-4o",
      messages=[
        {
          "role": "user",
          "content": [
            #{"type": "text", "text": query}
            {"type": "text", "text": query},
            {"type": "image_url", "image_url": {
                "url": f"data:image/png;base64,{base64_image}"}
            }
          ],
        }
      ],
      max_tokens=800,
    )

    return response.choices[0].message.content

ans = gpt4ov(command,path)
print(ans)