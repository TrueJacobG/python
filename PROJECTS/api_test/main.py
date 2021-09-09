import requests

responde = requests.get("https://randomfox.ca/floof")
fox = responde.json()

image_url = fox['image']
image = image_url.replace("https://randomfox.ca/images/", "")

with open(image, 'wb') as file:
    response = requests.get(image_url, stream=True)

    if not response.ok:
        print(response)

    for block in response.iter_content(1024):
        if not block:
            break
        file.write(block)
