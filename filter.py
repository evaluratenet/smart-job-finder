def keyword_match(title, description, filters):
    text = (title + ' ' + description).lower()
    matches = [f for f in filters if f in text]
    return ', '.join(matches) if matches else ''