from youtube_dl import YoutubeDL



YDL_OPTIONS = {'format': 'bestvideo', 'noplaylist':'True'}

def search_download(search_str, numOf_results):
    with YoutubeDL({'format': 'bestaudio', 'noplaylist': 'True'}) as ydl:
        videos = ydl.extract_info(f"ytsearch{numOf_results}:{search_str}", download=True)['entries']
        return [ydl.prepare_filename(video) for video in videos]


if __name__ == '__main__':
    # TODO you can change to any search string you want
    downloaded_files = search_download('הגשש', 5)

    # TODO use downloaded_files and complete a few lines to upload them to an S3 bucket

