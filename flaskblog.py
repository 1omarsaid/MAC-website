from flask import Flask, render_template, url_for
# from firebase import firebase
app = Flask(__name__)

# firebase = firebase.FirebaseApplication('https://macmississauga-8066f.firebasei$

# iqama = [None]*7
# iqama[0] = firebase.get('I-Fajr',None)
# iqama[1] = firebase.get('I-Dhur',None)
# iqama[2] = firebase.get('I-Asr',None)
# iqama[3] = firebase.get('I-Maghrib',None)
# iqama[4] = firebase.get('I-Isha',None)
# iqama[5] = firebase.get('Jumaa1',None)
# iqama[6] = firebase.get('Jumaa2',None)


# changedDate = firebase.get('DateChange',None)


# athan = ["12:30 pm","12:30 pm","12:30 pm","12:30 pm","12:30 pm"]
iqama = ["12:30 pm","12:30 pm","12:30 pm","12:30 pm","12:30 pm", "12:30 pm", "12:30 pm"]
changedDate = "June 12"

@app.route("/")
def home():
    return render_template('home.html', iqama=iqama, changedDate=changedDate)

if __name__ == '__main__':
    app.run(debug=True)