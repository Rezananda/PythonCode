import httplib2
def get(domain, path):
    url = "http://" + domain + "/" + path
    h = httplib2.Http(".cache")
    return h.request(url, "GET")

for data in get("filkom.ub.ac.id", "/"):
    print(data)
for data in get("filkom.ub.ac.id", "/apps"):
    print(data)