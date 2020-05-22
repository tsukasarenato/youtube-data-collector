import googleapiclient.discovery
import json

my_api_key = 'your key'
api_service_name = "youtube"
api_version = "v3"

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey = my_api_key)


def collect_comments(youtube, videoId, pageToken):
    results = youtube.commentThreads().list(
        part="snippet,replies",
        maxResults=100,
        videoId=videoId,
        textFormat="plainText",
        pageToken=pageToken
    ).execute()
    return results


def write_json_file(comments, name):
    text = ''
    for item in comments['items']:
        
        comment = item["snippet"]["topLevelComment"]["snippet"]
        text += 'author: ' + comment['authorDisplayName'] + '\n' 
        text += 'comment: ' + comment["textDisplay"].replace("\n", ". ") + '\n' 
        text += 'date: ' + comment["updatedAt"] + '\n'
        text += 'like: ' + str(comment["likeCount"]) + '\n\n'
        if 'replies' in item.keys():
            replies = item["replies"]["comments"]
            text += '\nreplies: \n'
            for replie in replies:
                text += 'author: ' + replie["snippet"]['authorDisplayName'] + '\n' 
                text += 'comment: ' + replie["snippet"]["textDisplay"].replace("\n", ". ") + '\n' 
                text += 'date: ' + replie["snippet"]["updatedAt"] + '\n'
                text += 'like: ' + str(replie["snippet"]["likeCount"]) + '\n\n'
                
        
    with open('database/comments/'+name+'.txt', 'w', encoding="utf8") as file:
        file.write(text)
    
    print('Information was stored in txt file')

videos = ['MX82C2rQSXo']


for video in videos:
    comments = collect_comments(youtube, video, '')
    write_json_file(comments, video)
    
