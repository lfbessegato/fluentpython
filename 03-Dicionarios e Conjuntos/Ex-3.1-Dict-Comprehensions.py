DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonésia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigéria'),
    (7, 'Rússia'),
    (81, 'Japan')
]
country_code = {country: code for code, country in DIAL_CODES}
print(country_code)

print({code: country.upper() for country, code in country_code.items()
    if code < 66})
