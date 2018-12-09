from flask import Flask, render_template, session, redirect, url_for, flash, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SelectField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = "1234567890abcde"

class RegistrationForm(Form):
    name = StringField('Name', [validators.DataRequired()])
    physics = StringField('Physics')
    chemistry = StringField('Chemistry')
    maths = StringField('Maths')
    submit = SubmitField('등록')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    print(request.method)

    if request.method == 'POST' and form.validate():
        flash('Thanks for registering')
        result = request.form # 딕셔너리 포맷
        return render_template("result.html",result = result)
    else:
        # 초기값 설정
        form.name.data = '조종태'

        return render_template('register.html', form=form)

if __name__ == '__main__':
   app.run(debug = True)
