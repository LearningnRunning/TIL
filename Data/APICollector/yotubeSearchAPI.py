#!/usr/bin/python
import json
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import streamlit as st

import pandas as pd
# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = st.secrets["DEVELOPER_KEY"]
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


class Options:
    def __init__(self):
        self.q = None
        self.max_results = None
        self.tag_bool = None

def collectInfo(search_result, videoType):
    thumbnails_url = search_result['snippet']['thumbnails']['high']['url']
    channel_title = search_result['snippet']['channelTitle']
    title = search_result['snippet']['title']
    channel_id = search_result['snippet']['channelId']
    video_id = search_result['id'][f'{videoType}Id']
    video_url = f'https://www.youtube.com/watch?v={video_id}'
    created_at = search_result['snippet']['publishedAt']
    description = search_result['snippet']['description']
    
    return {
        'thumbnails_url': thumbnails_url,
        'channel_title': channel_title,
        'title': title,
        'channel_id': channel_id,
        'video_id': video_id,
        'video_url': video_url,
        'created_at': created_at,
        'description': description
    }

def youtube_search(options):

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
    q=options.q,
    part="id,snippet",
    maxResults=options.max_results,
    order='rating',
    regionCode = "JP",
    type="video",
    ).execute()



    all_results = {}
    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        video_type = search_result["id"]["kind"].split("#")[-1]
        info_dict = collectInfo(search_result, video_type)
        if options.tag_bool:
            tag_response = youtube.videos().list(
            part="snippet",
            id = info_dict['video_id']
            ).execute()

            video_tags = tag_response['items'][0]['snippet'].get('tags', [])
            info_dict['video_tags'] = video_tags

        all_results[info_dict['video_id']] = info_dict

        # info_df = pd.DataFrame.from_dict(info_dict)
        # all_df = pd.concat([all_df, info_df])

    return all_results




# Create an instance of the Options class
options = Options()

# Set the value of q
options.q = "韓国化粧法"
options.max_results = 25
options.tag_bool = True

with open('AllSearchData.json', 'r') as file:
    # Load the contents of the file into a dictionary
    all_search_dict = json.load(file)


search_response_dict = youtube_search(options)
all_search_dict.update(search_response_dict)

# Convert JSON data to DataFrame
df = pd.DataFrame.from_dict(search_response_dict, orient='index')

# Save the dictionary as JSON
with open("AllSearchData.json", "w") as json_file:
    json.dump(all_search_dict, json_file)
