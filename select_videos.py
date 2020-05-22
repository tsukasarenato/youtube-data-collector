import googleapiclient.discovery

my_api_key = 'your key'
api_service_name = 'youtube'
api_version = 'v3'

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=my_api_key)


def collect_video_data(q, y):

    """
    This function collects data from YouTube videos

    :param q: words used to search for videos on Youtube
    :param y: year
    :return: Returns data from searched YouTube videos
    """

    results = youtube.search().list(
        part='snippet',
        q=q,
        type='video',
        publishedAfter=y+'-01-01T00:00:00Z',
        publishedBefore=y+'-12-31T00:00:00Z',
        order='viewCount',
        maxResults=50
                               ).execute()

    print('50 videos returned')
    
    return results


def format_information(video_list, name):

    """
    This function formats the information of the collected videos and writes them to a JSON file

    :param video_list: Youtube video data
    :param name: name of the JSON file
    :return: JSON file
    """
    
    text = '['
    
    for video in video_list['items']:
        
        info = video['id']
        text += '{\n'
        text += '"' + 'ID": ' + '"' + str(info['videoId']) + '",\n'
        
        info = video['snippet']
        text += '"' + 'Title": ' + '"' + str(info['title']) + '",\n'
        text += '"' + 'Channel": ' + '"' + str(info['channelTitle']) + '",\n'
        text += '"' + 'Date": ' + '"' + str(info['publishedAt']) + '",\n'
        text += '"' + 'Description": ' + '"' + str(info['description']) + '",\n},\n'
    
    text += ']'
        
    with open('database/videos/'+name+'.json', 'w', encoding="utf8") as file:
        file.write(text)
    
    print('Information was stored in json file')


words = ['cs go', 'anime', 'basketball']

year = '2018'

for word in words:
    videos = collect_video_data(word, year)
    format_information(videos, word)

