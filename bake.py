with open('index.html', 'r') as file:
    data = file.read()
    with open("style/main.css", 'r') as Sfile:
       data2 = Sfile.read()
       e = data.replace('<link rel="stylesheet" href="./style/main.css">', "<style>" + data2 + "</style>")
       with open("output.html", "w+") as g:
        g.write(e);