import re


class UrlExtractor:

    def __init__(self, url):
        self.url = self.sanitize_url(url)
        self.valid_url()

    def sanitize_url(self, url):
        if type(url) == str:
            return url.strip()
        return ""

    def valid_url(self):
        if not self.url:
            raise ValueError("URL is empty")

        url_pattern = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/exchange')
        match = url_pattern.match(self.url)

        if not match:
            raise ValueError('Invalid URL')

    def get_base_url(self):
        sep_index = self.url.find('?')
        url_base = self.url[:sep_index]
        return url_base

    def get_parameters_url(self):
        sep_index = self.url.find('?')
        url_param = self.url[sep_index + 1:]
        return url_param

    def get_parameter_value(self, param_search):
        param_index = self.get_parameters_url().find(param_search)
        value_index = param_index + len(param_search) + 1
        index_e = self.get_parameters_url().find('&', value_index)

        if index_e == -1:
            value = self.get_parameters_url()[value_index:]
        else:
            value = self.get_parameters_url()[value_index:index_e]

        return value

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + '\n' + 'Parameters: ' + self.get_parameters_url() + \
               '\n' + 'Base URL: ' + self.get_base_url()

    def __eq__(self, other):
        return self.url == other.url


# url_extractor = UrlExtractor("      ")
url_extractor = UrlExtractor("https://bytebank.com/exchange?originCurrency=real&destinationCurrency=dolar&quantity=100")
url_extractor2 = UrlExtractor("https://bytebank.com/exchange?originCurrency=real&destinationCurrency=dolar&quantity=100")
# print('URL length: ', len(url_extractor))
# print(url_extractor)

print(url_extractor == url_extractor2)

# quantity_value = url_extractor.get_parameter_value("quantity")
# print(quantity_value)


