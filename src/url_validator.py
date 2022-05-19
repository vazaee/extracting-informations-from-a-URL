# https://www.bytebank.com.br/exchange

import re

url = 'https://www.bytebank.com.br/exchange'
url_pattern = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/exchange')
match = url_pattern.match(url)

if not match:
    raise ValueError('Invalid URL')

print('Valid URL')
