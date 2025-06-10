# README.md
# Smart Job Finder

A Python Flask-based tool that lets users search job titles across multiple job portals (currently, real data from Indeed using Selenium), filter results by keywords, and generate company summaries using OpenAI GPT.

## Features
- Real job search from Indeed (via Selenium web scraping)
- Keyword-based filtering (positive and negative words)
- AI-powered company summaries using OpenAI GPT
- Clean, modern web interface

## Local Development Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/smart-job-finder.git
   cd smart-job-finder
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install ChromeDriver (for Selenium):**
   - Download ChromeDriver from: https://sites.google.com/chromium.org/driver/
   - Make sure the version matches your installed Chrome browser.
   - Extract `chromedriver.exe` (Windows) or `chromedriver` (Mac/Linux).
   - Move it to a folder, e.g., `C:\tools\chromedriver\`.
   - Add that folder to your system PATH:
     - Windows: Edit the `Path` variable in Environment Variables and add `C:\tools\chromedriver\`.
     - Mac/Linux: Move to `/usr/local/bin/` and run `sudo chmod +x /usr/local/bin/chromedriver`.
   - Test by running `chromedriver --version` in a new terminal.

5. Set your OpenAI API key as an environment variable:
   ```bash
   # On Windows
   set OPENAI_API_KEY=your_key
   
   # On Unix/MacOS
   export OPENAI_API_KEY=your_key
   ```

6. Run the app:
   ```bash
   python app.py
   ```

## Filtering Logic
- The app searches Indeed using only the job title(s) you enter.
- After retrieving jobs, it filters them:
  - **Positive words:** Only include jobs containing at least one of these words (in title or description).
  - **Negative words:** Exclude jobs containing any of these words (in title or description).
  - Filtering is case-insensitive.

## Deployment on Render

### Note
- Selenium/ChromeDriver setup on Render requires extra configuration and may not work out-of-the-box. For production, consider using an API if available.

### Automatic Deployment
1. Fork this repository to your GitHub account
2. Sign up for a [Render](https://render.com) account
3. Click "New +" and select "Web Service"
4. Connect your GitHub repository
5. Configure the service:
   - Name: smart-job-finder
   - Environment: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
6. Add environment variable:
   - Key: `OPENAI_API_KEY`
   - Value: Your OpenAI API key
7. Click "Create Web Service"

### Manual Deployment
1. Push your code to GitHub:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. Follow the automatic deployment steps above

## Usage
1. Enter job titles (one per line) in the first text area
2. Enter positive keywords (one per line) in the second text area
3. Enter negative keywords (one per line) in the third text area
4. Select which job sites to search (currently, only Indeed returns real data)
5. Click "Search Jobs" to view results

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.
