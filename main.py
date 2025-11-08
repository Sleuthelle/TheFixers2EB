import streamlit
import json
import os

if __name__ == "__main__":
    filePath = streamlit.text_input("Enter file path. Use just a folder for pulling multiple files, and go directly to the file for just the one file.")
    if streamlit.button("Submit File Path"):
        if filePath.endswith(".json"):
            with open(filePath) as jsonFile:
                jsonFileData = json.load(jsonFile)
                streamlit.write(jsonFileData)
                print(type(jsonFileData))

        else:
            jsonFiles = [jsonPosition for jsonPosition in os.listdir(filePath) if jsonPosition.endswith('.json')]
            for index, file in enumerate(jsonFiles):
                with open(os.path.join(filePath, file)) as jsonFile:
                    jsonFileData = json.load(jsonFile)
                    streamlit.write(jsonFileData)
                    print(type(jsonFileData))

