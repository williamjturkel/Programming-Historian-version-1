# write-html-2.py
 
import webbrowser
 
f = open('helloworld.html','w')
 
message = """<html>
<head></head>
<body>Hello World!</body>
</html>"""
 
f.write(message)
f.close()
 
webbrowser.open_new_tab('helloworld.html')
