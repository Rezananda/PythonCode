import urllib.request, json
from sys import argv

URL="https://www.googleapis.com/books/v1/volumes?q=isbn:"

def get(isbn):
    url = URL+ isbn
    with urllib.request.urlopen(url) as response:
        return response.read()
try:
    parseJson = (json.loads(get(argv[1])))
    title=parseJson["items"][0]["volumeInfo"]["title"]
    authors=parseJson["items"][0]["volumeInfo"]["authors"]
    publisher=parseJson["items"][0]["volumeInfo"]["publisher"]
    publishedDate=parseJson["items"][0]["volumeInfo"]["publishedDate"]

    print("Title: ",title)
    print("Authors:")
    for i in authors :
        print("- ",i)
    print("Publisher: ",publisher)
    print("Published Date: ",publishedDate)
except:
    print("Error Happens!")
