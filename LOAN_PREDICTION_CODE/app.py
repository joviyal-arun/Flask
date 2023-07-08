from flask import Flask, render_template, request
import pickle
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('register.html')

@app.route("/confirm", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        n = request.form.get('name')
        a = request.form.get('mobilenumber')
        c = request.form.get('city')
        return  render_template('confirm.html',name=n,age=a,city=c)

@app.route("/predict", methods=['POST', 'GET'])
def completed():
    if request.method == 'POST':

        label_encoder = LabelEncoder()

        new_gender=request.form.get('Gender')
        new_married_sts=request.form.get('Married')
        dependent_count=int(request.form.get('Dependents'))
        education_sts=request.form.get('Education')
        self_emp_sts=request.form.get('Self_Employed')
        applicant=int(request.form.get('ApplicantIncome'))
        co_applicant=int(request.form.get('CoapplicantIncome'))
        loan_amount=int(request.form.get('LoanAmount'))
        loan_amount_term=int(request.form.get('Loan_Amount_Term'))
        credit=int(request.form.get('Credit_History'))
        property_area=request.form.get('Property_Area')

        new_gender_transform=label_encoder.fit_transform([new_gender])
        new_married_sts_transform=label_encoder.fit_transform([new_married_sts])
        education_sts_transform=label_encoder.fit_transform([education_sts])
        self_emp_sts_transform=label_encoder.fit_transform([self_emp_sts])
        property_area_transform=label_encoder.fit_transform([property_area])

        # Prediction Process:-
        
        filename='loan_prediction_model.sav'
        loaded_model = pickle.load(open(filename, 'rb'))

        pickle_filename='label_encoder.sav'
        loaded_pickle_model = pickle.load(open(pickle_filename, 'rb'))

        prediction=(loaded_model.predict([[new_gender_transform[0],new_married_sts_transform[0],dependent_count,education_sts_transform[0],self_emp_sts_transform[0],applicant,co_applicant,loan_amount,loan_amount_term,credit,property_area_transform[0]]]))
        output=loaded_pickle_model.inverse_transform(prediction)[0]

        if output=='N':
            output='Loan Rejected'
        else:
            output='Loan Approved'

    return render_template('status.html',Gender=new_gender,Married=new_married_sts,Dependents=dependent_count,Education=education_sts,Self_Employed=self_emp_sts,ApplicantIncome=applicant,CoapplicantIncome=co_applicant,LoanAmount=loan_amount,Loan_Amount_Term=loan_amount_term,Credit_History=credit,Property_Area=property_area,status=output)


        

if __name__ == "__main__":
    app.run(debug=True)
    

##<form action="/log_in_details" method="post">

