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
        today_quote_url = "https://isha.sadhguru.org/in/en/wisdom/quotes/date/december-19-2021"

        main_soup = BeautifulSoup(site_data, "lxml")
        all_data = main_soup.findAll(
            class_="chakra-text css-1b9xz4"
        )
        print(all_data)
        # for item in all_data:
        # today_quote_url = all_data[0].a["href"]

        quote_page_resp = rq.get(today_quote_url, headers=self.header)
        quote_data = quote_page_resp.text
        print(quote_data)

        quote_soup = BeautifulSoup(quote_data, "lxml")
        self.quote_date = quote_soup.find(
            class_="css-lloxk7"
        )
        # print(self.quote_date.text)

        # self.quote_pic = quote_soup.find(class_="css-1p3o1x6")
        self.quote_pic = "https://images.sadhguru.org/d/46272/1639870212-dec-19-20160721slh0190-e.jpg"
        # print(self.quote_pic['src'])

        self.quote_text = quote_soup.find(
            class_="css-6th7md"
        )
        # print(self.quote_text.div.text.strip())
