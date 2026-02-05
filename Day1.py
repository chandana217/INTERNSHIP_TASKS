class Instagram:
     def __init__(self,title, description,comments,creator_name,location): 
         self.title = title
         self.description = description
         self.likes = 0
         self.comments=comments
         self.creator_name=creator_name
         self.location=location
     def display_title(self):
         print("The title of the reel is ",self.title)
     def display_description(self):
         print("The description of the reel is",self.description)
     def display_likes(self):
         print("The likes of the reel is ",self.likes)
     def liked(self):
         self.likes += 1
     def disliked(self):
         if self.likes > 0:
             self.likes-=1
     def display_comments(self):
         print("The comments of the reel is ",self.comments)
     def display_creator_name(self):
         print("The creator name of the reel is ",self.creator_name)
     def display_location(self):
         print("The location of the reel is ",self.location)
reel1=Instagram("dancing","dancing with friends","Nice Dance","Chandana","Mysuru")
# 0
reel1.disliked() #0
reel1.liked() #1
reel2=Instagram("finance minister conference","finance minister conference with friends","Good","News First","Delhi")

reel1.liked() #2
# 0
reel2.liked() #1
reel1.disliked() #1
reel1.display_likes()
reel2.display_likes()
print(id(reel1))
print(id(reel2))
reel1.display_comments()
reel2.display_comments()
reel1.display_creator_name()
reel2.display_creator_name()
reel1.display_location()

reel2.display_location()
