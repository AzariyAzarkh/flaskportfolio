from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route("/")
def portfolio():
    return render_template("portfolio.html")

@app.route('/yasinvideo')
def yasinvideo():
    return render_template('yasinvideo.html')

if __name__ == "__main__":
    app.run(debug=True)