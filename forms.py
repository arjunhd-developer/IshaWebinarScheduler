from flask_wtf import FlaskForm
from wtforms import SubmitField, validators, StringField, PasswordField, \
    SelectField, TextAreaField
from wtforms.fields.html5 import DateField, TimeField, EmailField


class SearchForm(FlaskForm):
    username = StringField(label='Username')
    password = PasswordField(label='Password')
    date = DateField(
        label='Enter Webinar Date',
        format='%Y-%m-%d',
        validators=(validators.DataRequired(),)
    )
    starttime = TimeField(
        label='Enter Starting Time',
        format='%H:%M',
        validators=(validators.DataRequired(),)
    )
    endtime = TimeField(
        label='Enter Ending Time',
        format='%H:%M',
        validators=(validators.DataRequired(),)
    )
    submit = SubmitField(label='Enter')


class MaterialReqForm(FlaskForm):
    borrow_date = DateField(
        label='Enter Borrow Date',
        format='%Y-%m-%d',
        validators=(validators.DataRequired(),)
    )
    return_date = DateField(
        label='Enter Return Date',
        format='%Y-%m-%d',
        validators=(validators.DataRequired(),)
    )
    poc_name = StringField(
        label='Enter POC Name :',
        validators=(validators.DataRequired(),)
    )
    mats = TextAreaField(
        label='What material do you need? (Ex: Laptop, '
              'webcam, Sadhguru photo, etc) Also specify '
              'the quantity of each item: ',
        validators=(validators.DataRequired(),)
    )
    poc_wa_num = StringField(
        label="POC's Whatsapp Number : ",
        validators=(validators.DataRequired(),)
    )
    submit = SubmitField(label='Enter')


class WebinarRequestForm(FlaskForm):
    zone = StringField(
        label='Enter Zone :',
        validators=(validators.DataRequired(),)
    )

    email = EmailField(
        label="Enter Your E-Mail ID : ",
        validators=(validators.DataRequired(), validators.Email(),)
    )

    module_name = SelectField(
        label='Select Module : ',
        choices=[
            ('choice1', 'Introduction to IE'),
            ('choice2', 'Yoga for Challenging Times'),
            ('choice3', 'Satsang'),
            ('choice4', 'Yoga for Immunity'),
            ('choice5', 'Yoga for respiratory health'),
            ('choice6', 'Equipping yourself for the Covid 19 era'),
            ('choice7', 'Shambhavi Q and A'),
            ('choice8', 'Shakti Chalana Kriya review'),
            ('choice9', 'Volunteers meet'),
            ('other_choice', 'Other Module')
        ],
        render_kw={'onchange': "myFunction()"}
    )
    other_module = StringField(
        label='Enter Other Module Name : ',
        validators=(validators.DataRequired(),)
    )

    language_name = SelectField(
        label='Select Language : ',
        choices=[
            ('choice1', 'English'),
            ('choice2', 'Tamil'),
            ('choice3', 'Hindi'),
            ('choice4', 'Malayalam'),
            ('choice5', 'Kannada'),
            ('choice6', 'Telugu'),
            ('choice7', 'Marathi'),
            ('choice8', 'Chinese(Cantonese)'),
            ('choice9', 'Chinese(Mandarin)'),
            ('choice10', 'Russian'),
            ('other_choice', 'Other Language')
        ],
        render_kw={'onchange': "myFunction()"},
        validators=(validators.DataRequired(),)
    )
    other_language = StringField(
        label='Enter Other Language Name : ',
        validators=(validators.DataRequired(),)
    )

    platform_name = SelectField(
        label='Select Platform : ',
        choices=[
            ('choice1', 'Youtube'),
            ('choice2', 'Google Meet'),
            ('choice3', 'MS Teams'),
            ('choice4', 'Webex'),
            ('choice5', 'Big Marker'),
            ('choice6', 'JW Player'),
            ('other_choice', 'Other Platform')
        ],
        render_kw={'onchange': "myFunction()"},
        validators=(validators.DataRequired(),)
    )
    other_platform = StringField(
        label='Enter Other Platform Name : ',
        validators=(validators.DataRequired(),)
    )

    channel_name = SelectField(
        label='Select Channel : ',
        choices=[
            ('choice1', 'Isha Foundation (Youtube)'),
            ('choice2', 'Regional Platform (Regional Youtube Channel)'),
            ('other_choice', 'Other Channel')
        ],
        render_kw={'onchange': "myFunction()"},
        validators=(validators.DataRequired(),)
    )
    other_channel = StringField(
        label='Enter Other Channel Name : ',
        validators=(validators.DataRequired(),)
    )

    need_tech = SelectField(
        label='Do you need Tech support? ',
        choices=[
            ('choice1', 'YES'),
            ('choice2', 'NO')
        ],
        validators=(validators.DataRequired(),)
    )

    org = StringField(
        label='Enter Organisation Name : ',
        validators=(validators.DataRequired(),)
    )

    cond_ish = StringField(
        label="Enter Conducting Ishanga's Name : ",
        validators=(validators.DataRequired(),)
    )

    prog_name = StringField(
        label='Enter Program Name : ',
        validators=(validators.DataRequired(),)
    )

    mat_need = TextAreaField(
        label='What material do you need? (Ex: Laptop, '
              'webcam, Sadhguru photo, etc) : ',
        validators=(validators.DataRequired(),)
    )

    req_person = StringField(
        label="Requesting Person Name : ",
        validators=(validators.DataRequired(),)
    )

    wa_num = StringField(
        label="Requesting Person's Whatsapp Number : ",
        validators=(validators.DataRequired(),)
    )

    comments = TextAreaField(label="Other Comments : ")

    submit_form = SubmitField(label='Submit')
