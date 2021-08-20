from flask import Flask, render_template, session, redirect
from forms import SearchForm
from data_handler import DataHandler
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SECRET_KEY'] = 'kadkajdjasdfasjbdakshd'
data_h = DataHandler()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/search', methods=['GET', 'POST'])
def slot_search():
    global data_h
    form = SearchForm()
    if form.date.data is None:
        return render_template('search.html', form=form)
    elif form.validate_on_submit():
        data_h = DataHandler()
        data_h.struct_data_n1g()
        data_h.struct_data_n1tr()
        data_h.create_datetime_obj(
            form.date.data,
            form.starttime.data,
            form.endtime.data
        )
        return redirect('searchresults')


@app.route('/searchresults', methods=['GET', 'POST'])
def search_results():
    global data_h
    data_h.check_availability()
    return data_h.response


@app.route('/webinar_requests/<room>', methods=['GET', 'POST'])
def webinar_req(room):
    global data_h
    data_h.webinar_form_struct_data(room)
    return data_h.response


@app.route('/webinar_requests/request_process', methods=['GET', 'POST'])
def request_process():
    global data_h
    data_h.webinar_form_process()
    return render_template("processed.html")


@app.route('/live_dash')
def live_dash():
    return render_template('live_dashboard.html')


if __name__ == "__main__":
    app.run(debug=True)
