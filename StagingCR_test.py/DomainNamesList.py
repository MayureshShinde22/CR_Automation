from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://stg-ind.connectreseller.com")
sleep(2)
#login details 


try:
    
    Last1 = driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-auth-login-v2/div/div/div[2]/div/form/div[1]/input').send_keys("ind.mayureshconnectreseller@gmail.com")
    sleep(2)
    Last2 = driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-auth-login-v2/div/div/div[2]/div/form/div[2]/div[2]/input').send_keys("Mayuresh@1998")
    sleep(2)

    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-auth-login-v2/div/div/div[2]/div/form/div[4]/div/label').click()
    sleep(2)
    #LOGIN
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-auth-login-v2/div/div/div[2]/div/form/button').click()
    sleep(2)
    print("Log_in succesfully")
    
    driver.get("https://stg-ind.connectreseller.com/reseller/domain")
    sleep(2)
    print("Domain Names List_Page...!!")
    
    #Domain_search
    driver.find_element("xpath", '//*[@id="keyword"]').click()
    sleep(2)
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-domain/div/div[2]/div/app-domainsearch/div/div[1]/button[1]').click()
    sleep(2)
    ##Show_Filter
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-domain/div/div[2]/div/app-domainsearch/div/div[1]/button[2]').click()
    sleep(2)
    ##Hide_Filter
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-domain/div/div[2]/div/app-domainsearch/div/div[1]/button[2]').click()
    sleep(2)
    ##Select All CheckBox
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-domain/div/div[3]/div/app-domainlist/div[2]/div/ngx-datatable/div/datatable-header/div/div[2]/datatable-header-cell[1]/div/div').click()
    sleep(2)
    print("Select_All_CheckBox.....!!")
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-domain/div/div[3]/div/app-domainlist/div[2]/div/ngx-datatable/div/datatable-header/div/div[2]/datatable-header-cell[1]/div/div').click()
    sleep(2)
    print("Unselect_All_CheckBox....!!")
    ##pagination of the DomainNameList
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-domain/div/div[3]/div/app-domainlist/div[1]/div[4]/div/label/select').click()
    sleep(2)
    print("Count100_pagination of the DomainNameList....!!")
    ##Select 100 from the pagination of the DomainNameList
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-domain/div/div[3]/div/app-domainlist/div[1]/div[4]/div/label/select/option[4]').click()
    sleep(2)
    #driver.find_element("xpath", '').click()
    #sleep(2)
    
    
    SCROLL_PAUSE_TIME = 0.1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        sleep(5)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    #driver.execute_script("window.scrollTo(2, Y)") 

    
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.refresh()
    sleep(2)
    
    
    
    
    
    
    
    
    
    
    
    print("run succesfully")
except ValueError:
    print("error")
    