import os
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

file_credentials = open('credentials.txt', 'r')
USERNAME = file_credentials.readline()
PASSWORD = file_credentials.readline()

if __name__ == '__main__':
    print('Please run the Runner.py to use this bot!')
    exit(0)

# This will save the logged in state of Instagram
chrome_options = Options()
chrome_options.add_argument('user-data-dir=/cookies')

chrome = webdriver.Chrome('chromedriver.exe', options=chrome_options)
chrome.get('https://www.instagram.com/accounts/login/')
time.sleep(3)

try:
    username_field = chrome.find_element_by_name('username')
    password_field = chrome.find_element_by_name('password')

    username_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD)

    # Pressing enter on the password filed
    password_field.send_keys(Keys.RETURN)
    time.sleep(10)

except NoSuchElementException:
    print('Login not required!')

RECENT_POSTS = 1
TOP_POSTS = 2


def follow(username):
    chrome.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    chrome.get(f'https://www.instagram.com/{username}')

    try:
        follow_button = chrome.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button')
    except NoSuchElementException:
        print(f'{username} is unavailable')
        return

    if follow_button.text == 'Follow':
        follow_button.click()
        print(f'{username} is followed')

        with open('Following.txt', 'a+') as following:
            following.write(f',{username}')
        add_log(True, 1, 'follow', username)
    else:
        print(f'{username} is already followed')


def unfollow(username):
    chrome.get(f'https://www.instagram.com/{username}')
    time.sleep(1)

    try:
        unfollow_button = chrome.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button')
    except NoSuchElementException:
        try:
            unfollow_button = chrome.find_element_by_class_name('_5f5mN.-fzfL._6VtSN.yZn4P')
        except NoSuchElementException:
            print(f'Cannot unfollow {username}. Maybe this account is already unfollowed.')
            return

    following = open('Following.txt', 'a+')
    following.seek(0)  # Moving the pointer to the first position

    unfollow_button.click()
    chrome.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()
    print(f'{username} is unfollowed')

    usernames = following.read().split(',')
    following.truncate(0)  # Deleting all the usernames after reading them

    # Removing the unfollowed username from the list
    if username in usernames:
        usernames.remove(username)

    # Writing back the remaining usernames to the file
    for user_name in usernames:
        following.write(f',{user_name}')

    # Adding log
    add_log(True, 1, 'unfollow', username)

    following.close()


def like_and_follow_posts_of_username(username, number_of_posts=-1, should_follow=False):
    """
    After going to the profile of 'username', the bot will start liking 'number_of_posts' posts of that profile
    By default all the pictures of the 'username' will be liked
    :param: Will follow 'username' if True
    """

    if should_follow:
        follow(username)

    # Going to the 'username''s profile
    chrome.get(f'https://www.instagram.com/{username}')

    # Getting total number of posts.
    total_no_of_posts = int(chrome.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span/span').text)

    if number_of_posts > total_no_of_posts:
        print(f'{username} have {total_no_of_posts} posts and you asked to like {number_of_posts} posts')
        return

    # Clicking on the first picture of 'username'
    first_post = chrome.find_element_by_class_name("_9AhH0")
    chrome.execute_script("arguments[0].scrollIntoView(true);", first_post)
    first_post.click()

    like_picture()  # This will like the first post

    if number_of_posts == -1:
        for i in range(total_no_of_posts - 1):  # -1 because the bot has already liked the first post
            click_next()
            like_picture()
    else:
        for i in range(number_of_posts - 1):  # -1 because the bot has already liked the first post
            click_next()
            like_picture()

    add_log(should_follow, 1, 'follow', username)


def like_and_follow_posts_of_hashtag(hashtag, number_of_posts, tab, should_follow_people=False):
    """
    This will randomly like posts and may follow people from the 'tab' of hashtag search

    :param hashtag: The hashtag whose posts has to be liked
    :param number_of_posts: Number of posts that should be liked from 'hashtag'
    :param tab: The images will be liked based on this value.
    :param should_follow_people: If True, bot will follow people whose posts are liked
    :return: None
    """

    # Searching the hashtag
    chrome.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
    time.sleep(2)

    # Clicking on the image based on 'tab'
    if tab == RECENT_POSTS:
        try:
            chrome.find_element_by_xpath("//article/div[2]/div/div/div/a/div/div[2]").click()
        except NoSuchElementException:
            print(f'Looks like #{hashtag} does not have a recent tab. Try choosing TOP_POSTS')
            return
    elif tab == TOP_POSTS:
        try:
            chrome.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]').click()
        except NoSuchElementException:
            print('You may have chosen a hashtag which is unavailable')
            return
    else:
        print('var \'tab\' should be either RECENT_POSTS or TOP_POSTS')
        return
    time.sleep(3)

    # Creating a file object to save the new follows usernames
    following = open('Following.txt', 'a+')

    new_follows = []
    for i in range(number_of_posts):

        # Randomly skips few posts
        from random import randint
        for rand in range(randint(0, 5)):
            click_next()
        time.sleep(3)

        account_name = chrome.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a').text
        print(f"A picture of {account_name} is being liked")

        like_picture()
        time.sleep(5)  # This will not let Instagram know that we are using a bot

        if should_follow_people:
            follow_button = chrome.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')
            if follow_button.text == 'Following':
                print(f'{account_name} is already Followed')
            else:
                follow_button.click()
                print(f'\n\t\t{account_name} is followed!\n')
                following.write(f',{account_name}')
                new_follows.append(account_name)

        click_next()
        time.sleep(3)
    following.close()
    print(f"Number of new follows: {len(new_follows)}")

    add_log(should_follow_people, len(new_follows), 'follow', new_follows)


# Helper functions
def add_log(update, people, follow_or_unfollow, usernames):
    # Adding the log information
    if update:
        from datetime import date
        from datetime import datetime

        current_time = datetime.now().strftime("%H:%M:%S")
        today = date.today()
        log = open('log.txt', 'a+')

        if follow_or_unfollow == 'follow':
            message = f'when {people} new follows were made: {usernames}'
        elif follow_or_unfollow == 'unfollow':
            message = f'when {people} were unfollowed: {usernames}'
        else:
            print(f'Third var to add_log() should be either "follow" or "unfollow". But found: {follow_or_unfollow}')
            return

        log.write(
            f'\nLast updated: {today.day}/{today.month}/{today.year} at {current_time}, {message}')

        log.close()


def click_next():
    """
    Clicks next image. If the last image is reached, this method will click the previous button.
    :return: None
    """
    try:
        time.sleep(2)
        # finds the button which gives the next picture
        next_button = chrome.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
        time.sleep(1)

        next_button.click()
    except NoSuchElementException:
        try:
            next_button = chrome.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')
            time.sleep(0.8)
            next_button.click()
        except NoSuchElementException:
            print('No image is opened')


def like_picture():
    """
    If the picture is already liked, it will be unliked!
    :return: None
    """
    time.sleep(5)
    like = chrome.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
    time.sleep(2)

    try:
        like.click()  # clicking the like button
    except NoSuchElementException:
        print('Cannot find a like button. Click on a post first')


def unfollow_usernames(usernames):
    for username in usernames:
        if len(username) > 0:
            unfollow(username)


def follow_usernames(usernames):
    for username in usernames:
        if len(username) > 0:
            follow(username)


def shutdown():
    """
    This method must be called at the end to automatically shutdown the computer
    Use this method in case you are performing a long operation using this program and want to shut down
    your PC after it completes.
    :return: None
    """
    os.system("shutdown /s /t 1")
