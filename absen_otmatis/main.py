from selenium import webdriver
import yaml

env = yaml.load(open('./user.yml'))
driver = webdriver.Chrome()
user = env['user']


def login(u, p):
    driver.get("http://36.94.206.117:8000/masterweb/index.php/login")
    driver.find_element_by_id('username').send_keys(u)
    driver.find_element_by_id('password').send_keys(p)
    driver.find_element_by_tag_name("button").click()
    driver.get(
        'http://36.94.206.117:8000/masterweb/index.php/sos/kesiswaan/absen_mpls')
    driver.find_element_by_xpath("//input[@type='image']").click()
    driver.get("http://36.94.206.117:8000/masterweb/index.php/login/logout")


for i in user:
    login(user[i]['username'], user[i]['password'])

driver.close()
