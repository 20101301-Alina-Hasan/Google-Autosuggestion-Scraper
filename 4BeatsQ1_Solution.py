import time
import openpyxl
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

sheets = pd.read_excel("4BeatsQ1.xlsx", sheet_name=None)  # Read all sheets
sheet = datetime.now().strftime('%A')  # Returns full day name (e.g. 'Friday') 
# sheet ='Sunday'
# sheet ='Monday'
# sheet ='Tuesday'
# sheet ='Wednesday'
# sheet ='Thursday'
# sheet ='Friday'
# sheet ='Saturday'
df = sheets[sheet]

df = df.drop(columns=['Unnamed: 0'])  # Drop column where all elements are NaN
df.columns = ['Keyword', 'Value', 'Longest Option', 'Shortest Option']  # Label columns for better readability
# Check if "Keyword" is present in the first row (For sheets like Tuesday)
if not any(cell.startswith('Keyword') for cell in df.iloc[0].astype(str).values):
    df = df.drop(df.index[0])  # Remove row with partial/old labels
# Reset index of the DataFrame to ensure the indices align
df.reset_index(drop=True, inplace=True)

keywords = df['Value'].dropna().tolist()

def get_auto_suggestions(browser):
    elements = browser.find_elements(By.XPATH, '//*[@id="Alh6id"]/div[1]/div/ul/li')
    suggestions = [elem.text for elem in elements if elem.text]
    return suggestions

browser = webdriver.Firefox() 
browser.maximize_window()  
browser.get('http://www.google.com')
assert 'Google' in browser.title

for index, keyword in enumerate(keywords):
    elem = browser.find_element(By.NAME, 'q')  
    elem.clear()  # Clear search box of any previous search keywords
    elem.send_keys(keyword)  
    
    time.sleep(3)  # Allow autocomplete suggestions to load

    suggestions_list = get_auto_suggestions(browser)
    
    if suggestions_list:
        longest_option = max(suggestions_list, key=len)
        shortest_option = min(suggestions_list, key=len)
    else:
        longest_option = shortest_option = ''
    
    df.at[index, 'Longest Option'] = longest_option
    df.at[index, 'Shortest Option'] = shortest_option
    
    time.sleep(3)  # Wait a few seconds before the next search

browser.close()

# Update workbook with modified sheet
sheets[sheet] = df

with pd.ExcelWriter("4BeatsQ1.xlsx", engine='openpyxl', mode='w') as f:
    for sheet, content in sheets.items():
        content.to_excel(f, sheet_name=sheet, index=False)