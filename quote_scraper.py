from bs4 import BeautifulSoup
import requests as rq


class QuoteScraper:
    def __init__(self):
        self.header = {'user-agent': 'Mozilla/5.0'}
        self.quote_date = None
        self.quote_pic = None
        self.quote_text = None

    def get_quote(self):
        isha_resp = rq.get(
            "https://isha.sadhguru.org/in/en/wisdom/type/quotes",
            headers=self.header
        )
        site_data = isha_resp.text
        today_quote_url = None

        main_soup = BeautifulSoup(site_data, "lxml")
        all_data = main_soup.findAll(
            id="views-bootstrap-wisdom-grid-view-block-8"
        )
        for item in all_data:
            today_quote_url = item.a["href"]

        quote_page_resp = rq.get(today_quote_url, headers=self.header)
        quote_data = quote_page_resp.text

        quote_soup = BeautifulSoup(quote_data, "lxml")
        self.quote_date = quote_soup.find(
            class_="isha-daily-mystic-quote-title h1-head-quote"
        )
        # print(self.quote_date.text)

        self.quote_pic = quote_soup.find(class_="img-responsive")
        # print(self.quote_pic['src'])

        self.quote_text = quote_soup.find(
            class_="quote-cards quote-table-cell quote-table-content"
        )
        # print(self.quote_text.div.text.strip())
