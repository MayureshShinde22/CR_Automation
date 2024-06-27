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
    
    
    driver.get("https://stg-ind.connectreseller.com/reseller/placeorder")
    sleep(1)
    
    
    driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[2]/app-transfer-register/div/div/div[1]/input').click()
    sleep(10)
    #PlaceOrder process
    driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[2]/app-transfer-register/div/div/div[2]/button').click()
    sleep(15)
    print("Domain Available_Check ")    

    ##Manage Customer
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-bulk-register/div[2]/div[1]/div[1]/ngx-datatable/div/datatable-body/datatable-selection/datatable-scroller/datatable-row-wrapper/datatable-body-row/div[2]/datatable-body-cell[3]/div/div/span[1]').click()
    sleep(3)

    driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[2]/div/div[1]/label').click()
    sleep(3)
    driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[2]/div/div[2]/label').click()
    sleep(3)
    
    driver.find_element("xpath", '//*[@id="name"]').click()
    sleep(1)
    driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[2]/div/div[3]/app-new-customer/form/div/div[2]/div[2]/input').click()
    sleep(1)
    driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[2]/div/div[3]/app-new-customer/form/div/div[3]/div[1]/input').click()
    sleep(1)
    driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[2]/div/div[3]/app-new-customer/form/div/div[3]/div[2]/input').click()
    sleep(1)
    driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[2]/div/div[3]/app-new-customer/form/div/div[4]/div[1]/input').click()
    sleep(1)
    driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[2]/div/div[3]/app-new-customer/form/div/div[4]/div[2]/input').click()
    sleep(1)
    driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[2]/div/div[3]/app-new-customer/form/div/div[5]/div[1]/ng-select/div/div/div[3]').click()
    sleep(1)
    driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[2]/div/div[3]/app-new-customer/form/div/div[5]/div[2]/ng-select/div/div/div[3]/input').click()
    sleep(1)
    
    driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[2]/div/div[2]/label').click()
    sleep(3)
    #Search Customer
    driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[2]/div/div[3]/div/ng-select/div/div/div[2]/input').click()
    sleep(3)
    driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[2]/div/div[3]/div/ng-select/ng-dropdown-panel/div/div[2]/div/span').click()
    sleep(3)
    driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[2]/div/div[1]/label').click()
    sleep(3)
    driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[1]/button').click()
    sleep(3)
    print("Manage Customer Action compeleted")
    ###Manage NameServer
    ##driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-bulk-register/div[2]/div[1]/div[1]/ngx-datatable/div/datatable-body/datatable-selection/datatable-scroller/datatable-row-wrapper/datatable-body-row/div[2]/datatable-body-cell[3]/div/div/span[2]').click()
    ##sleep(3)
    ##driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[2]/div/div[1]/label').click()
    ##sleep(3)
    ##driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[2]/div/div[1]/label').click()
    ##sleep(3)
    ##driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[2]/div/div[2]/button').click()
    ##sleep(3)
    ##print("Name Server Action Compeleted")
    #Add_More Domain action
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-bulk-register/div[2]/div[3]/div/button[3]').click()
    sleep(3)
    driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[2]/input').click()
    sleep(3)
    print("Add_More Domain action Compeleted")
    #Search Again    
    driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[1]/button').click()
    sleep(3)

    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-bulk-register/div[2]/div[3]/div/button[2]').click()
    sleep(3)
    driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[1]/button').click()
    sleep(3)
    print("Search Again action Compeleted")
    
    #Register Domain Button
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-bulk-register/div[2]/div[3]/div/button[1]').click()
    sleep(3)
    driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[3]/button[1]').click()
    sleep(3)
    print("Domain Registered Successfully")
    #driver.find_element("xpath", '').click()
    #sleep(3)
    #driver.find_element("xpath", '').click()
    #sleep(3)
    #driver.find_element("xpath", '').click()
    #sleep(3)
    driver.get("https://stg-ind.connectreseller.com/reseller/dashboard")
    sleep(2)
    

    print("run succesfully")
except ValueError:
    print("error")
    