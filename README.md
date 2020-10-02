# Instagram-Bot
An Instagram bot that can follow, unfollow accounts and also like posts of those accounts or a given hashtag.

### Please read the below instructions before using this bot! ###

First of all, open the following files and delete all of their contents:
1. *Following.txt*
2. *log.txt*
3. *credentials.txt*

Then place your username/email id and password on the **credentials.txt** file on **SEPERATE LINES!** Like this:

*exampleusername*

*mypass23_90*

Following are the functions(in bot.py) that you would wish to call(in Runner.py). Please make sure to pass a value whose type matches exactly as mentioned below:

**1. follow(str)**

**2. unfollow(str)**

**3. follow_usernames(list)**

**4. unfollow_usernames(list)**

**5. like_and_follow_posts_of_username(str, int(-1 by default), bool(False by default))**

**6. like_and_follow_posts_of_hashtag(str, int, int, bool(False by default))**

To use this bot, you have to know at least how to call Methods/Functions in python and how to pass arguments to them. Below is the list of actions you can perform using this bot and also the instructions on how to perform them:

Open the *Runner.py* file and on the 10th line of the file call your desired function according to the instructions below:

1. *To Follow account(s)*: If you want to follow only one account, type '*bot.follow(**username of the account**).*' If you're up to follow more than one account, pass a list of usernames of those accounts to '*bot.follow_usernames(**list containing all the usernames**)*'. Example of both the cases are as follows:

  **i) bot.follow('garyvee')** 
  
  **ii) bot.follow_usernames(['garyvee', 'chimpanzee.coder', 'programmerplus'])** 
  
2. *To Unfollow account(s)*: If you want to unfollow only one account, type '*bot.unfollow(**username of the account**).*' If you're up to unfollow more than one account, pass a list of usernames of those accounts to '*bot.unfollow_usernames(**list containing all the usernames**)*'. Example of both the cases are as follows:

   **i) bot.unfollow('garyvee')** 
  
   **ii) bot.unfollow_usernames(['garyvee', 'chimpanzee.coder', 'programmerplus'])**
  
3. *To Like posts of an account but not follow it*: If you want to like posts of an account, use this exact syntax '*bot.like_and_follow_posts_of_username(**username of that account, number of posts you want to like, False**)*'. *If you want to like all the posts of an account pass **-1** as the second parameter*. Examples are as follows:

   **i) bot.like_and_follow_posts_of_username('garyvee', 5, False)**
  
   **ii) bot.like_and_follow_posts_of_username('garyvee', -1, False)**

4. *To Like posts of an account and also follow that account*: If you want to like posts of an account **and** also follow that account, use this exact syntax '*bot.like_and_follow_posts_of_username(**username of that account, number of posts you want to like, True**)*'. *If you want to like all the posts of an account pass **-1** as the second parameter*. Examples are as follows:

   **i) bot.like_and_follow_posts_of_username('garyvee', 5, True)**
  
   **ii) bot.like_and_follow_posts_of_username('garyvee', -1, True)**
  
5. *To Like posts from **Top posts tab/ Recent posts tab** of a certain hashtag but not follow the accounts whose posts are being liked*: If you want to like posts from Top posts tab/ Recent posts tab of a certain hashtag but not follow the accounts whose posts are being liked, use this exact syntax '*bot.like_and_follow_posts_of_hashtag(**desired hashtag, number of posts you want to like, bot.TOP_POSTS/bot.RECENT_POSTS, False**)*'. Examples are as follows:

   **i) bot.like_and_follow_posts_of_hashtag('chimpanzeecoder', 5, bot.TOP_POSTS, False)**
  
   **ii) bot.like_and_follow_posts_of_hashtag('chimpanzeecoder', 5, bot.RECENT_POSTS, False)**

6. *To Like posts from **Top posts tab/ Recent posts tab** of a certain hashtag and also follow the accounts whose posts are being liked.*:  If you want to like posts from Top posts tab/ Recent posts tab of a certain hashtag and also follow the accounts whose posts are being liked, use this exact syntax '*bot.like_and_follow_posts_of_hashtag(**desired hashtag, number of posts you want to like, bot.TOP_POSTS/bot.RECENT_POSTS, True**)*'. Examples are as follows:

   **i) bot.like_and_follow_posts_of_hashtag('chimpanzeecoder', 5, bot.TOP_POSTS, True)**
  
   **ii) bot.like_and_follow_posts_of_hashtag('chimpanzeecoder', 5, bot.RECENT_POSTS, True)**
