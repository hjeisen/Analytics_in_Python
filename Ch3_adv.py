import requests
a  = requests.get("https://en.wikipedia.org/wiki/main_page")
# print (a.text)
print (a.content.decode('utf-8').find("Did you know"))
# print (a.text.find("Did you know"))

