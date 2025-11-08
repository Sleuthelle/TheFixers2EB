import streamlit as st
import json
import os
import uuid


def make_str_field(label: str, value: str = ..., obj=None):
    state = None
    if obj is not None:
        state = obj.text_input(label=label, value=value, key=str(uuid.uuid4()))
    else:
        state = st.text_input(label=label, value=value, key=str(uuid.uuid4()))
    print(state)
    return state


def make_bool_field(label: str, value: bool = False, obj=None):
    state = None
    if obj is not None:
        state = obj.text_input(label=label, value=value, key=str(uuid.uuid4()))
    else:
        state = st.text_input(label=label, value=value, key=str(uuid.uuid4()))
    print(state)
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
            thing[key] = st.text_input(label=label, value=value, key=str(uuid.uuid4()))
            #print("THING KEY HERE:", thing[key])
            #thing[key] = make_str_field(label=label, value=value)
        if isinstance(value, bool):
            # col1.write(key)
            thing[key] = make_bool_field(label=label, value=value)
        if isinstance(value, list):
            # print("Found list")
            for mod_idx, entry in enumerate(value, start=1):
                # label = f"{label}.{mod_idx}"
                if isinstance(entry, dict):
                    st.header(f"{key.title()} {mod_idx}")
                    explore_dict(entry, path=f"{label}.{mod_idx}")
                if isinstance(entry, str):
                    # col1.write(key)
                    thing[key] = make_str_field(label=label, value=entry)
                if isinstance(entry, bool):
                    # col1.write(key)
                    thing[key] = make_bool_field(label=label, value=entry)
    #return thing

#with open("templates/action.json", "r") as fp:
    # with open("templates/character.json", "r") as fp:

#    data = json.load(fp)
    # print(data)
#explore_dict(data)

if __name__ == "__main__":
    filePath = st.text_input("Enter file path. Use just a folder for pulling multiple files, and go directly to the file for just the one file.")
    if st.button("Submit File Path"):
        if filePath.endswith(".json"):
            with open(filePath) as jsonFile:
                jsonFileData = json.load(jsonFile)
                #st.write(jsonFileData)
                #print(explore_dict(jsonFileData))
                tempDict = explore_dict(jsonFileData)
                #print(tempDict)
                print(type(jsonFileData))
            #if st.button("Write to file", key='writebutton2'):
            #    print("write button pressed")
            #    json.dump(tempDict, open("/home/willow/Documents/Hackathon11_25/TheFixers2EB/temp.json", "w"))

        else:
            jsonFiles = [jsonPosition for jsonPosition in os.listdir(filePath) if jsonPosition.endswith('.json')]
            for index, file in enumerate(jsonFiles):
                with open(os.path.join(filePath, file)) as jsonFile:
                    jsonFileData = json.load(jsonFile)
                    #st.write(jsonFileData)
                    tempDict = explore_dict(jsonFileData)
                    print(type(jsonFileData))

