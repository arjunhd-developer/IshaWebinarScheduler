from flask import Flask, render_template, redirect
from forms import SearchForm, MaterialReqForm
from data_handler import DataHandler
from quote_scraper import QuoteScraper
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SECRET_KEY'] = 'kadkajdjasdfasjbdakshd'
data_h = DataHandler()


@app.route('/')
def home():
    quote = QuoteScraper()
    quote.get_quote()
    data_handler = DataHandler()
    data_handler.struct_quote_data()
    data_handler.search_day()
    date_today = data_handler.today
    return render_template(
        "home.html",
        quote_date=quote.quote_date.text,
        img_src=quote.quote_pic['src'],
        quote_text=quote.quote_text.div.text.strip(),
        master_data_set=data_handler.master_data_set,
        today=date_today
    )

@app.route('/calendar')
def calendar():
    return render_template("index.html")


@app.route('/search', methods=['GET', 'POST'])
def slot_search():
    global data_h
    form = SearchForm()
    if form.date.data is None:
        return render_template('search.html', form=form)
    elif form.validate_on_submit():
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


@app.route('/material_requests', methods=['GET', 'POST'])
def mat_req():
    global data_h
    data_h.material_form = MaterialReqForm()
    if data_h.material_form.poc_name.data is None:
        return render_template('mat_req_form.html', form=data_h.material_form)
    elif data_h.material_form.validate_on_submit():
        data_h.create_mat_req_obj(
            data_h.material_form.poc_name.data,
            data_h.material_form.mats.data,
            data_h.material_form.borrow_date.data,
            data_h.material_form.return_date.data,
            data_h.material_form.poc_wa_num.data
        )
        data_h.mat_req_struct_data()
        return redirect('mats_proc')


@app.route('/mats_proc', methods=['GET', 'POST'])
def mats_processed():
    global data_h
    data_h.submit_mat_req()
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
