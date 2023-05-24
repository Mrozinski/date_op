from datetime import datetime 

def date_diff(date_1, date_2, date_format="%d%m%Y"):
    """
    Returns tete difference in days
    Input: 
        date_1
        date_2
    Output: 
        date_diff : Int 
    """
    a = datetime.strptime(date_1, date_format)
    b = datetime.strptime(date_2, date_format)
    return((b - a).days)

def date_check(d, date_format="%d%m%Y"):
    dig_count = sum(c.isdigit() for c in d)
    if dig_count != 8:
        return False
    try: 
        res= bool(datetime.strptime(d, date_format))
        return True
    except ValueError:
        return False