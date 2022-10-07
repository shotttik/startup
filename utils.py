from automation.webdriver import Browser
from automation.config import config_browser
from bs4 import BeautifulSoup
import pandas as pd


class ParseGpuList:

    @staticmethod
    def parser():
        # Bad Idea btw its for example
        url = 'https://www.cashify.in/best-gpu-graphics-processing-unit-cards-ranking-list'
        browser_i = Browser(config_browser(), url)
        html = browser_i.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        gpu_rows = soup.find(
            'figure', {'class': 'wp-block-table'}).find_all('tr')[1:]  # skip header

        raw_data = {
            'Model': [],
            '3DMark Graphics Score': [],
            'Architecture': [],
            'Pixel Shaders': [],
            'Core speed': [],
            'Boost/Turbo': [],
            'Memory Speed': [],
            'Memory Type': [],
        }
        for row in gpu_rows:
            rows_d = row.find_all('td')[1:]
            for (r, d) in zip(rows_d, raw_data):
                raw_data[d].append(r.text)

        df = pd.DataFrame(raw_data, columns=['Model', '3DMark Graphics Score', 'Architecture',
                                             'Pixel Shaders', 'Core speed', 'Boost/Turbo', 'Memory Speed', 'Memory Type'])
        df.to_csv('automation/Resources/gpus_data.csv', index=False)
        browser_i.driver.quit()
