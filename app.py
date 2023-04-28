from flask import Flask, render_template, request
from AppCode import average_rate
app = Flask(__name__)




@app.route('/', methods=["GET", "POST"])
def nearestStation():
    if request.method == "POST":
        staeName= request.form['state']
        cityName = request.form['city']
        zipCode = request.form['zipcode']
        numRoom = request.form['numroom']
        averageRate = average_rate(staeName,cityName,zipCode,numRoom)
        
        return render_template("result1.html", cityName = cityName, averageRate= averageRate, numroom = numRoom)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)