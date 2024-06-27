##Domain_functions
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
    
    driver.get("https://stg-ind.connectreseller.com/reseller/dashboard")
    sleep(1)
    
    #SelectAll_Renew from Dashboard
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-dashboard2/div/div[3]/div/app-renewdomains/div/div/ngx-datatable/div/datatable-header/div/div[2]/datatable-header-cell[1]/div/div').click()
    sleep(2)
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-dashboard2/div/div[3]/div/app-renewdomains/div/div/ngx-datatable/div/datatable-header/div/div[2]/datatable-header-cell[1]/div/div').click()
    sleep(2)

 

    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-dashboard2/div/div[3]/div/app-renewdomains/div/div/ngx-datatable/div/datatable-body/datatable-selection/datatable-scroller/datatable-row-wrapper[2]/datatable-body-row/div[2]/datatable-body-cell[1]/div/div').click()
    sleep(2)

    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-dashboard2/div/div[3]/div/app-renewdomains/div/div/ngx-datatable/div/datatable-body/datatable-selection/datatable-scroller/datatable-row-wrapper[3]/datatable-body-row/div[2]/datatable-body-cell[1]/div').click()  
    sleep(2)
    #Renew_Button
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-dashboard2/div/div[3]/div/app-renewdomains/button').click()    
    sleep(5)

    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-domainrenewal/div/div[2]/div[2]/table/tr[7]/td/button').click()
    sleep(2)
    driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[3]/button[1]').click()
    sleep(2)
    driver.find_element("xpath", '/html/body/div[2]/div/div[3]/button[1]').click()
    sleep(5)
    print("Renew from DashBoard action succesfully")
        

    print("run succesfully")
except ValueError:
    print("error")