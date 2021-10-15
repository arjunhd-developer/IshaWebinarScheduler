class MainDataStructure:
    def __init__(
            self, date, start_time, end_time, web_name, lang, category, room,
            ishanga, techsupport, platform, event_start, event_finish,
            cal_entry_done, wapp_num, conf_msg_sent, month
    ):
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.web_name = web_name
        self.lang = lang
        self.category = category
        self.room = room
        self.ishanga = ishanga
        self.techsupport = techsupport
        self.platform = platform
        self.event_start = event_start
        self.event_finish = event_finish
        self.cal_entry_done = cal_entry_done
        self.wapp_num = wapp_num
        self.conf_msg_sent = conf_msg_sent
        self.month = month


class DateTimeStructure:
    def __init__(self, date, start_t, end_t):
        self.date = date
        self.start_time = start_t
        self.end_time = end_t

class SliderDataStruct:
    def __init__(self, in_date, in_month, in_name, in_reg, in_room,
                 in_starttime, in_endtime, in_year):
        self.date = in_date
        self.month = in_month
        self.name = in_name
        self.reg = in_reg
        self.room = in_room
        self.start_time = in_starttime
        self.end_time = in_endtime
        self.year = in_year
