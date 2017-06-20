import base64
enString = base64.b64encode(b'binary\x00string')
deString = base64.b64decode(enString)
print(enString)
print(deString)

safeUrl = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')

url = base64.urlsafe_b64decode('abcd--__')

print(safeUrl)
print(url)
