from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.config['MAIL_SERVER'] = 'smtp.ethereal.email'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'bart.powlowski@ethereal.email'
app.config['MAIL_PASSWORD'] = 'r4AWvcX6WcbRcyGax5'
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@example.com'  

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

def send_registration_email(email):

    message = Message(subject='Registration Successful',
                      recipients=[email],
                      body='Thank you for registering. Your account has been successfully created.')

  
    with mail.connect() as smtp:
        smtp.send(message)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        
        user_email = request.form['email']
        send_registration_email(user_email)

        
        flash('Registration successful. Check your email for further instructions.', 'success')
        return redirect(url_for('registration_success'))

    return render_template('Register.html')

@app.route('/registration_success') 
def registration_success():
    return render_template('registration_success.html')  

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
       
        flash('Login successful. Welcome back!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('Login.html')

@app.route('/login_success')  
def dashboard():
    return render_template('login_success.html')  



if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

