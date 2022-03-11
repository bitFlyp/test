########################################################################
##
## File name: apiExampleCode.py
## File type: Python file
## Size:
## Author: Sunghyun Kim
## Created On:       3/11/2022[:]
## Last Modified on: 3/11/2022[19:32]
##
## Description: 
## Built for the purpose of being a syntax cheatsheet for using an API
##
########################################################################

## Imported Modules (Must pip install the requests)
import webbrowser, requests, time
#_______________________________________________________________________

response = requests.get("https://randomfox.ca/floof")
#                                 API URL
#_______________________________________________________________________

##                   ----- STATUS CODE -----

print(response.status_code)
## 1xx: Informational
## 2xx: Successful Operation
## 3xx: Redirection - (Must take additional action)
## 4xx: Client Error
## 5xx: Server Error
## 
## (Status code documentation) https://restfulapi.net/http-status-codes/
#_______________________________________________________________________

cuteFox = response.json()

print(type(response.json()))

print(cuteFox["image"])

## Mixing the API request and webbrowser module together
chrome = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
webbrowser.get(chrome).open_new(cuteFox["image"])