url = "https://bytebank.com/exchange?originCurrency=real&destinationCurrency=dolar&quantity=100"
print(url)

# separates the base and the parameters
sep_index = url.find('?')
url_base = url[:sep_index]
url_param = url[sep_index + 1:]
print(url_param)

# find the value of a parameter
param_search = 'originCurrency'
param_index = url_param.find(param_search)
value_index = param_index + len(param_search) + 1
index_e = url_param.find('&', value_index)

if index_e == -1:
    value = url_param[value_index:]
else:
    value = url_param[value_index:index_e]

print(value)
