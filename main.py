import streamlit as st
import json
import os

st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&family=Silkscreen&display=swap');
            
            h1 {
            color: #7FDA8F !important;
            font-family: 'Silkscreen', sans-serif !important;
            text-align: center !important;
            }
            h2 {
            color: #4A7F54 !important;
            font-family: 'Silkscreen', sans-serif !important;
            }
            html, body, [class*="css"] {
            font-family: 'Silkscreen', sans-serif !important;
            }
            button {
            background-color: #0a0e0a !important;
            border: 12 px !important;
            color: #7FDA8F !important;
            border-color: #7FDA8F !important;
            }
            button:hover {
            background-color: #579C6E !important;
            border: 12 px !important;
            color: #000000 !important;
            border-color: #579C6E !important;
            }
             p {
            color: #7FDA8F !important;
            font-family: 'Silkscreen', sans-serif !important;
            }
            ul {
            color: #7FDA8F !important;
            font-family: 'Silkscreen', sans-serif !important;
            }
            </style>
            """, unsafe_allow_html=True)  
        

st.title("Bottle Episodes: Creations")

st.header("Write your story", divider="rainbow")


def make_str_field(label: str, value: str = ..., obj=None):
    state = None
    if obj is not None:
        state = obj.text_input(label=label, value=value)
    else:
        state = st.text_input(label=label, value=value)
    return state


def make_bool_field(label: str, value: bool = False, obj=None):
    state = None
    if obj is not None:
        state = obj.text_input(label=label, value=value)
    else:
        state = st.text_input(label=label, value=value)
    return state


def explore_dict(thing: dict, path: str = ""):
    for key, value in thing.items():
        # #print(f"{key}")
        label = f"{path}.{key}" if path else key.title()
        # print(label)
        if isinstance(value, dict):
            st.header(key.title())
            explore_dict(value, f"{path}.{key.title()}" if path else key.title())
        if isinstance(value, str):
            # col1.write(key)
            make_str_field(label=label, value=value)
        if isinstance(value, bool):
            # col1.write(key)
            make_bool_field(label=label, value=value)
        if isinstance(value, list):
            # print("Found list")
            for mod_idx, entry in enumerate(value, start=1):
                # label = f"{label}.{mod_idx}"
                if isinstance(entry, dict):
                    st.header(f"{key.title()} {mod_idx}")
                    explore_dict(entry, path=f"{label}.{mod_idx}")
                if isinstance(entry, str):
                    # col1.write(key)
                    make_str_field(label=label, value=entry)
                if isinstance(entry, bool):
                    # col1.write(key)
                    make_bool_field(label=label, value=entry)

hints = """
 Placeholder tokens used in fragments:
 - {character} - Target's display name
 - {pronoun_subject} - "she", "he", "they"
 - {pronoun_subject_cap} - "She", "He", "They"
 - {pronoun_object} - "her", "him", "them"
 - {pronoun_possessive} - "her", "his", "their"
 - {verb_look} - "doesn't" or "don't" (based on plural)
 - {verb_feel} - "feels" or "feel" (based on plural)
 - {verb_want} - "wants" or "want" (based on plural)
 - {verb_be} - "is" or "are" (based on plural)
 - {verb_plan} - "plans" or "plan" (based on plural)
"""

#with open("templates/action.json", "r") as fp:
    # with open("templates/character.json", "r") as fp:

#    data = json.load(fp)
    # print(data)
#explore_dict(data)

if __name__ == "__main__":
    filePath = st.text_input("Enter file path. Use just a folder for pulling multiple files, and go directly to the file for just the one file.")
    if st.button("Submit File Path"):
        st.write(hints)
        if filePath.endswith(".json"):
            with open(filePath) as jsonFile:
                jsonFileData = json.load(jsonFile)
                #st.write(jsonFileData)
                explore_dict(jsonFileData)
                print(type(jsonFileData))

        else:
            jsonFiles = [jsonPosition for jsonPosition in os.listdir(filePath) if jsonPosition.endswith('.json')]
            for index, file in enumerate(jsonFiles):
                with open(os.path.join(filePath, file)) as jsonFile:
                    jsonFileData = json.load(jsonFile)
                    #st.write(jsonFileData)
                    explore_dict(jsonFileData)
                    print(type(jsonFileData))

