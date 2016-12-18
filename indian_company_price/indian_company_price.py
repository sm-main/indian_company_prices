import datetime
import dateutil.parser
import requests


def indian_company_price(company_symbol, start_date, end_date):
        start_date = dateutil.parser.parse(start_date).date().strftime('%Y-%m-%d')
        end_date = dateutil.parser.parse(end_date).date().strftime('%Y-%m-%d')
        url = 'https://www.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp?symbol=' + company_symbol + '&segmentLink=3&symbolCount=2&series=ALL&dateRange=+&fromDate=' + start_date + '&toDate=' + end_date + '&dataType=PRICEVOLUMEDELIVERABLE'
        r = requests.get(url)
        if r.status_code == 200:
                pass
