from selenium import webdriver
from time import sleep
import platform


if platform.uname().node == 'raspberrypi':
    #from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
    #from selenium import webdriver

    #binary = FirefoxBinary('/usr/bin/firefox')
    #driver = webdriver.Firefox(firefox_binary=binary)
    #driver.get('www.google.com')
    
    from pyvirtualdisplay import Display
    from selenium import webdriver

    display = Display(visible=0, size=(800, 600))
    display.start()

    driver = webdriver.Firefox()
else:
    driver = webdriver.Chrome('/Users/pruthvivikram/whatsapp_python/chromedriver')

driver.get('https://web.whatsapp.com')

name = 'BOT'
msg = 'This is newly created PYTHON BOT for this channel.Development under progress.'

input("Waiting on QR Code scan...")
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

def send_message(text):
    try:
        msg = text
        msg_box = driver.find_element_by_class_name('_2S1VP')
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_35EW6')
        button.click()
        print("Message sent")
    except:
        print("Message could not be sent... Sorry...! ;-(")

while True:
    new_msg = ''
    old_msg = ''
    sleep(2)

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    try:
        last_class = driver.find_elements_by_class_name('_3zb-j')
        new_msg = last_class[-1].text

        if old_msg != new_msg:
            old_msg = new_msg

            if new_msg == "#help":
                send_message("Bot\t\t\t\t#help - Help commands\t\t\t\tC-k Worked")
            elif new_msg == "#love":
                send_message("£♡ Sam, Pruthvi loves you so much ♡£")
    except:
        pass




