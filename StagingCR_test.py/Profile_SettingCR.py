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
    

    #Profile name 
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/app-navbar/div/ul/li/a/div/span').click()
    sleep(2)
    
    #Profile setting
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/app-navbar/div/ul/li/div/a[1]').click()
    sleep(2)
    #Modify button
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-profile/div/div[2]/div[2]/app-main-sidebar-profile/div/div/app-profile-settings/div/div/div[2]/label').click()
    sleep(2)
    print("Profile_Modicifaction started")
    #Select Name
    print("Enter UserName value")
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-profile/div/div[2]/div[2]/app-main-sidebar-profile/div/div/app-profile-settings/div/form/div[1]/div[1]/input').click()
    sleep(5)

    #select_Phone_No
    print("-> Phone No value")
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-profile/div/div[2]/div[2]/app-main-sidebar-profile/div/div/app-profile-settings/div/form/div[1]/div[3]/div/input').click()
    sleep(5)
    
    # clear contents 
    #element.clear()

    #Alternate Phone No
    print("-> Enter Alternate Phone No value")
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-profile/div/div[2]/div[2]/app-main-sidebar-profile/div/div/app-profile-settings/div/form/div[1]/div[4]/div/input').click()
    sleep(5)
    #Select_Fax No
    print("-> Enter Fax No value")
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-profile/div/div[2]/div[2]/app-main-sidebar-profile/div/div/app-profile-settings/div/form/div[1]/div[5]/div/input').click()
    sleep(5)
    #Select_Address
    print("-> Enter Address value")
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-profile/div/div[2]/div[2]/app-main-sidebar-profile/div/div/app-profile-settings/div/form/div[1]/div[6]/input').click()
    sleep(5)
    #Select_CityName
    print("-> Enter CityName value")
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-profile/div/div[2]/div[2]/app-main-sidebar-profile/div/div/app-profile-settings/div/form/div[1]/div[7]/input').click()
    sleep(5)
    #Select_StateName
    print("-> Select StateName value")
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-profile/div/div[2]/div[2]/app-main-sidebar-profile/div/div/app-profile-settings/div/form/div[1]/div[8]/ng-select/div/div/div[3]/input').click()
    sleep(5)
    #Select_Zipcode
    print("-> Enter Zipcode value")
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-profile/div/div[2]/div[2]/app-main-sidebar-profile/div/div/app-profile-settings/div/form/div[1]/div[9]/input').click()
    sleep(5)
    #Select_Skype Id
    print("-> Enter Skype Id value")
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-profile/div/div[2]/div[2]/app-main-sidebar-profile/div/div/app-profile-settings/div/form/div[1]/div[10]/input').click()
    sleep(5)
    #Select_linkedin Id
    print("-> Enter Linkedin ID value")
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-profile/div/div[2]/div[2]/app-main-sidebar-profile/div/div/app-profile-settings/div/form/div[1]/div[11]/input').click()
    sleep(5)
    #Select_Funds Threshold
    print("-> Enter_Fund_Threshold value")
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-profile/div/div[2]/div[2]/app-main-sidebar-profile/div/div/app-profile-settings/div/form/div[1]/div[12]/input').click()
    sleep(5)
    #Select_Signature
    print("-> Enter_Signature_Name value")
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-profile/div/div[2]/div[2]/app-main-sidebar-profile/div/div/app-profile-settings/div/form/div[1]/div[13]/textarea').click()
    sleep(5)
    #SELECT_GSTIN
    print("-> Enter_GstIN value")
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-profile/div/div[2]/div[2]/app-main-sidebar-profile/div/div/app-profile-settings/div/form/div[1]/div[14]/input').click()
    sleep(5)
    #Click SAVE_Button
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-profile/div/div[2]/div[2]/app-main-sidebar-profile/div/div/app-profile-settings/div/form/div[2]/div[2]/button').click()
    sleep(5)
    
    print("-> Profile Updated Successfully")


    #Update Password
    print("-> Update_Password Function")
    
    driver.find_element("xpath", '//*[@id="ngb-nav-1"]').click()
    sleep(5)
    #Current_Password
    print("-> Current Password is required")
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-profile/div/div[2]/div[2]/app-main-sidebar-profile/div/div/app-password/div/div/form/div[1]/div[1]/div[2]/input').click()
    sleep(5)
    #New_Password
    print("-> New Password is required")
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-profile/div/div[2]/div[2]/app-main-sidebar-profile/div/div/app-password/div/div/form/div[1]/div[2]/div[2]/input').click()
    sleep(5)
    #Confirm Password
    print("-> Comfirm Password is required")
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-profile/div/div[2]/div[2]/app-main-sidebar-profile/div/div/app-password/div/div/form/div[1]/div[3]/div[2]/input').click()
    sleep(5)
    #Save Button
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-profile/div/div[2]/div[2]/app-main-sidebar-profile/div/div/app-password/div/div/form/div[2]/div/button').click()
    sleep(5)
    print("-> Password Updated Successfully")

    #Select Domain Pricing
    print("-> Domain Pricing Function")
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-profile/div/div[2]/div[2]/app-main-sidebar-profile/ul/li[3]').click()
    print("-> DropDwon of Search Tlds :")
    print("-> Select any TLD & Verify Value")
    #Select Search Tlds 
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-profile/div/div[2]/div[2]/app-main-sidebar-profile/div/div/app-domain-pricing/div/div/div[2]/div/ng-select/div/div/div[2]/input').click()
    sleep(5)
    
    
    

    
    #Select Reseller Branding
    print("-> Reseller Branding Function <-")
    driver.find_element("xpath", '//*[@id="ngb-nav-3"]').click()
    sleep(5)
    
    print("-> Branding Logo Function")
    driver.find_element("xpath", '//*[@id="ngb-nav-8"]').click()  
    sleep(5)

    print("-> Default Name Server function")
    driver.find_element("xpath", '//*[@id="ngb-nav-9"]').click()    
    sleep(5)

    driver.find_element("xpath", '//*[@id="defaultServerName"]').click()
    sleep(5)
    print("-> Successfully Updated")
    
    ####Panel Setting 
    print("-> Panel Setting <-")
    driver.find_element("xpath", '//*[@id="ngb-nav-4"]').click()
    sleep(5)
    #Update button
    print("Settings Updated Successfully")
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-profile/div/div[2]/div[2]/app-main-sidebar-profile/div/div/app-panel-settings/div/form/div[2]/div[2]/button').click()
    sleep(5)
    
    #####Reseller Api
    print("Reseller API Settings")
    driver.find_element("xpath", '//*[@id="ngb-nav-5"]').click()
    sleep(5)
    
    #View API Key 
    print("-> View API Key")
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-profile/div/div[2]/div[2]/app-main-sidebar-profile/div/div/app-api-key/div/div[2]/div/a').click()
    sleep(5)
    
    #Copy API key
    print("Your API key Copied Successfully ")
    driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[3]/button[2]').click()  
    sleep(5)
    #Close PopUp
    driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[1]/button').click()    
    sleep(5)

    
    #View Encryption Key 
    print("View Encryption Key")
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-profile/div/div[2]/div[2]/app-main-sidebar-profile/div/div/app-api-key/div/div[3]/div/a').click()
    sleep(5)
    
    #Click on Generate button
    print("Generate Encryption Key's")
    driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[3]/button[1]').click()
    sleep(5)
    print("Key Updated Successfully")
    
    #Close popup
    driver.find_element("xpath", '/html/body/ngb-modal-window/div/div/div[1]/button/span').click()
    sleep(5)
    
    
    #Click on Use Two Factor Authentication
    print("-> Use Two Factor Authentication")
    driver.find_element("xpath", '//*[@id="ngb-nav-6"]').click()
    sleep(5)
    
    #Two Factor Authentication Button
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-profile/div/div[2]/div[2]/app-main-sidebar-profile/div/div/app-two-factor-auth/div/div[2]/div/div/div[2]/button').click()
    sleep(5)
    #Continue Button
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/div/content/div/app-profile/div/div[2]/div[2]/app-main-sidebar-profile/div/div/app-two-factor-auth/div/div[3]/div[6]/div/button').click()
    sleep(5)
    

    #Add funds
    print("Add Funds - Online Payment")
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/app-navbar/div/ul/app-available-funds/li/div/button').click()
    sleep(5)

    print("Add fund to your accoun")
    driver.find_element("xpath", '/html/body/app-root/vertical-layout/app-navbar/div/ul/app-available-funds/li/div/button').click()  
    sleep(5)
    driver.refresh()
    #DashBoard
    #print("DashBoard function")
    #driver.get("https://stg-ind.connectreseller.com/reseller/dashboard")
    #sleep(5)
    #driver.find_element("xpath", '').click()
    #sleep(5)
    #
    #driver.find_element("xpath", '').click()
    #sleep(5)
    #
    #driver.find_element("xpath", '').click()
    #sleep(5)
    #
    #driver.find_element("xpath", '').click()
    #sleep(5)
#
    #
    #
    #
    
    
    
    
    

    
    
    
    
    
    
    
    
        # driver.close()
    print("run succesfully")
except ValueError:
    print("error")