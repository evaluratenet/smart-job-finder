# README.md
# Smart Job Finder

A Python Flask-based tool that lets users search job titles across multiple job portals (LinkedIn, Indeed, JobStreet), filter results by keywords, and generate company summaries using OpenAI GPT.

## Features
- Multi-site job search (LinkedIn, Indeed, JobStreet)
- Keyword-based filtering
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

4. Set your OpenAI API key as an environment variable:
   ```bash
   # On Windows
   set OPENAI_API_KEY=your_key
   
   # On Unix/MacOS
   export OPENAI_API_KEY=your_key
   ```

5. Run the app:
   ```bash
   python app.py
   ```

## Deployment on Render

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
2. Enter keywords (one per line) in the second text area
3. Select which job sites to search
4. Click "Search Jobs" to view results

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.
