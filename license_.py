import re


def validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    pattern = re.compile('^PB-[A-Z0-9]{8}-[A-Z0-9]{8}-[A-Z0-9]{8}-[A-Z0-9]{8}$')
    match = pattern.match(key)
    return bool(match)



#pybites
def validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    return bool(
        re.match(r'^PB-[A-Z0-9]{8}(?:-[A-Z0-9]{8}){3}$', key)
    )