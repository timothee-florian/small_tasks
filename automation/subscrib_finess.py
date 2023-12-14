# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 21:15:25 2023

@author: me the problem
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import yaml
import os


def subscribe():
    with open(os.path.join(os.path.dirname(__file__),'..','..','..', 'Desktop', 'connect.yml'), 'r') as stream:
        connection = yaml.safe_load(stream)

    driver = webdriver.Chrome()
    driver.implicitly_wait(10) 
    url_start = 'https://www.activfitness.ch/fr/reservation-de-cours/'


    driver.set_window_size(1444,1444)

    driver.get(url_start)

    # accept cookies
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[6]/button[1]').click()

    #login
    driver.find_element(By.XPATH, '/html/body/header/nav/div/div[2]/div[2]/div[1]/div[2]/a/span[2]').click()


    driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div/div/div[2]/div/div[2]/div[4]/button').click()

    email=driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div/form/div[3]/input')
    password=driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div/form/div[4]/div/div/input')


    email.send_keys(connection['connection']['email'])
    password.send_keys(connection['connection']['password'])
    driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div/form/div[5]/button').click()

    time.sleep(15)
    #go to reservation
    driver.get("https://www.activfitness.ch/it/prenotazione-di-corsi/")

    # set filter
    try:
        driver.find_element(By.XPATH,'/html/body/div[2]/div/main/div[2]/div[1]/div/section/div/div[2]/button').click()   
        driver.find_element(By.XPATH,'/html/body/div[2]/div/main/div[2]/div[1]/div/section/div/div/div/div/div[2]/a[1]/div/h4').click()
    except:
        driver.find_element(By.XPATH,'/html/body/div[2]/div/main/div[2]/div[1]/div/section/div/div[3]/div/div[1]/div/div[1]/button[1]/div').click()

    target = driver.find_element(By.NAME, 'ACTIV FITNESS Lugano')
    if not target.is_selected():
        target.click()
        
    time.sleep(15)
    try:
        driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div[2]/div[1]/div/section/div/div/div/div[3]/div/button/span').click()
    except:
        driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div[2]/div[1]/div/section/div/div[3]/div/div[2]/div/div[3]/div/button/span').click()
        
    i = 1
    for _ in range(10):
        
        #monstra di piu
        try:
            driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div[2]/div[1]/div/section/div/div[6]/button').click()
            i += 1
        except:
            time.sleep(15)
        if i>2:
            break
    time.sleep(15)
    #find course
    elems = driver.find_elements(By.XPATH, "*//button[@class='sc-gScZFl bizrcz']")

    for ele in elems:
        text = ele.text
        print(text, end='\n\n')
        
        if 'BODYCOMBAT' in text and '19:10 - 20:00' in text:
            break
    for _ in range(5):
        try:
            ele.click()
        except:
            time.sleep(15)
            
    for _ in range(5):
        try:
            driver.find_element(By.XPATH,'/html/body/div[2]/div/main/div[2]/div[1]/div/section/div/div[7]/div/div/div[2]/button[1]').click()
        except:
            time.sleep(15)    

    driver.close()
if __name__ == '__main__':
    subscribe()

