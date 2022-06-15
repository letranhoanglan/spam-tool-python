from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def spam():
    user = username.get()
    pas = password.get()
    channel1 = channel.get()
    word1 = words.get()
    browser = webdriver.Chrome("./chromedriver.exe")
    browser.get("https://discord.com/login")
    username1 = browser.find_element_by_name("email")
    username1.send_keys(user)
    password1 = browser.find_element_by_name("password")
    password1.send_keys(pas)
    password1.send_keys(Keys.ENTER)
    time.sleep(5)
    browser.get(channel1)
    time.sleep(5)
    messager = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div/div[2]")
    for i in range(10):
      messager.send_keys(word1)
      messager.send_keys(Keys.ENTER)
      time.sleep(2)
      

app = Tk()
app.geometry("250x130")
app.title("spam discord tool remake")
app.configure(bg="lavender")
Label(app, text="Tên đăng nhập: ", bg="lavender").grid(row=0, column=0)
Label(app, text="Mật khẩu: ", bg="lavender").grid(row=1, column=0)
Label(app,text="link kênh muốn spam",bg="lavender").grid(row=2,column=0)
Label(app,text="từ muốn spam",bg="lavender").grid(row=3,column=0)
username = Entry(app, width=15)
username.grid(row=0, column=1)
password = Entry(app, width=15)
password.grid(row=1, column=1)
channel = Entry(app,width=15)
channel.grid(row=2,column=1)
words = Entry(app,width=15)
words.grid(row=3,column=1)
Button(app, text="time to spam", bg="skyblue", command=spam).grid(row=4, column=0)
app.mainloop()