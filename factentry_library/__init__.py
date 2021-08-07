def isin_validator(a):
    a = str(a)
    isin_codes = ['DZ', 'AO', 'AR', 'AW', 'AU', 'AT', 'BS', 'BH', 'BB', 'BE', 'BZ', 'BM', 'BO', 'BA', 'BW', 'BR', 'VG', 'BG', 'CM', 'CA', 'KY', 'GG', 'CL', 'CN', 'CI', 'CO', 'CR', 'HR', 'CU', 'CY', 'CZ', 'DK', 'DO', 'EC', 'EG', 'SV', 'EE', 'FJ', 'FI', 'FR', 'DE', 'GH', 'GI', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JO', 'KZ', 'KW', 'LV', 'LB', 'LR', 'LI', 'LT', 'LU', 'MO', 'MK', 'MW', 'MY', 'MT', 'MH', 'MU', 'MX', 'MN', 'MA', 'NL', 'AN', 'NZ', 'NI', 'NG', 'NO', 'OM', 'PK', 'PA', 'PE', 'PH', 'PL', 'PT', 'QA', 'MD', 'RO', 'RU', 'SA', 'SC', 'SG', 'SK', 'SI', 'ZA', 'ES', 'LK', 'EU', 'SZ', 'SE', 'CH', 'TW', 'TH', 'TT', 'TN', 'TR', 'UA', 'AE', 'GB', 'US', 'UY', 'VE', 'VN', 'ZM', 'KE', 'BD', 'AL', 'BY', 'AZ', 'UG', 'GE', 'GM', 'PG', 'YE', 'AM', 'KG', 'TJ', 'PY', 'TZ', 'RW', 'CG', 'KH', 'WS', 'NA', 'SY', 'LS', 'JE', 'MZ', 'SL', 'TG', 'UZ', 'VC', 'LA', 'SR', 'ML', 'GN', 'MC', 'GA', 'KN', 'NP', 'LC', 'TL', 'CF', 'TD', 'AG', 'GY', 'AD', 'CG', 'CI', 'ST', 'HT', 'SB', 'NE', 'LY', 'ET', 'BN', 'BJ', 'MM', 'MP', 'MV', 'GD', 'AF', 'BF', 'SD', 'SN', 'ER', 'MG', 'AI', 'ME', 'CW', 'VU', 'VI', 'ZW', 'NC', 'CV', 'CK', 'GU', 'NR', 'BT', 'GL', 'GW', 'KR', 'KR', 'RS', 'MR', 'TC', 'SM', 'TM', 'TO', 'XS']
    isin_code = a[:2]
    if isin_code not in [x for x in isin_codes]:
        return False

    if len(a) != 12 or not all(c.isalpha() for c in a[:2]) or not all(c.isalnum() for c in a[2:]):
        return False
    s = "".join(str(int(c, 36)) for c in a)
    return (sum(sum(divmod(2 * (ord(c) - 48), 10)) for c in s[-2::-2]) +
            sum(ord(c) - 48 for c in s[::-2])) % 10 == 0