




import os
from flask import Flask,render_template,request
import requests
from scraping import Scraping
product = 1
search = 1


"-----------------------------------------------"


def initializeInput(inputname):
    return Scraping(inputname)

def initializeFiles():
    attributes = {}
    comments = []
    prices = {}
    with open("project3/attributes.txt","r",encoding="UTF-8") as file:
        attributesList = file.readlines()
        for element in attributesList: 
            char = element.split(":")
            attributes[char[0]] = char[1]
    with open("project3/comments.txt","r",encoding="UTF-8") as file:
        list = file.readlines()
        for element in list:
            comments.append(element)
        if (len(comments) == 0):
            comments.append("Bu ürün için yorum bulunmamaktadır.")
    with open("project3/prices.txt","r",encoding="UTF-8") as file:
        list = file.readlines()
        print(len(list))
        for element in list:
            oneprice = element.split("_")
            prices[oneprice[0]] = oneprice[1]
    image = os.path.join("static")
    app.config['UPLOAD_FOLDER'] = image
    return attributes,comments,prices

    

"-----------------------------------------------"


app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def homePage():
    if request.method == "POST":
        searchingInput = request.form.get("input")
        initializeInput(searchingInput)
        attributes,comments,prices = initializeFiles()
        image = os.path.join(app.config['UPLOAD_FOLDER'], 'filename.png')
        return render_template("layout.html",features = attributes,comments = comments,product=product,user_image=image,prices=prices)
    elif request.method == "GET":
        return render_template("layout.html",search=search)
    return render_template("layout.html",search=search)

if __name__ == "__main__":
    app.run(debug=True,port=5555)
