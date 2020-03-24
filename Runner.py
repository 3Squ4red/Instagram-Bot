import bot

# The following two lines reads all the usernames and stores them in
# var 'usernames' pass this var as parameter to bot.unfollow_usernames() to unfollow
# every account in Following.txt.
file = open('Following.txt', 'r')
usernames = file.read().split(',')

# Call the desired function below


print('Exiting bot...')
