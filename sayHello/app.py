from flask import Flask, render_template, request, flash
import os

app = Flask(__name__)
app.secret_key = "een_zeer_geheime_sleutel"

# Zorg ervoor dat de map 'data' bestaat
if not os.path.exists('data'):
    os.makedirs('data')

@app.route("/FindMyDate3000", methods=["GET", "POST"])
def FindMyDate3000():
    if request.method == "POST":
        name_input = request.form['name_input']
        
        # Sla de naam op in een tekstbestand
        with open(os.path.join('data', 'names.txt'), 'a') as file:
            file.write(name_input + '\n')
        
        flash(f"Hello {name_input}, great, I have saved your name. I will send it to Eloise!")
    
    return render_template("index.html")

if __name__ == "__main__":
    # Zorg ervoor dat de Flask-app luistert op alle interfaces
    app.run(host='0.0.0.0', port=5000, debug=True)