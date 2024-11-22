# Automated Job Application Script

This Python script leverages Selenium to automate the job application process on Reed.co.uk. Designed to simplify the repetitive and time-consuming steps of applying for jobs, this script empowers unemployed coders by streamlining the job hunt process, giving them more time to focus on refining their skills and preparing for interviews.

Features:

- Automated Sign-In: Logs into your Reed.co.uk account using your credentials securely stored in environment variables.
- Job Search Customization:
  - Automatically inputs your chosen keywords and location.
  - Option to filter for remote work jobs via a user prompt.
- Easy Apply Automation:
  - Locates and clicks "Easy Apply" buttons on job listings.
  - Navigates through multiple pages to apply for more opportunities.
- Work-from-Home Filter: Filters listings for remote jobs, reducing manual searches for remote-friendly roles.
- Error Handling: Robust error-catching ensures the script gracefully continues even when encountering minor issues.
- Scalability: Designed to be extended with new features or adjusted for other job platforms.

Motivation:

This project aims to assist unemployed coders by removing the monotony of repeatedly filling out job applications. By automating routine tasks, this script helps job seekers apply for more positions in less time, increasing their chances of landing the right opportunity.

Prerequisites:

- Python 3.7 or higher.
- Google Chrome browser.
- Environment file (.env) with the following variables:
  - email_address: Your Reed.co.uk account email.
  - password: Your account password.
  - keywords: Job-related keywords (e.g., "Python Developer").
  - location: Preferred job location (e.g., "London").

Installation:

1. Clone this repository:  
   `git clone https://github.com/pythonsnatcher/automatic_job_search.git`  
   `cd automatic_job_search`


2. Install dependencies:  
   `pip install -r requirements.txt`  

3. Create a `.env` file in the project root:  
   ```
   email_address=your_email@example.com  
   password=your_password  
   keywords="Python Developer"  
   location="London"  
   ```

4. Ensure you have Google Chrome installed. The script will automatically download and configure the required Chrome WebDriver using `webdriver-manager`.

Usage:

1. Run the script:  
   `reed_dot_com_auto_apply.py`

2. Follow the prompts:  
   - Specify whether you'd like to filter for remote work jobs.  
   - The script will log into your account, apply search filters, and systematically apply for jobs.  

3. Monitor the output for feedback on successfully applied jobs or any errors encountered.

Notes:

- Ensure your `.env` file is secure and does not contain sensitive information when sharing the script.
- The script currently supports Reed.co.uk but can be modified to work with other job boards.

Roadmap:

- Add support for other job platforms like LinkedIn, Indeed, and Glassdoor.
- Implement CAPTCHA-solving capabilities if required by certain platforms.
- Enhance logging and reporting features to provide users with detailed summaries of their applications.

Disclaimer:

This script is provided as-is and is intended for educational and personal use only. Use it responsibly and ensure it adheres to the terms of service of the job board platform.
