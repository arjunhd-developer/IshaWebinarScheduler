from gsheet import Gspread, GSheetApi
import datetime as dt
from datetime import timezone
from data_structure import MainDataStructure, SliderDataStruct
from flask import render_template, session, redirect
from forms import WebinarRequestForm
from dateutil import parser as date_parser


class DataHandler:
    def __init__(self):
        self.main_data_base = []
        self.n1g_data_base = []
        self.n1tr_data_base = []
        self.data_set = []
        self.data_base = []
        self.master_data_set = []
        self.quote_data_set = []
        self.sheet = Gspread()
        self.main_data = self.sheet.main_data
        self.response = None
        self.today = dt.datetime.today().strftime("%d/%m/%Y")

    def struct_quote_data(self):
        self.response = None
        self.data_base = []
        self.sheet.sort_alpha()
        self.sheet.get_all_records()
        for data in self.main_data:
            if data['Date'] != "":
                date = dt.datetime.strptime(data['Date'], '%Y-%m-%d').strftime('%d/%m/%Y')
                month = data['Month']
                name = data['WebinarName']
                reg = data['Category']
                room = data['Room']
                start_time = data['StartTime']
                end_time = data['EndTime']
                year = data['Year']
                # year = dt.datetime.strptime(date, "%Y-%m-%d").strftime('%Y')
                data_obj = SliderDataStruct(date, month, name, reg, room,
                                            start_time, end_time, year)
                self.data_base.append(data_obj)

    def search_day(self):
        self.struct_quote_data()
        item_index = -1
        self.response = None
        self.quote_data_set = []
        self.master_data_set = []
        self.today = dt.datetime.today().strftime('%d/%m/%Y')

        for data in self.data_base:
            if data.date == self.today:
                item = {
                    "date": data.date,
                    "month": data.month,
                    "name": data.name,
                    "reg": data.reg,
                    "room": data.room,
                    "start_time": data.start_time,
                    "end_time": data.end_time
                }
                self.quote_data_set.append(item)
                item_index += 1
                if (item_index+1) % 12 == 0:
                    self.master_data_set.append(self.quote_data_set)
                    self.quote_data_set = []
        if self.quote_data_set != []:
            self.master_data_set.append(self.quote_data_set)
            self.quote_data_set = []

    def create_datetime_obj(self, date, start_t, end_t):
        session["date"] = date
        session["start_timestamp"] = dt.datetime.combine(date, start_t)
        session["end_timestamp"] = dt.datetime.combine(date, end_t)

    def struct_data_n1g(self):
        self.sheet = Gspread()
        self.n1g_data_base = []
        self.sheet.sort_alpha()
        self.sheet.get_n1g_records()
        for data in self.sheet.n1g_data:
            date = dt.datetime.strptime(data['Date'], "%Y-%m-%d").date()
            start_time = data['StartTime']
            end_time = data['EndTime']
            web_name = data['WebinarName']
            lang = data['Language']
            category = data['Category']
            room = data['Room']
            ishanga = data['ConductingIshanga']
            techsupport = data['TechSupport']
            platform = data['Platform']
            event_start = dt.datetime.strptime(data['EventStart'],
                                               "%d/%m/%Y %H:%M:%S")
            event_finish = dt.datetime.strptime(data['EventFinish'],
                                                "%d/%m/%Y %H:%M:%S")
            cal_entry_done = data['CalendarEntryDone']
            wapp_num = data['WhatsAppNumber']
            conf_msg_sent = data['ConfirmationMessageSent']
            month = data['Month']
            data_obj = MainDataStructure(
                date, start_time, end_time, web_name, lang, category, room,
                ishanga, techsupport, platform, event_start, event_finish,
                cal_entry_done, wapp_num, conf_msg_sent, month
            )
            self.n1g_data_base.append(data_obj)

    def struct_data_n1tr(self):
        self.sheet = Gspread()
        self.n1tr_data_base = []
        self.sheet.sort_alpha()
        self.sheet.get_n1tr_records()
        for data in self.sheet.n1tr_data:
            date = dt.datetime.strptime(data['Date'], "%Y-%m-%d").date()
            start_time = data['StartTime']
            end_time = data['EndTime']
            web_name = data['WebinarName']
            lang = data['Language']
            category = data['Category']
            room = data['Room']
            ishanga = data['ConductingIshanga']
            techsupport = data['TechSupport']
            platform = data['Platform']
            event_start = dt.datetime.strptime(data['EventStart'],
                                               "%d/%m/%Y %H:%M:%S")
            event_finish = dt.datetime.strptime(data['EventFinish'],
                                                "%d/%m/%Y %H:%M:%S")
            cal_entry_done = data['CalendarEntryDone']
            wapp_num = data['WhatsAppNumber']
            conf_msg_sent = data['ConfirmationMessageSent']
            month = data['Month']
            data_obj = MainDataStructure(
                date, start_time, end_time, web_name, lang, category, room,
                ishanga, techsupport, platform, event_start, event_finish,
                cal_entry_done, wapp_num, conf_msg_sent, month
            )
            self.n1tr_data_base.append(data_obj)

    def check_availability(self):
        self.response = None
        session["datetext"] = dt.datetime.strftime(
            date_parser.parse(session["date"]), "%d/%m/%Y"
        )
        session["web_start_text"] = dt.datetime.strftime(
            session["start_timestamp"], "%H:%M %p"
        )
        session["web_start"] = dt.datetime.strptime(dt.datetime.strftime(
            session["start_timestamp"], "%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S"
        )
        session["web_end_text"] = dt.datetime.strftime(
            session["end_timestamp"], "%H:%M %p"
        )
        session["web_end"] = dt.datetime.strptime(dt.datetime.strftime(
            session["end_timestamp"], "%Y-%m-%d %H:%M:%S"),
            "%Y-%m-%d %H:%M:%S"
        )
        session["n1g_available"] = None
        session["n1tr_available"] = None
        session["n1g_status"] = ""
        session["n1tr_status"] = ""
        n1g_conflict_counter = 0
        n1tr_conflict_counter = 0
        session['date'] = date_parser.parse(session["date"]).date()
        if session['date'] >= dt.datetime.today().date():
            for webinar in self.n1g_data_base:
                if webinar.date == session["date"]:
                    if session["web_start"] >= webinar.event_finish + \
                            dt.timedelta(minutes=58):
                        n1g_conflict_counter += 0
                    elif session['web_end'] <= webinar.event_start - \
                            dt.timedelta(minutes=58):
                        n1g_conflict_counter += 0
                    else:
                        n1g_conflict_counter += 1
                else:
                    n1g_conflict_counter += 0
            for webinar in self.n1tr_data_base:
                if webinar.date == session["date"]:
                    if session["web_start"] >= webinar.event_finish + \
                            dt.timedelta(minutes=58):
                        n1tr_conflict_counter += 0
                    elif session['web_end'] <= webinar.event_start - \
                            dt.timedelta(minutes=58):
                        n1tr_conflict_counter += 0
                    else:
                        n1tr_conflict_counter += 1
                else:
                    n1tr_conflict_counter += 0

            if n1g_conflict_counter > 0:
                session["n1g_available"] = False
                session["n1g_status"] = "Nalanda 1 Glass Room is Unavailable !"
            else:
                session["n1g_available"] = True
                session["n1g_status"] = "Nalanda 1 Glass Room is Available !"

            if n1tr_conflict_counter > 0:
                session["n1tr_available"] = False
                session["n1tr_status"] = "Nalanda 1 Training Room is Unavailable !"
            else:
                session["n1tr_available"] = True
                session["n1tr_status"] = "Nalanda 1 Training Room is Available !"

            self.response = render_template(
                'search_results.html',
                g_status=session["n1g_available"],
                g_status_text=session["n1g_status"],
                tr_status=session["n1tr_available"],
                tr_status_text=session["n1tr_status"],
                date=session["datetext"],
                start_t=session["web_start_text"],
                end_t=session["web_end_text"]
            )
        else:
            self.response = render_template(
                'bygonedate.html'
            )

    def webinar_form_struct_data(self, room):
        self.response = None
        web_form = WebinarRequestForm()
        if room == "pass":
            session['email'] = web_form.email.data
            session['zone'] = web_form.zone.data
            session['organisation'] = web_form.org.data
            if dict(web_form.module_name.choices).get(
                web_form.module_name.data
            ) == "Other Module":
                session['module_name'] = web_form.other_module.data
            else:
                session['module_name'] = \
                    dict(web_form.module_name.choices).get(
                        web_form.module_name.data
                    )
            if dict(web_form.language_name.choices).get(
                web_form.language_name.data
            ) == "Other Language":
                session['language'] = web_form.other_language.data
            else:
                session['language'] = dict(web_form.language_name.choices).get(
                    web_form.language_name.data
                )
            if dict(web_form.platform_name.choices).get(
                web_form.platform_name.data
            ) == "Other Platform":
                session['platform'] = web_form.other_platform.data
            else:
                session['platform'] = dict(web_form.platform_name.choices).get(
                    web_form.platform_name.data
                )
            session['conducting_ishanga'] = web_form.cond_ish.data
            session['program_name'] = web_form.prog_name.data
            if dict(web_form.channel_name.choices).get(
                web_form.channel_name.data
            ) == "Other Channel":
                session['channel'] = web_form.other_channel.data
            else:
                session['channel'] = dict(web_form.channel_name.choices).get(
                    web_form.channel_name.data
                )
            session['need_tech'] = dict(web_form.need_tech.choices).get(
                    web_form.need_tech.data
            )
            print(web_form.need_tech.data)
            session['mats_need'] = web_form.mat_need.data
            session['req_person'] = web_form.req_person.data
            session['comments'] = web_form.comments.data
            session['whatsapp_num'] = web_form.wa_num.data
            self.response = redirect('request_process')
        else:
            if room == "n1g":
                session['room_select'] = "Nalanda 1 Glass Room"
            elif room == "n1tr":
                session['room_select'] = "Nalanda 1 Training Room"
            elif room == "other":
                session['room_select'] = "Other Rooms"
            self.response = render_template(
                'webinar_req_form.html',
                form=web_form,
                render_kw={'onchange': "myFunction()"},
                date=session['date'],
                start=session['web_start'],
                end=session['web_end'],
                room_select=session['room_select']
            )

    def webinar_form_process(self):
        self.data_set = []
        sheet = GSheetApi()
        date = dt.datetime.strftime(
            date_parser.parse(session["date"]), "%d/%m/%Y"
        )
        start_time = session['web_start']
        end_time = session['web_end']
        room_select = session['room_select']
        email = session['email']
        zone = session['zone']
        org = session['organisation']
        module = session['module_name']
        language = session['language']
        platform = session['platform']
        cond_ishanga = session['conducting_ishanga']
        prog_name = session['program_name']
        channel = session['channel']
        need_tech = session['need_tech']
        mats_needed = session['mats_need']
        req_person = session['req_person']
        wa_num = session['whatsapp_num']
        comments = session['comments']
        self.data_set = [
            date, start_time, end_time, room_select, email, zone, org, module,
            language, platform, cond_ishanga, prog_name, channel, need_tech,
            mats_needed, req_person, wa_num, comments
        ]
        sheet.write_data(self.data_set)
