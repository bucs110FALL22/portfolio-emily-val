import requests

class YoutubeAPI:
  def init(self, api_key):
    self.api_key = api_key

  def get_video_data(self, video_id):
    url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id=%7Bvideo_id%7D&key=%7Bself.api_key%7D"
    response = requests.get(url)
    return response.json()

  def get_video_views(self, video_id):
    data = self.get_video_data(video_id)
    return data["items"][0]["statistics"]["viewCount"]