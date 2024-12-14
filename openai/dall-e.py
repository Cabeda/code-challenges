import argparse
import datetime

import requests
from openai import OpenAI


def generate_image(prompt: str):
    client = OpenAI()

    response = client.images.generate(
        model="dall-e-3",
        prompt="prompt",
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url

    print(image_url)

    # Download the image using the URL

    image = requests.get(image_url)

    # generate datetime for filename
    filename = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    # Save the image
    with open(f"{filename}.jpg", "wb") as file:
        file.write(image.content)

if __name__ == "__main__":

    # Accept the prompt from the user
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--prompt", type=str)

    args = argparser.parse_args()

    print(args.prompt)
    generate_image(prompt = args.prompt)