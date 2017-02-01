# from pyvirtualdisplay import Display
from selenium import webdriver
from time import sleep


# noinspection PyDeprecation
def send_proton_email(email_to, email_subject, email_message):
    driver = ''
    display = ''
    try:
        # display = Display(visible=0, size=(1920, 1080))   # Used to create a virtual display to be able to run selenium in a terminal without GUI
        # display.start()
        driver = webdriver.Firefox()
        driver.get('https://mail.protonmail.com/login')
        driver.find_element_by_id('username').send_keys('Account_Username')
        driver.find_element_by_id('password').send_keys('Account_password')
        driver.find_element_by_id('login_btn').click()
        sleep(3)
        driver.find_element_by_id('password').send_keys('Mail_Decrypt_Password')
        driver.find_element_by_id('unlock_btn').click()
        sleep(5)
        driver.find_element_by_xpath('//*[@id="pm_sidebar"]/section/a').click()
        sleep(2)
        driver.switch_to_active_element().send_keys(email_to + '\n' + '\t' + email_subject + '\t')
        sleep(0.5)
        driver.switch_to_active_element().send_keys(email_message + '\t' + '\t' + '\t' + '\t' + '\t' + '\t')
        sleep(0.5)
        driver.switch_to_active_element().click()
        sleep(5)
        driver.quit()
        # display.stop()
        print('E-mail Sent!')
        del email_subject
        del email_message
        del driver
        del display
    except Exception as err:
        driver.quit()
        # display.stop()
        print('\nError Occurred while sending e-mail!!')
        status = (str(err), 'Error Origin: Proton Mail Script')
        print(status)
        del err
        del status
        del driver
        # del display

send_proton_email('receiver_email@gmail.com', 'test', 'testmsg')