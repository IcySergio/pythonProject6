from flask import Flask, render_template, request

app = Flask(__name__)

# Пример данных
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/plots")
def plots():
    return render_template("plots.html", data=data)

@app.route("/average", methods=["POST"])
def average():
    start = int(request.form.get("start"))
    end = int(request.form.get("end"))
    selected_data = data[start:end + 1]
    avg = sum(selected_data) / len(selected_data)
    return f"Average for selected range: {avg}"

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
