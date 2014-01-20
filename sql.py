In cmd prompt type:
  mysql -u root -p
To read html file in python:
  #!/python33/python
  import cgi,cgitb
  f=open("cg.html",r)
  print(f.read())
form.html:
<html>
<body>
<form name="ak" action="k.py" method="post">
<input type="text" name="uname">
<input type="submit" name"submit">
</form>
</body>
</html>
l.py:
  #!python33/python
  import cgi,cgitb
  cgitb.enable()
  print("content_type:text/html")
  print(" ")
  f=cgi.FieldStorage()
  n=f.getvalue('uname')
  print("Hi.{0}","welcome to python".format(n))
