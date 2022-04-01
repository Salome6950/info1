import requests
import json
import base64

# Set the confluence User and Password for authentication
user = '@gmail.com'
password = 'token'

# Set the title and content of the page to create
page_title = 'WebLab Deployment Notice'
page_html = '<p>WebLab on AWS deploy completed.</p>'

# You need to know the parent page id and space key.
# You can use the /content API to search for these values.
# Parent Page example http://example.com/display/ABC/Cheese
# Search example: http://example.com/rest/api/content?title=Cheese
parent_page_id = 557192
space_key = 'WEB'

# Request URL - API for creating a new page as a child of another page
url = 'url'

# Create the basic auth for use in the authentication header
#auth = base64.b64encode(b'{}:{}'.format(user, password))
auth_str = bytes('{}:{}'.format(user, password), 'utf-8')
auth = base64.b64encode(auth_str).decode('utf-8')
# Request Headers
headers = {
    'Authorization': 'Basic {}'.format(auth),
    'Content-Type': 'application/json',
}

# Request body
data = {
    "page_id": "688136",
    "type": "page",
    "title": page_title,
#    'ancestors': [{'id':parent_page_id}],
    "space": {"key":space_key},
    "body": {
        "storage":{
            "value": page_html,
            "representation":"storage",
        }
    },
    "version":{"number":6}
}
print(data)

# We're ready to call the api
try:

    r = requests.post(url=url, data=json.dumps(data), headers=headers)

    # Consider any status other than 2xx an error
    if not r.status_code // 100 == 2:
        print("Error: Unexpected response {}".format(r))
#        print("Error Msg: {}".format(r.json()))
        print("Header: {}".format(headers))
        print("Body: {}".format(data))
    else:
#        print(r.message)
        print('Page Created!')

except requests.exceptions.RequestException as e:

    # A serious problem happened, like an SSLError or InvalidURL
    print("Error: {}".format(e))
