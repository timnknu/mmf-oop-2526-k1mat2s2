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

def convert_value(s, currency_to):
    d = s.split()  # ["50.5", "EUR"]
    v = float(d[0])
    k = (d[1], currency_to)
    v_new = v * rates[k]
    return v_new