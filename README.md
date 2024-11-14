

# Cricket Match Scraping System

## Project Overview

This project is designed to scrape and monitor cricket match schedules and related data from [CREX](https://crex.live/fixtures/match-list). It extracts and tracks information from the following sections:
- **Match Info**
- **Squads**
- **Live Updates**
- **Scorecard**

The system automatically triggers individual match scraping jobs for real-time data when a match starts.

## Features

- **Automated Scraping System**: Monitors and extracts match schedules and details.
- **Real-Time Data Extraction**: Starts individual scraping jobs for "Live" and "Scorecard" data when matches begin.
- **Comprehensive Data Handling**: Handles edge cases and ensures relevant data is accurately organized.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Sarthakk0/crix_web_scrapper.git
   ```
2. Navigate to the project directory:
   ```bash
   cd crix_websc
   ```
3. Run the scraping system:
   ```bash
   python main.py
   ```

## Assessment Criteria Met

- **Handling of Edge Cases**: The system includes extensive error handling and edge-case management to ensure reliable scraping.
- **Efficient Resource Usage**: Optimized codebase and memory management.
- **Well-Structured Output Data**: Output data is neatly organized for easy parsing and processing.

## Potential Improvements

Given more time, improvements such as increased scraping efficiency, support for additional data points, and further resource optimization would be considered.

