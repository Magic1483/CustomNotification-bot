from instagrapi import Client


def get_content(url):
	cl = Client()
	cl.login("morrisjonson4","NfyR1945")

	id=cl.media_pk_from_url(url)

	
	video_url = cl.media_info(id).video_url
	cl.video_download_by_url(video_url, filename='video',folder='/root/tgbot/files')
	








