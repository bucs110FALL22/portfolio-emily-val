class DataAnalysis:
    def __init__(self):
        self.video_data = []

    def add_video_data(self, video_data):
        self.video_data.append(video_data)

    def __len__(self):
        return len(self.video_data)

    def __str__(self):
        output_str = "Video data:\n"
        for data in self.video_data:
            output_str += f"Title: {data['snippet']['title']}\n"
            output_str += f"Duration: {data['contentDetails']['duration']}\n"
            output_str += f"View count: {data['statistics']['viewCount']}\n"
        return output_str

    def find_optimal_video_settings(
