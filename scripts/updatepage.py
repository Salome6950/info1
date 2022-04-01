# coding: utf8
from atlassian import Confluence
import inspect


print(inspect.signature(Confluence))
confluence = Confluence(
        url='url',
    username='@gmail.com',
    password='token')
#print("The confluence: {}".format(confluence))
space = confluence.get_space("Web")
print("The space: {}\n\n".format(space))

status = confluence.update_page(
#    space= "WEB",
    page_id='688136',
    title='The annoucement of WebLab',
    body='This is the body. You can use HTML tags!'
    )

print(status)
