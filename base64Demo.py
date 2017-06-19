import base64
enString = base64.b64encode(b'binary\x00string')
deString = base64.b64decode(enString)
print(enString)
print(deString)
