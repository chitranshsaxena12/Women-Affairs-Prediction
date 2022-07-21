from flask import Flask, render_template, request
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__ , template_folder='template')
model = pickle.load(open("finalized_model.pickle","rb"))
@app.route("/",methods = ["GET"])
def home_page():
    return render_template("index.html")

standard_to = StandardScaler()
@app.route("/predict",methods = ["POST"])
def prediction_page():
    if request.method == "POST":
        occupation = request.form['occupation']
        if occupation == "Farming/Semi-Skilled/Unskilled":
            Intercept=1
            occ_2 = 1
            occ_3 = 0
            occ_4 = 0
            occ_5 = 0
            occ_6 = 0
        elif occupation == "White Collar":
            Intercept = 1
            occ_2 = 0
            occ_3 = 1
            occ_4 = 0
            occ_5 = 0
            occ_6 = 0
        elif occupation == "Teacher/Nurse/Writer/Technician/Skilled":
            Intercept = 1
            occ_2 = 0
            occ_3 = 0
            occ_4 = 1
            occ_5 = 0
            occ_6 = 0
        elif occupation == "Managerial/Business":
            Intercept = 1
            occ_2 = 0
            occ_3 = 0
            occ_4 = 0
            occ_5 = 1
            occ_6 = 0
        else:
            Intercept = 1
            occ_2 = 0
            occ_3 = 0
            occ_4 = 0
            occ_5 = 0
            occ_6 = 1

        occupation_husb = request.form["occupation_husb"]
        if occupation_husb == "Farming/Semi-Skilled/Unskilled":
            occ_husb_2 = 1
            occ_husb_3 = 0
            occ_husb_4 = 0
            occ_husb_5 = 0
            occ_husb_6 = 0
        elif occupation_husb == "White Collar":
            occ_husb_2 = 0
            occ_husb_3 = 1
            occ_husb_4 = 0
            occ_husb_5 = 0
            occ_husb_6 = 0
        elif occupation_husb == "Teacher/Nurse/Writer/Technician/Skilled":
            occ_husb_2 = 0
            occ_husb_3 = 0
            occ_husb_4 = 1
            occ_husb_5 = 0
            occ_husb_6 = 0
        elif occupation_husb == "Managerial/Business":
            occ_husb_2 = 0
            occ_husb_3 = 0
            occ_husb_4 = 0
            occ_husb_5 = 1
            occ_husb_6 = 0
        else:
            occ_husb_2 = 0
            occ_husb_3 = 0
            occ_husb_4 = 0
            occ_husb_5 = 0
            occ_husb_6 = 1
        rate_marriage = float(request.form["rate_marriage"])
        age = float(request.form["age"])
        yrs_married = float(request.form["yrs_married"])
        children = float(request.form["children"])
        religious = request.form['religious']
        if religious =="Not Religious":
            religious = 1
        elif religious == "Medium Religious":
            religious = 2 or 3
        else:
            religious = 4
        educ = request.form["educ"]
        if educ == "Grade School":
            educ = 9
        elif educ == "High School":
            educ = 12
        elif educ == "Some College":
            educ = 14
        elif educ == "College Graduate":
            educ = 16
        elif educ == "Some Graduate School":
            educ = 17
        else:
            educ = 20
        prediction = model.predict([[Intercept,occ_2,occ_3,occ_4,occ_5,occ_6,occ_husb_2,occ_husb_3,occ_husb_4,occ_husb_5,occ_husb_6,rate_marriage,age,yrs_married,children,religious,educ]])
        if prediction ==1:
            return render_template("result.html" , prediction_texts="Yes,Woman Have At Least One Affair")
        else:
            return render_template("result.html", prediction_texts="No,Woman Haven't Any Affair")
    else:
        return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)



