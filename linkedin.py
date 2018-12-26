while True:
    try:
        import pip, os
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        import time
        from skrol import scrolls_bottom, scrolls_top, scrolls
        break
    except Exception as e:
        pip.main(['install', '--upgrade', 'pip'])
        print('You don"t have install librery', e)
        module = str(e)[17:]
        module = module[0:len(module)-1]
        pip_return = pip.main(['install', module])
        if pip_return == 1:
            print("Can't install python library", module)
            exit(0)

def start_browser(url, goo_fire='firefox'):
    ''' We are opening browser, either Mozilla Firefox or Google Chrome
     will be opened '''
    if goo_fire.lower() == 'firefox':
        browser = webdriver.Firefox(executable_path=os.getcwd() + '\\' + 'geckodriver.exe')
        browser.get(url)
    else:
        browser = webdriver.Chrome(executable_path=os.getcwd() + '\\' + 'chromedriver.exe')
        browser.get(url)
    return browser

def login(browser):
    ''' This is acctualy login method accepting 3 parramaters
    mail, password, browser'''
    email = browser.find_element_by_id('login-email')
    password = browser.find_element_by_id('login-password')
    email.send_keys('type-your@mail')
    password.send_keys('type-your-password')
    sign_in = browser.find_element_by_id('login-submit')
    sign_in.click()
    time.sleep(5)

def my_network(browser, number = 0):
    ''' This will lead us to My Network tab '''
    my_connection = browser.find_element_by_id('mynetwork-nav-item')
    my_connection.click()
    time.sleep(10)

def all_connections(browser, number = 0):
    ''' Through this function, we scroll to bottom '''
    scrolls_bottom(int(1), browser, stop='')
    scrolls_top(browser)
    time.sleep(5)

def connect_people(browser):
    ''' Now we click on Connect for each profile'''
    connect = browser.find_elements_by_tag_name("span")
    for connection in connect:
        try:
            if 'Connect' == connection.text:
                print('Click on:',connection.text)
                connection.click()
                print("Connect")
                time.sleep(1)

        except Exception as e:
            print(e)

browser = start_browser('https://www.linkedin.com',goo_fire='a')
login(browser)
my_network(browser)
all_connections(browser)
connect_people(browser)
browser.quit()
