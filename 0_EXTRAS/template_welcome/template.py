style = '''\
<!DOCTYPE html>
<html>
<head>
<style>
body {
  font-family: 'Trebuchet MS', sans-serif;
}
.header {
  width: 100%;
  margin-left: auto; 
  margin-right: auto;
  border-radius: 10px;
  padding: 1px;
  text-align: center;
  background-color: black;
  color: rgb(60, 179, 113);
  font-size: 32px;
}
tr:hover {background-color:rgb(0,0,0); color:rgb(60, 179, 113);}
/* Create two equal columns that sits next to each other */
table, th, td, tr {
  font-size: 12px;
  border-radius: 5px;
  border: none;
  padding: 1px;
  border-collapse: collapse;
  text-align: center;   
  white-space: nowrap;
  margin-left: auto; 
  margin-right: auto;
}
th {
  height: 16px;
}
td {
  font-weight: bold;
}
</style>
</head>
<body>
'''
end_html =''' 
</body>
</html>'''


highlight = """<div class="header">
                <h5>&lt;Programación Aplicada a Finanzas/&gt;</h5>
              </div> """
