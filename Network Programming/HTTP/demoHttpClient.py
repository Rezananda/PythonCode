import http.client
def get(domain, url):
    conn = http.client.HTTPSConnection(domain)
    conn.request("GET", url)
    response = conn.getresponse()
    return response.getheaders(), response.read()

for data in get("filkom.ub.ac.id", "/"):
    print(data)

for data in get("filkom.ub.ac.id", "/apps"):
    print(data)