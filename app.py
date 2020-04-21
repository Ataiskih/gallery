from flask import Flask, render_template, request


app = Flask(__name__)
@app.route("/")
def main():
    filee = open('uuu.txt', 'r', encoding='utf-8')
    lst_photo = [line for line in filee]
    filee.close()
    return render_template("main.html", lst_photoo = lst_photo)

@app.route("/add", methods=["POST", "GET"])
def adds():
    if request.method == 'POST':
        urls = request.form.get('url')
        filee = open('uuu.txt', 'a+', encoding='utf-8')
        filee.write(str(urls) + '\n')
        filee.close()
    return render_template("photo.html")

    filee = open('uuu.txt', 'r', encoding='utf-8')
    filee.close()
    return render_template("photo.html")