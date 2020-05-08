# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 21:32:00 2017

@author: Leonardo
"""
import pandas as pd
from db import DemoDB
import time

database = DemoDB()
#print(database.tables)
time.sleep(2)

album = database.tables.Album.all()
print('\n', album.head())

artist = database.tables.Artist.all()
print('\n', artist.head())

album_artist = pd.merge(artist, album)
print('\n', album_artist.head())

album_artist = pd.merge(artist, album, on='ArtistId')
print('\n', album_artist.head())

album.rename(columns={'ArtistId': 'Artist_Id'}, inplace=True)
print('\n', album.head())

album_artist = pd.merge(album, artist, left_on='Artist_Id', right_on='ArtistId')
print('\n', album_artist.head())

album_artist = pd.merge(album, artist, left_on='Artist_Id', right_on='ArtistId').drop('Artist_Id', axis=1)
print('\n', album_artist.head())

