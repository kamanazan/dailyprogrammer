from sys import stdin
month_dict = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05',
                'Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10',
                'Nov':'11','Dec':'12'}
def normalize_year(year):
    '''
    return year in 4 digit format
    '''
    if int(year) >= 50 and int(year) <=99:
        year = str(1900 + int(year))
    elif int(year) >=0 and int(year) <=49:
        year = str(2000 + int(year))

    return str(year).strip()

def normalize_date(dt):
    '''
    dt can be:

    yyyy-mm-dd
    mm/dd/yy
    mm#yy#dd
    dd*mm*yyyy
    (month word) dd, yy
    (month word) dd, yyyy
    
    valid year:
    1950 - 2049
    return date in yyyy-mm-dd format
    '''
    month = ''
    year = ''
    day = ''
    correct_dt = ''
    if dt.count('-'):
        #date in intended format
        year,month,day = dt.split('-')
        year = normalize_year(year)
    elif dt.count('/'):
        month,day,year = dt.split('/')
        year = normalize_year(year) 
    elif dt.count('#'):
        month,year,day = dt.split('#')
        year = normalize_year(year)
    elif dt.count('*'):
        day,month,year = dt.split('*')
    elif dt.count(' '):
        month,day,year = dt.split(' ')
        month = month_dict[month]
        day = day.strip(',')
        if len(year.strip()) == 2:
            year = normalize_year(year) 
    else:
        return 'unknown format:'+dt
    return '%s-%s-%s' % (year.strip(),month.strip(),day.strip())

for line in stdin:
    print normalize_date(line)
