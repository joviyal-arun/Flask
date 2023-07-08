from flask import *
import pandas as pd

# url='http://127.0.0.1:5000'

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home_page.html')

@app.route("/sign_in_details", methods=['POST', 'GET'])
def sign_in():
    return render_template('sign_in.html')


@app.route("/log_in_details", methods=['POST', 'GET'])
def log_in():
    return render_template('log_in.html')


@app.route("/sign_in_parameters", methods=['POST', 'GET'])
def sign_in_parameters():
    
    output_dictionary={}
    
    if request.method == 'POST':
        
        first_name = request.form.get('firstname')
        last_name = request.form.get('lastname')
        mobile_number = request.form.get('mobilenumber')
        email = request.form.get('email')
        psw = request.form.get('psw')
        psw_repeat = request.form.get('psw-repeat')
        
        output_dictionary['first_name']=first_name
        output_dictionary['last_name']=last_name
        output_dictionary['mobile_number']=mobile_number
        output_dictionary['email']=email
        output_dictionary['psw']=psw
        output_dictionary['psw_repeat']=psw_repeat
        output_dictionary['main_balance']=1000

        df=pd.DataFrame(output_dictionary, index=[0])
        df.to_csv('sign_details.csv')

        return render_template('home_page.html')


@app.route("/log_in_parameters", methods=['POST', 'GET'])
def log_in_parameters():
    if request.method == 'POST':
        mobile_number=request.form.get('mobilenumber')
        psw=request.form.get('psw')

        df=pd.read_csv('sign_details.csv')
        sign_password=df['psw'][0]

        if psw==sign_password:
            return render_template('services.html')
        else:
            return redirect(url_for('log_in'))  

@app.route('/profile',methods=['POST','GET'])
def profile():
    df=pd.read_csv('sign_details.csv')
    first_name=df['first_name'][0]
    last_name=df['last_name'][0]
    full_name=first_name+' '+last_name
    mail_id=df['email'][0]
    mobile_number=df['mobile_number'][0]
    main_balance=df['main_balance'][0]

    return render_template('profile.html',name=full_name,mail_id=mail_id,mobile_number=mobile_number,balance=main_balance)


@app.route('/balance',methods=['POST','GET'])
def balance():
    df=pd.read_csv('sign_details.csv')
    main_balance=df['main_balance'][0]
    return render_template('balance.html',main_balance=main_balance)


@app.route('/deposit',methods=['POST','GET'])
def deposit():
    return render_template('amount_deposit.html')


@app.route('/amount_deposit_details',methods=['POST','GET'])
def amount_deposit_details():
    if request.method == 'POST':
        deposit_amount=int(request.form.get('deposit_amount'))
        df=pd.read_csv('sign_details.csv')
        main_balance=df['main_balance'][0]
        addition_operation=main_balance+deposit_amount
        df['main_balance']=addition_operation
        df.to_csv('sign_details.csv')
        return render_template('display_deposit_amount.html',deposit_amount=deposit_amount,balance=addition_operation)

@app.route('/with_draw',methods=['POST','GET'])
def with_draw():
    return render_template('amount_withdraw.html')

@app.route('/amount_with_draw_details',methods=['POST','GET'])
def amount_with_draw_details():
    if request.method == 'POST':
        with_draw_amount=int(request.form.get('with_draw_amount'))
        df=pd.read_csv('sign_details.csv')
        main_balance=df['main_balance'][0]
        sub_operation=main_balance-with_draw_amount
        df['main_balance']=sub_operation
        df.to_csv('sign_details.csv')
        return render_template('display_with_draw_amount.html',with_draw_amount=with_draw_amount,balance=sub_operation)

@app.route("/service_parameters", methods=['POST', 'GET'])
def service_parameters():
    if request.method == 'POST':
        service=request.form.get('radio')
        if service =='Deposit':
            return redirect(url_for('deposit'))
        elif service=='Withdraw':
            return redirect(url_for('with_draw'))
        elif service=='Profile':
            return redirect(url_for('profile'))
        elif service=='Exit':
            return redirect(url_for('homepage'))
        elif service=='Balance':
            return redirect(url_for('balance'))

        
if __name__ == "__main__":
    app.run(debug=True)


