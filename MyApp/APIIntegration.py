import requests

URL_ = "https://api.memegen.link/images/custom/" # _ at the end bc don t wanna risk overwriting anything remotely important
def generate_meme(topText: str, bottomText: str):

    #links cant hold spaces so replace them with _
    memeURL = f"{URL_}{topText.replace(" ", "_")}/{bottomText.replace(" ", "_")}.png"

    # Download the meme image
    response = requests.get(memeURL)

    if response.status_code == 200:
        with open("meme.png", "wb") as file: # wb = write binary
            file.write(response.content)
    else:
        print(f"Failed. Status code: {response.status_code}")

generate_meme("Hello", "World")