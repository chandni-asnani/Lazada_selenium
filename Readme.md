# Selenium Scraper Project

This Selenium-based web scraper automates the process of extracting reviews from web page, leveraging the power of Selenium for browser automation.

## Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.6+**: The programming language used for the script.
- **pip**: The Python package installer.

## Installation

### Clone the Repository

First, clone the project repository to your local machine:

```bash
git clone https://your-repository-url.git
cd your-project-directory
```

### Set Up a Virtual Environment

(Optional, but recommended) Create and activate a virtual environment:

- **Unix/macOS**:

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- **Windows**:

  ```cmd
  python -m venv venv
  .\venv\Scripts\activate
  ```

### Install Dependencies

Install the necessary Python packages:

```bash
pip install -r requirements.txt
```

This will install Selenium and other dependencies defined in `requirements.txt`.

## Configuration

### Environment Variables

Copy the `.env.example` file to a new `.env` file and adjust it with your specific settings, such as API keys or database URLs:

```bash
cp .env.example .env
```

Edit `.env` with the appropriate values.

### Web Driver

Ensure you have the correct WebDriver for your browser (e.g., ChromeDriver for Chrome, geckodriver for Firefox). Update the path to the WebDriver and website url (for specific item reviews) in your `.env` file or script as needed.

## Running the Scraper

Execute the scraper with the following command:

```bash
python selenium_scraper.py
```

## Running the Scraper on Docker

Execute the scraper with the following command:

```bash
docker build -t selenium-scraper .
docker run selenium-scraper
```

## Additional Notes

- **Customization**: The script can be customized to fit specific scraping needs. Check the comments within the script for guidance.
- **Troubleshooting**: Ensure the WebDriver is up-to-date and compatible with your browser's version if you encounter issues.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your proposed changes.