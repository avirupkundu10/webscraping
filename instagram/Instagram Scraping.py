# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 20:39:34 2023

@author: kundu
"""
import instaloader
bot = instaloader.Instaloader()
profile = instaloader.Profile.from_username(bot.context, 'sampurna_c')
print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers: ", profile.followers)
print("Followees: ", profile.followees)
print("Bio: ", profile.biography,profile.external_url)

# Login with username and password in the script
bot.login(user="your username",passwd="your password")

# Interactive login on terminal
bot.interactive_login("your username")
# Retrieve the usernames of all followers
followers = [follower.username for follower in profile.get_followers()]

# Retrieve the usernames of all followees
followees = [followee.username for followee in profile.get_followees()]
print(followers)

# Load a new profile
profile = instaloader.Profile.from_username(bot.context, 'wwe')

# Get all posts in a generator object
posts = profile.get_posts()

# Iterate and download
for index, post in enumerate(posts, 1):
    bot.download_post(post, target=f"{profile.username}_{index}")

