rates = {
    ('USD', 'UAH'): 36.9,
    ('USD', 'USD'): 1.0,
    ('USD', 'EUR'): 36.9/39.5,

    ('EUR', 'UAH'): 39.5,
    ('EUR', 'USD'): 39.5/36.9,
    ('EUR', 'EUR'): 1.0,

    ('UAH', 'USD'): 1.0,
    ('UAH', 'USD'): 1/36.9,
    ('UAH', 'EUR'): 1/39.5,
}

class InvalidFormatError(BaseException):
    pass

class UnknownCurrencyError(BaseException):
    pass

class NegativeAmountError(BaseException):
    pass

def convert_value(s, currency_to):
    d = s.split()  # ["50.5", "EUR"]
    if len(d) != 2:
        raise InvalidFormatError
    try:
        v = float(d[0])
    except:
        raise InvalidFormatError
    if v < 0:
        raise NegativeAmountError

    k = (d[1], currency_to)
    if k not in rates.keys():
        raise UnknownCurrencyError

    v_new = v * rates[k]
    return v_new

