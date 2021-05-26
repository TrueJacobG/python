import instaloader

m = instaloader.Instaloader()
a = input("Paste your name here: ")

m.download_profile(a, profile_pic_only=True)
