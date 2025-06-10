def keyword_match(title, description, filters, avoid_terms=None):
    text = (title + ' ' + description).lower()
    if avoid_terms:
        for avoid in avoid_terms:
            if avoid in text:
                return ''
    matches = [f for f in filters if f in text]
    return ', '.join(matches) if matches else ''
