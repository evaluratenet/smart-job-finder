def generate_search_links(title, site):
    import urllib.parse
    encoded = urllib.parse.quote_plus(title)
    
    if site == 'LinkedIn':
        return [{
            'title': title,
            'company': 'ExampleCo',
            'location': 'Singapore',
            'source': 'LinkedIn',
            'link': f"https://www.linkedin.com/jobs/search/?f_TPR=r604800&geoId=102454443&keywords={encoded}",
            'description': title + ' opportunity in logistics or supply chain'
        }]
    elif site == 'Indeed':
        return [{
            'title': title,
            'company': 'IndeedCorp',
            'location': 'Singapore',
            'source': 'Indeed',
            'link': f"https://sg.indeed.com/jobs?q={encoded}&fromage=7",
            'description': title + ' at a growing technology-forward logistics company.'
        }]
    elif site == 'JobStreet':
        return [{
            'title': title,
            'company': 'JobStreet Ltd.',
            'location': 'Singapore',
            'source': 'JobStreet',
            'link': f"https://sg.jobstreet.com/{encoded}-jobs?daterange=7&sortmode=ListedDate",
            'description': title + ' position with regional logistics responsibility.'
        }]
    return []