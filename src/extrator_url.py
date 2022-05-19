class ExtractorUrl:

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


# extractor_url = ExtractorUrl("      ")
extractor_url = ExtractorUrl("https://bytebank.com/exchange?originCurrency=real&destinationCurrency=dolar&quantity=100")
quantity_value = extractor_url.get_parameter_value("quantity")
print(quantity_value)
