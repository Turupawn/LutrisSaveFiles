import json
import glob
import os

from pprint import pprint

def findFilesByExpression(files_expression):
    files_expression = files_expression.replace("$HOME", os.getenv("HOME"))
    files_expression = files_expression.replace("$XDG_DATA_HOME", os.getenv("HOME")+"/.local/share")
    files_expression = files_expression.replace("$XDG_CONFIG_HOME", os.getenv("HOME")+"/.config")
    files_found = glob.glob(files_expression, recursive=True)
    for file_found in files_found:
        pprint(file_found)

def findFiles(file_type):
    pprint(file_type + " files:")
    if file_type in game["files"]:
        files_expression = game["files"][file_type]
        if isinstance(files_expression,str):
            findFilesByExpression(game["files"][file_type])
        if isinstance(files_expression,list):
            for expression in files_expression:
                findFilesByExpression(expression)

with open('game_list.json') as data_file:    
    data = json.load(data_file)


for game in data["games"]:
    pprint('===' + game["name"] + '===')

    findFiles("config")
    findFiles("saves")
    findFiles("replays")
    findFiles("screenshots")
