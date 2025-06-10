# app.py
from flask import Flask, render_template, request
from utils.sites import generate_search_links
from utils.filter import keyword_match
from utils.openai_summary import get_company_summary

app = Flask(__name__)

# Domain configuration
DOMAIN = "sjf.evalurate.net"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        job_titles = request.form['job_titles'].splitlines()
        filter_terms = [term.strip().lower() for term in request.form['filter_terms'].splitlines() if term.strip()]
        selected_sites = request.form.getlist('sites')

        results = []
        for title in job_titles:
            for site in selected_sites:
                listings = generate_search_links(title.strip(), site)
                for listing in listings:
                    match = keyword_match(listing['title'], listing['description'], filter_terms)
                    summary = get_company_summary(listing['company'])
                    results.append({
                        **listing,
                        'filter_match': match,
                        'company_summary': summary
                    })

        return render_template('results.html', results=results)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
