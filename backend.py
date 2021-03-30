from flask import Flask, render_template, request
import folium

# This should be working
app = Flask(__name__)


@app.route("/index/")
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/Map", methods=['POST'])
def map():
    if request.method == 'POST':
        Lat = request.form["Latitude"]
        Lon = request.form["Longitude"]
        f_map = folium.Map(location=[Lat, Lon], zoom_start=9)
        f_map.save("/Users/martin/PycharmProjects/geo/templates/Map.html")
    return render_template("Map.html")


if __name__ == '__main__':
    app.run(debug=True)

    
