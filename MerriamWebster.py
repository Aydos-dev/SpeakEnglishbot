import requests
from pprint import pprint

API_KEY = "981e4fc7-eff6-49bb-9e01-18942d6bda27"

def getDefinitions(word_id):

    url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word_id}?key={API_KEY}"
    response = requests.get(url)
    result = response.json()

    try:
        definitions = "\n".join(result[0]["shortdef"])
    except TypeError:
        return False
    except IndexError:
        return False
    else:

        link_audio = result[0]["hwi"]["prs"][0]["sound"]["audio"]

        if link_audio.startswith("big"):
            subdirectory = "bix"
        elif link_audio.startswith("gg"):
            subdirectory = "gg"
        elif link_audio[0] in ["0","1","2","3","4","5","6","7","8","9"] or link_audio[0] in [".", ",", "!", "?", "-", "_", ":",";"]:
            subdirectory = "number"
        else:
            subdirectory = link_audio[0]
        audio = f"https://media.merriam-webster.com/audio/prons/en/us/ogg/{subdirectory}/{link_audio}.ogg"

        output = {"definitions": definitions, "audio": audio}

        return output

if __name__ == "__main__":
    pprint(getDefinitions("apple"))
    pprint(getDefinitions("prodigious"))
    pprint(getDefinitions("nonono"))




