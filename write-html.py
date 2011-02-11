# write-html.py
 
f = open('helloworld.html','w')
 
message = """<html>
<head></head>
<body>Hello World!</body>
</html>"""
 
f.write(message)
f.close()