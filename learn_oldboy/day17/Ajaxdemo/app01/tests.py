from django.test import TestCase

# Create your tests here.
import json

ret=json.dumps({'name':'alex'})
print(ret)# '{"name": "alex"}'

ret=json.loads('{"name":"alex"}')
print(ret["name"])
