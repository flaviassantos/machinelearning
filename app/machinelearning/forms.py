


# class RegistrationForm(FlaskForm):
#     username = StringField(_l('Username'), validators=[DataRequired()])
#     email = StringField(_l('Email'), validators=[DataRequired(), Email()])
#     password = PasswordField(_l('Password'), validators=[DataRequired()])
#     password2 = PasswordField(
#         _l('Repeat Password'), validators=[DataRequired(),
#                                            EqualTo('password')])
#     submit = SubmitField(_l('Register'))
#
#     def validate_username(self, username):
#         user = User.query.filter_by(username=username.data).first()
#         if user is not None:
#             raise ValidationError(_('Please use a different username.'))
#
#     def validate_email(self, email):
#         user = User.query.filter_by(email=email.data).first()
#         if user is not None:
#           raise ValidationError(_('Please use a different email address.'))