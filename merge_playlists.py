# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 09:50:45 2022

@author: Joao

Objective: merge any number of spotify playlists into unique URIs, that are
           then used to build a playlist with only unique songs.
           
(intercept.ninja would have solved this issue, but it's offline)

"""

import pandas as pd
import numpy as np

# Export playlists with https://watsonbox.github.io/exportify
playlists = ['rolling_stone_500_greatest_songs_of_all_time_(2004).csv',
             'rolling_stone_500_greatest_songs_of_all_time_(2021).csv']

# example_csv = pd.read_csv(playlists[0])
# print(example_csv)

# Put all URIs in the same list
all_track_URIs = []
for playlist in playlists:
    curr_csv = pd.read_csv(playlist)
    all_track_URIs += curr_csv['Track URI'].values.tolist()


# Select only the unique URIs
unique_URIs = np.unique(np.array(all_track_URIs))

# Save to text
np.savetxt('unique_URIs.csv', unique_URIs, fmt='%s', delimiter=',')

# Now go to www.spotlistr.com/search/file-scraper and upload the file above.
# Then click on "Create Playlist". 

# This method only downloads the songs that you CAN listen in those playlists. 
# Sometimes Spotify removes songs and those you won't be able to listen anymore.
# At the bottom of the page there is a list of songs that either are no longer 
# in spotify, or that have changed address, and the responsible for the playlist
# needs to update that song.
