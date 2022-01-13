from elements import elements
import elements.elements as elements
from selenium import webdriver #the web driver is what we use to interact with the webpage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys # allows keyboard interactions to be made like enter
from bs4 import BeautifulSoup #used to scrape information from the website
 
import requests
 
driver = webdriver.Chrome(ChromeDriverManager().install()) # initialises ensures latest version of chromedriver
eles= elements.AllElements
 
for ele in eles:
    driver.get('https://simple.wikipedia.org/wiki/'+ele)
    page = requests.get(driver.current_url)
    soup = BeautifulSoup(page.text,'html.parser')
    infobox = soup.find('div',{'class':'mw-parser-output'})
    paras = infobox.find_all('p')
    count = 0
    desc = ''
    content = ''
    while count < (len(paras)):
        desc = paras[count].text
        if len(desc) > 2:
            for character in desc:
                if character.lower() in 'abcdefghijklmnopqrstuvwxyz. 1234567890()':
                    content = content + character
            break
        count += 1
    fpath = 'C:\\mywork\\pythonprgs\\Element_Information\\' + ele + '.txt' 
    try:
        f = open(fpath,'w')
        f.write(content)
        f.close()
    except:
        print('Error at', ele)
        
driver.quit()
