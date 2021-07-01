import time

# infinite scroller from: https://medium.com/analytics-vidhya/using-python-and-selenium-to-scrape-infinite-scroll-web-pages-825d12c24ec7
def scroll(URL, driver):
    driver.get(URL)
    time.sleep(2)
    scroll_pause_time = 1
    screen_height = driver.execute_script("return window.screen.height;")
    scrolls = 1
    i = 1

    while True:
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
        scrolls += 1
        i += 1
        time.sleep(scroll_pause_time)
        # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        scroll_height = driver.execute_script("return document.body.scrollHeight;")
        # Break the loop when the height we need to scroll to is larger than the total scroll height
        if (screen_height) * scrolls > scroll_height or scrolls == 2:  # limits scrolls
            break
