# imporiting webdriver from selenium module
from selenium import webdriver
# importing tkinter module for GUI
from tkinter import *
import tkinter.ttk as ttk
# importing time module
import time
# importing messagebox from tkinter module
from tkinter.messagebox import showinfo

# creating function to login into instagram using username and password
def autologin():
    # accessing globally declared variables
    global username
    global passwd
    # getting user input from entry component in the GUI
    username_automation = username.get()
    password_automation = passwd.get()

    # checking whether both the username and password are not empty
    if(username_automation == "" or password_automation == ""):
        showinfo('instagram Login', 'Please Add Username or Password')

    else:
        # creating driver object of webdriver with chrome driver
        driver = webdriver.Chrome('chromedriver.exe')
        # accessing instagram
        driver.get('https://instagram.com')

        # putting sleep so that instagram don't think us a robot and block our account
        time.sleep(10)

        # finding username field using xpath
        username = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
        # putting user specified username
        username.send_keys(username_automation)

        # finding password field using xpath
        password = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
        # putting user specified password
        password.send_keys(password_automation)

        # again putting our program for sleep
        time.sleep(3)

        # finding login button using xpath
        login = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]')
        # pressing login button using click method
        login.click()

        # again putting program to sleep
        time.sleep(3)

        # finding notification button xpath to deny the notifications
        notification = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        # clicking the deny button
        notification.click()

# creating window using tkinter
win = Tk()

# giving title to our window
win.title('Instagram Login')
# specifing size of the window
win.geometry('250x100')

# creating label to print username on the window
username_label = ttk.Label(win, text = 'Username', foreground = 'blue', font=('',12))
username_label.grid(row = 0, column = 0)

# creating a entry field to get username from the user
username = ttk.Entry(win,width = 20)
username.grid(row = 0, column = 1)

# creating label to print password on the window
passwd_label = ttk.Label(win, text = 'Password', foreground = 'blue', font = ('', 12))
passwd_label.grid(row = 1, column = 0)

# creating a entry field to get password from the user
passwd = ttk.Entry(win, show='*', width = 20)
passwd.grid(row = 1, column = 1, padx=15)

# creating button to call auto login function to execute the automation
button = ttk.Button(win, text = 'Go', command = autologin)
button.grid(row = 2, column = 0, columnspan = 2)

# creating loop for window
win.mainloop()