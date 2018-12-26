import time
        
def scrolls_top(browser):
        print('Skroll to Top')
        #browser.execute_script('window.scrollTo(0, %d);' % skrol)
        browser.execute_script('window.scrollTo(0, 0);')

def scrolls_bottom(skrol, browser, stop=None):
    print(type(skrol),type(browser))
    incerment = 0
    while incerment < skrol:

        SCROLL_PAUSE_TIME = 0.5
        
        # Get scroll height
        last_height = browser.execute_script("return document.body.scrollHeight")
        while incerment < skrol:

            incerment += 1
            print('Scroll to bottom: %d' % incerment)
        
            # Scroll down to bottom
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
        
            # Calculate new scroll height and compare with last scroll height
            new_height = browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                if stop != None:
                        scrolls_top(browser)
                break
            last_height = new_height
        
def scrolls(number, browser):
        browser.execute_script('window.scrollTo(0, %d);'% number)