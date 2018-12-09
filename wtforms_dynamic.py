from flask import Flask, render_template, session, redirect, url_for, flash, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SelectField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = "1234567890abcde"

class RegistrationForm(Form):
    name = StringField('Name', [validators.DataRequired()])
    physics = StringField('Physics')
    chemistry = StringField('Chemistry')
    maths = StringField('Maths')
    private_info_use = BooleanField('개인정보 사용에 동의', [validators.DataRequired()])
    # submit = SubmitField('등록')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # 동적으로 폼의 항목을 추가
    setattr(RegistrationForm, 'address', StringField('address'))
    setattr(RegistrationForm, 'geonsu',SelectField(u'Geonsu',
        choices=[('0', '0건'), ('10', '10건'), ('20', '20건'), ('30', '30건')]))
    setattr(RegistrationForm, 'submit', SubmitField('등록'))

    form = RegistrationForm(request.form)
    print(request.method)

    if request.method == 'POST' and form.validate():
        flash('Thanks for registering')
        result = request.form # 딕셔너리 포맷
        return render_template("result.html",result = result)
    else:
        # 초기값 설정
        form.name.data = '조종태'
        form.private_info_use.data = True
        form.geonsu.data = '10'

        return render_template('register.html', form=form)

if __name__ == '__main__':
   app.run(debug = True)
