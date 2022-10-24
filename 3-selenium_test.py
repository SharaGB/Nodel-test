import time
from selenium import webdriver
# Control mouse functions
from selenium.webdriver import ActionChains
# Used to locate elements within a document
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
service = Service(executable_path=r"./chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
# Navigate to a page given by the URL
driver.get('http://www.pbclibrary.org/raton/mousercise.htm')
# time.sleep(1)

# Start page 1 of the game
# Find the element by xpath
start_button = driver.find_element(by=By.XPATH, value='/html/body/table[2]/tbody/tr[2]/td/form/input')
# Click the element
ActionChains(driver).move_to_element(start_button).click().perform()
# time.sleep(1)

# Page 2 of the game
button1 = driver.find_element(by=By.XPATH, value='/html/body/div/p/a')
ActionChains(driver).move_to_element(button1).click().perform()
# time.sleep(1)

# Page 3 of the game
button2 = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td[2]/p/a')
ActionChains(driver).move_to_element(button2).click().perform()

# Page 4 of the game
button3 = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td/a')
ActionChains(driver).move_to_element(button3).click().perform()

# Page 5 of the game
button4 = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td[1]/a')
ActionChains(driver).move_to_element(button4).click().perform()

# Page 6 of the game
button5 = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td/a')
ActionChains(driver).move_to_element(button5).click().perform()

# Page 7 of the game
button6 = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/p/a')
ActionChains(driver).move_to_element(button6).click().perform()

# Page 8 of the game
button7 = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/p/a')
ActionChains(driver).move_to_element(button7).click().perform()

# Page 9 of the game
button8 = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/p/a')
ActionChains(driver).move_to_element(button8).click().perform()

# Page 10 of the game
button9 = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[3]/td/a[2]')
ActionChains(driver).move_to_element(button9).click().perform()

# Page 11 of the game
button10 = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[3]/td/a[2]')
ActionChains(driver).move_to_element(button10).click().perform()

# Page 12 of the game
button11 = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[3]/td/a[2]')
ActionChains(driver).move_to_element(button11).click().perform()

# Page 13 of the game
button12 = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[3]/td/a[2]')
ActionChains(driver).move_to_element(button12).click().perform()

# Page 14 of the game
button13 = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[3]/td[2]/a[2]')
ActionChains(driver).move_to_element(button13).click().perform()

# Page 15 of the game
orange_text = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[4]/a')
ActionChains(driver).move_to_element(orange_text).click().perform()

# Page 16 of the game
blue_text = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/a')
ActionChains(driver).move_to_element(blue_text).click().perform()

# Page 17 of the game
click_now = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr/td/form/input')
ActionChains(driver).move_to_element(click_now).click().perform()

# Page 18 of the game
_continue = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td/form/input')
ActionChains(driver).move_to_element(_continue).click().perform()

# Page 19 of the game
subit = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td/form/button')
ActionChains(driver).move_to_element(subit).click().perform()

# Page 20 of the game
click_here = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td/form/input')
ActionChains(driver).move_to_element(click_here).click().perform()

# Page 21 of the game
keys = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[3]/a/img')
ActionChains(driver).move_to_element(keys).click().perform()

# Page 22 of the game
animated_image = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[3]/td[2]/a/img')
ActionChains(driver).move_to_element(animated_image).click().perform()

# Page 23 of the game
# Press all buttons to continue
green_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[1]/img')
ActionChains(driver).move_to_element(green_button).click().perform()
green_button2 = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[2]/img')
ActionChains(driver).move_to_element(green_button2).click().perform()
turquoise_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[3]/img')
ActionChains(driver).move_to_element(turquoise_button).click().perform()
blue_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[4]/img')
ActionChains(driver).move_to_element(blue_button).click().perform()
dark_blue_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[5]/img')
ActionChains(driver).move_to_element(dark_blue_button).click().perform()
dark_blue_button2 = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[6]/img')
ActionChains(driver).move_to_element(dark_blue_button2).click().perform()
purple_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[7]/img')
ActionChains(driver).move_to_element(purple_button).click().perform()
pink_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[8]/img')
ActionChains(driver).move_to_element(pink_button).click().perform()
red_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[9]/img')
ActionChains(driver).move_to_element(red_button).click().perform()
orange_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[10]/img')
ActionChains(driver).move_to_element(orange_button).click().perform()
yellow_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[11]/img')
ActionChains(driver).move_to_element(yellow_button).click().perform()

_continue = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[4]/td/a/img')
ActionChains(driver).move_to_element(_continue).click().perform()

# Page 24 of the game
# Press all buttons and images to continue
push_me_button = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[2]/td[1]/form/input')
ActionChains(driver).move_to_element(push_me_button).click().perform()
button_me_too = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[3]/td[1]/form/input')
ActionChains(driver).move_to_element(button_me_too).click().perform()
image_start = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[4]/td[1]/img')
ActionChains(driver).move_to_element(image_start).click().perform()
image_open = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[5]/td[1]/img')
ActionChains(driver).move_to_element(image_open).click().perform()
next_button = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[2]/td[3]/form/input')
ActionChains(driver).move_to_element(next_button).click().perform()
image_arrow = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[3]/td[3]/img')
ActionChains(driver).move_to_element(image_arrow).click().perform()
image_home = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[4]/td[3]/img')
ActionChains(driver).move_to_element(image_home).click().perform()

_continue = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[5]/td[3]/a/img')
ActionChains(driver).move_to_element(_continue).click().perform()

# Page 25 of the game
# Press twice on all rockets to continue.
rocket = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[2]/td[1]/img')
ActionChains(driver).move_to_element(rocket).double_click().perform()
rocket2 = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[2]/td[2]/img')
ActionChains(driver).move_to_element(rocket2).double_click().perform()
rocket3 = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[2]/td[3]/img')
ActionChains(driver).move_to_element(rocket3).double_click().perform()
rocket4 = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[2]/td[4]/img')
ActionChains(driver).move_to_element(rocket4).double_click().perform()
rocket5 = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[3]/td[1]/img')
ActionChains(driver).move_to_element(rocket5).double_click().perform()
rocket6 = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[3]/td[2]/img')
ActionChains(driver).move_to_element(rocket6).double_click().perform()
rocket7 = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[3]/td[3]/img')
ActionChains(driver).move_to_element(rocket7).double_click().perform()
rocket8 = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[3]/td[4]/img')
ActionChains(driver).move_to_element(rocket8).double_click().perform()

_continue = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[4]/td/a/img')
ActionChains(driver).move_to_element(_continue).click().perform()

# Page 26 of the game
# Drag the scroll palette as far as you want and press continue.
scroll_palette1 = driver.find_element(by=By.XPATH, value='//*[@id="red-slider"]')
scroll_palette2 = driver.find_element(by=By.XPATH, value='//*[@id="green-slider"]')
target = driver.find_element(by=By.XPATH, value='//*[@id="canvas"]/table/tbody/tr[3]/td/a')
ActionChains(driver).drag_and_drop(scroll_palette1, target).perform()
ActionChains(driver).drag_and_drop(scroll_palette2, target).perform()
_continue = driver.find_element(by=By.XPATH, value='//*[@id="canvas"]/table/tbody/tr[3]/td/a')
ActionChains(driver).move_to_element(_continue).click().perform()

# Page 27 of the game
# Use scroll bar to get to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
next = driver.find_element(by=By.XPATH, value='/html/body/p[1]/a')
ActionChains(driver).move_to_element(next).click().perform()

# Page 28 of the game
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
next = driver.find_element(by=By.XPATH, value='/html/body/div/p[1]/a')
ActionChains(driver).move_to_element(next).click().perform()

# Page 29 of the game
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
next = driver.find_element(by=By.XPATH, value='/html/body/div/p[2]/a')
ActionChains(driver).move_to_element(next).click().perform()

# Page 30 of the game
# Use scroll bar to move the page to the right
driver.execute_script("window.scrollTo(100, 0);")
# time.sleep(3)
next = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td[2]/p/a')
ActionChains(driver).move_to_element(next).click().perform()

# Page 31 of the game
# Use scroll bar to move the page down and to the right
driver.execute_script("window.scrollTo(100, 100);")
# time.sleep(3)
next = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr/td[2]/p/a')
ActionChains(driver).move_to_element(next).click().perform()

# Page 32 of the game
# Warning box
show = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td/a')
ActionChains(driver).move_to_element(show).click().perform()
Alert(driver).accept()

# Page 33 of the game
maze = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td[2]/span/a')
ActionChains(driver).move_to_element(maze).click().perform()

# Page 34 of the game
box1 = driver.find_element(by=By.XPATH, value='/html/body/form/input[1]')
box1.click()
box2 = driver.find_element(by=By.XPATH, value='/html/body/form/input[2]')
box2.click()
box3 = driver.find_element(by=By.XPATH, value='/html/body/form/input[3]')
box3.click()
box4 = driver.find_element(by=By.XPATH, value='/html/body/form/input[4]')
box4.click()
box5 = driver.find_element(by=By.XPATH, value='/html/body/form/input[5]')
box5.click()
box6 = driver.find_element(by=By.XPATH, value='/html/body/form/input[6]')
box6.click()
box7 = driver.find_element(by=By.XPATH, value='/html/body/form/input[7]')
box7.click()
box8 = driver.find_element(by=By.XPATH, value='/html/body/form/input[8]')
box8.click()
box9 = driver.find_element(by=By.XPATH, value='/html/body/form/input[9]')
box9.click()

ActionChains(driver).move_to_element(box2).click().perform()
ActionChains(driver).move_to_element(box4).click().perform()
ActionChains(driver).move_to_element(box6).click().perform()
ActionChains(driver).move_to_element(box8).click().perform()

_continue = driver.find_element(by=By.XPATH, value='/html/body/p/a/img')
ActionChains(driver).move_to_element(_continue).click().perform()

# Page 35 of the game
# Check the box
extra_cheese = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/input[1]')
extra_cheese.click()
peppers = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/input[3]')
peppers.click()
pepperoni = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/input[5]')
pepperoni.click()
_continue = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/input[7]')
ActionChains(driver).move_to_element(_continue).click().perform()

# Page 36 of the game
one = driver.find_element(by=By.XPATH, value='/html/body/form/input[1]')
one.click()
two = driver.find_element(by=By.XPATH, value='/html/body/form/input[2]')
two.click()
three = driver.find_element(by=By.XPATH, value='/html/body/form/input[3]')
three.click()
four = driver.find_element(by=By.XPATH, value='/html/body/form/input[4]')
four.click()
five = driver.find_element(by=By.XPATH, value='/html/body/form/input[5]')
five.click()
six = driver.find_element(by=By.XPATH, value='/html/body/form/input[6]')
six.click()
seven = driver.find_element(by=By.XPATH, value='/html/body/form/input[7]')
seven.click()
eight = driver.find_element(by=By.XPATH, value='/html/body/form/input[8]')
eight.click()
nine = driver.find_element(by=By.XPATH, value='/html/body/form/input[9]')
nine.click()

_continue = driver.find_element(by=By.XPATH, value='/html/body/p/a/img')
ActionChains(driver).move_to_element(_continue).click().perform()

# Page 37 of the game
medium_pizza = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/input[2]')
medium_pizza.click()
_continue = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/input[5]')
ActionChains(driver).move_to_element(_continue).click().perform()

# Page 38 of the game
box = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/select')
box.click()
option = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/select/option[6]')
option.click()
_continue = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/p/a/img')
ActionChains(driver).move_to_element(_continue).click().perform()

# Page 39 of the game
menu = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/select')
menu.click()
option = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/select/option[4]')
option.click()
_continue = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/input')
ActionChains(driver).move_to_element(_continue).click().perform()

# Page 40 of the game
six = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/select/option[6]')
six.click()
_continue = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/p/a/img')
ActionChains(driver).move_to_element(_continue).click().perform()

# Page 41 of the game
menu = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/select/option[8]')
menu.click()
_continue = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/input')
ActionChains(driver).move_to_element(_continue).click().perform()

# Page 42 of the game
text_box_name = driver.find_element(by=By.XPATH, value='/html/body/form/input[1]')
text_box_name.send_keys('Sarah')
text_box_last_name = driver.find_element(by=By.XPATH, value='/html/body/form/input[2]')
text_box_last_name.send_keys('García')
_continue = driver.find_element(by=By.XPATH, value='/html/body/form/input[3]')
ActionChains(driver).move_to_element(_continue).click().perform()

# Close the browser
driver.quit()
