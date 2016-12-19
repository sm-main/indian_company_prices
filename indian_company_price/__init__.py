import datetime
import dateutil.parser
import requests
from bs4 import BeautifulSoup

def indian_company_price(company_symbol, start_date, end_date):
        start_date = dateutil.parser.parse(start_date).date().strftime('%d-%m-%Y')
        end_date = dateutil.parser.parse(end_date).date().strftime('%d-%m-%Y')
        url = 'https://www.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp?symbol=' + company_symbol + '&segmentLink=3&symbolCount=2&series=ALL&dateRange=+&fromDate=' + start_date + '&toDate=' + end_date + '&dataType=PRICEVOLUMEDELIVERABLE' 
        r = requests.get(url)
        if r.status_code == 200:
                bsObj = BeautifulSoup(r.text, "html5lib")
                bs_filter = bsObj.findAll('tr')[1:]
                bs_rows = [x.findAll('td', {"class":["number", "date"]}) for x in bs_filter]
                e = []
                for x in bs_rows:
                        j = []
                        for y in x:
                                j.append(y.get_text())
                        e.append(j)
                return e
        else:
                print r.status_code

print(indian_company_price('TCS', '01-12-2016', '20-12-2016'))

