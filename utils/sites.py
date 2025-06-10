from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def generate_search_links(title, site):
    if site != 'Indeed':
        return []  # Only Indeed implemented for now

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    encoded_title = title.replace(' ', '+')
    url = f"https://sg.indeed.com/jobs?q={encoded_title}&fromage=7"
    driver.get(url)
    time.sleep(2)  # Wait for page to load

    jobs = []
    job_cards = driver.find_elements(By.CSS_SELECTOR, 'a.tapItem')
    for card in job_cards[:30]:  # Limit to 30 jobs
        try:
            job_title = card.find_element(By.CSS_SELECTOR, 'h2.jobTitle').text
            company = card.find_element(By.CSS_SELECTOR, 'span.companyName').text
            location = card.find_element(By.CSS_SELECTOR, 'div.companyLocation').text
            link = card.get_attribute('href')
            description = card.text
            jobs.append({
                'title': job_title,
                'company': company,
                'location': location,
                'source': 'Indeed',
                'link': link,
                'description': description
            })
        except Exception:
            continue

    driver.quit()
    return jobs

def generate_search_links_old(title, site):
    import urllib.parse
    encoded = urllib.parse.quote_plus(title)
    
    if site == 'LinkedIn':
        return [
            {'title': title, 'company': 'ExampleCo', 'location': 'Singapore', 'source': 'LinkedIn', 'link': f"https://www.linkedin.com/jobs/search/?f_TPR=r604800&geoId=102454443&keywords={encoded}", 'description': f'{title} opportunity in logistics'},
            {'title': title, 'company': 'AnotherCo', 'location': 'Malaysia', 'source': 'LinkedIn', 'link': 'https://www.linkedin.com/jobs/view/12345', 'description': f'{title} in sales and marketing'},
        ]
    elif site == 'Indeed':
        return [
            {
                'title': title,
                'company': 'IndeedCorp',
                'location': 'Singapore',
                'source': 'Indeed',
                'link': f"https://sg.indeed.com/jobs?q={encoded}&fromage=7",
                'description': f'{title} at a growing technology-forward logistics company.'
            },
            {
                'title': title,
                'company': 'TechLogix',
                'location': 'Singapore',
                'source': 'Indeed',
                'link': 'https://sg.indeed.com/viewjob?jk=12345',
                'description': f'{title} in sales and marketing for logistics.'
            }
        ]
    elif site == 'JobStreet':
        return [
            {
                'title': title,
                'company': 'JobStreet Ltd.',
                'location': 'Singapore',
                'source': 'JobStreet',
                'link': f"https://sg.jobstreet.com/{encoded}-jobs?daterange=7&sortmode=ListedDate",
                'description': f'{title} position with regional logistics responsibility.'
            },
            {
                'title': title,
                'company': 'AsiaFreight',
                'location': 'Malaysia',
                'source': 'JobStreet',
                'link': 'https://sg.jobstreet.com/viewjob?jk=67890',
                'description': f'{title} opportunity in supply chain management.'
            }
        ]
    return []
