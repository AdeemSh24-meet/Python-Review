def create_youtube_video(title,desc):
 	video = {"title": title,"description": desc, "likes": 0,"dislikes": 0,"comments":{}}
 	return video


def like (video):
	if "likes" in video :
		video["likes"] += 1
	return video

def dislike (video):
	if "dislikes" in video :
		video["dislikes"] += 1
	return video


def add_comment ():
	[youtubevideo] = ""
	[username] = ""
	comment={"username":"comment_text"}
	return comment



youtubevideo = create_youtube_video("hi","hh")
print (youtubevideo)
