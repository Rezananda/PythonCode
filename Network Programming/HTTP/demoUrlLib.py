import urllib.request
def get(domain, path):
    url = "http://" + domain + "/" + path
    with urllib.request.urlopen(url) as f:
        return f.info(), f.read()

for data in get("filkom.ub.ac.id", "/"):
    print(data)
for data in get("filkom.ub.ac.id", "/apps"):
    print(data)