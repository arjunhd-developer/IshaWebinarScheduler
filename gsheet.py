import gspread as gsp
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = [
    "https://spreadsheets.google.com/feeds",
    'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
SERVICE_ACCOUNT_FILE = 'google-credentials.json'
SPREADSHEET_ID = '13-GsSLnll2SxUpQYHcZWbQFNuj9EzOP-dfFvUJapKkg'

creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


class Gspread:
    def __init__(self):
        self.client = gsp.authorize(credentials=creds)
        self.main_sheet = self.client.open("Isha Webinar Scheduler - Updated").\
            worksheet("Main Sheet")
        self.n1g_sheet = self.client.open("Isha Webinar Scheduler - Updated"). \
            worksheet("N1G")
        self.n1tr_sheet = self.client.open("Isha Webinar Scheduler - Updated"). \
            worksheet("N1TR")
        self.main_data = self.main_sheet.get_all_records()
        self.n1g_data = self.n1g_sheet.get_all_records()
        self.n1tr_data = self.n1tr_sheet.get_all_records()

    def get_all_records(self):
        self.main_sheet = self.client.open("Isha Webinar Scheduler - Updated").\
            worksheet("Main Sheet")
        self.main_data = self.main_sheet.get_all_records()

    def get_n1g_records(self):
        self.n1g_sheet = self.client.open("Isha Webinar Scheduler - Updated"). \
            worksheet("N1G")
        self.n1g_data = self.n1g_sheet.get_all_records()

    def get_n1tr_records(self):
        self.n1tr_sheet = self.client.open("Isha Webinar Scheduler - Updated"). \
            worksheet("N1TR")
        self.n1tr_data = self.n1tr_sheet.get_all_records()

    def sort_alpha(self):
        self.main_sheet.sort((1, 'asc'))


class GSheetApi:
    def write_data(self, data):
        service = build('sheets', 'v4', credentials=creds)
        data_range = "'Webinar Requests'!B2"
        sheet = service.spreadsheets()
        entries = {"values": [data]}
        sheet.values().append(
            spreadsheetId=SPREADSHEET_ID,
            range=data_range,
            valueInputOption="USER_ENTERED",
            insertDataOption="INSERT_ROWS",
            body=entries
        ).execute()
