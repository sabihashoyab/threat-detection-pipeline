import ipinfo

ACCESS_TOKEN = '61f302ddf8aa00'
handler = ipinfo.getHandler(ACCESS_TOKEN)

def enrich_ip(ip):
    try:
        details = handler.getDetails(ip)
        return {
            'ip': ip,
            'city': details.city,
            'region': details.region,
            'country': details.country_name,
            'org': details.org
        }
    except:
        return {
            'ip': ip,
            'city': None,
            'region': None,
            'country': None,
            'org': None
        }
