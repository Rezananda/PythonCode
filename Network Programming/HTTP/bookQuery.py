import urllib.request, json
from sys import argv

URL="https://www.googleapis.com/books/v1/volumes?q="

def get(author):
    url = URL+ author.replace(" ","%20")
    with urllib.request.urlopen(url) as response:
        return response.read()
try:
    parseJson = (json.loads(get(argv[1])))
    books = parseJson["items"]
    print("Publisher: ", argv[1])
    print("Title:")
    for i in books:
        print("- ",i["volumeInfo"]["title"])
except:
    print("Error Happens!")


