# Google Autosuggestion Scraper

## Overview
This repository contains a Python script for scraping Google Autosuggestions. It was developed as part of the 4Beats INTERN TA & DevOps Q1 Solution. 

**Author:** Alina Hasan

## Prerequisites

- **Python**: Ensure you have Python installed on your system.
- **Firefox Browser**: The script uses Firefox as the browser for automation.
- **Geckodriver**: The script requires `geckodriver` to interface with Firefox. Ensure `geckodriver` is located in the same directory as the script or is in your system PATH.

## Libraries

- **Selenium**: For web automation and scraping.
- **openpyxl**: For handling Excel files.

## Setup

1. **Install Dependencies**: Install the required Python libraries using pip:
   ```bash
   pip install selenium openpyxl
   ```
   
2. **Download Geckodriver**:
     - Download the appropriate version of geckodriver for your operating system from [Geckodriver Releases](https://sourceforge.net/projects/geckodriver.mirror/). *A [Gecko release](Setup/geckodriver-v0.35.0-win32.zip)(https://github.com/20101301-Alina-Hasan/Google-Autosuggestion-Scraper/blob/a66e204726958993695030c32013ed7546a11fe9/Setup/geckodriver-v0.35.0-win32.zip) is also provided in the 'Setup' folder of this repository*
     - Place geckodriver in the same directory as the script or add it to your system PATH.

3. **Firefox Installation**:
     - Ensure Firefox is installed on your system. *A [Firefox Installer.exe](https://github.com/20101301-Alina-Hasan/Google-Autosuggestion-Scraper/blob/3908fbad28833fc1951bcd7931e20678b6bf37fa/Setup/Firefox%20Installer.exe) is available in the 'Setup' folder of this repository.*

4. **Jupyter Notebook**:
     - Open the provided Jupyter Notebook file in a Jupyter environment to run the script. The notebook demonstrates the functionality and provides instructions for use.

*A Sample Output is provided in the 'Sample Output' folder*
