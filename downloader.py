#! /usr/bin/env python3
# -*- coding: utf8 -*-

import lyricwikia as lw
from bs4 import BeautifulSoup
import requests
import pandas as pd

artist = str(input("Please input the name of an artist: "))

#listOfArtists = open("list-of-musicians.txt", "r")
#artists = listOfArtists.read().strip().split()


def meter():
    readLyrics = open("lyrics.txt", "r")
    lyrics = readLyrics.read().strip().split()
    numberOfSwears = 1
    numberOfWords = 1


    #   FROM https://www.cs.cmu.edu/~biglou/resources/bad-words.txt
    readBadWords = open("bad-words.txt", "r")
    badWords = readBadWords.read().strip().split()
    for bad in badWords:
        for word in lyrics:
            if word == bad:
                numberOfSwears += 1
    numberOfWords = len(lyrics)
    readBadWords.close()
    readLyrics.close()
    return str(numberOfWords), str(numberOfSwears), numberOfWords / numberOfSwears

def getNames():
    links = []
    swap = []

    baseurl = "http://lyrics.wikia.com/wiki/"

    url = baseurl + artist
    page = requests.get(url)
    names = [] 

    soup = BeautifulSoup(page.content, "html.parser")
    links.append(soup.find_all("ol"))
    for link in links:
        link = str(link)
        swap = link.split(":")
    #   Select only the odd ones so it isn't duplicated
    links = []
    for i in range(len(swap)):
        if not i % 2 == 0:
            links.append(swap[i])
    
    swap = []
    for link in links:
        swap.append(link.split('"'))
   
    swap = []
    for i in range(len(links)):
        swap.append(links[i].split('"'))
    
    links = []
    for i in swap:
        if i not in links:
            links.append(i)
        
    for link in links:
        names.append(link[0]) 
    
    if "decimal" in names: names.remove("decimal") 
    
    for name in names:
        for nam in name:
            nam = nam.replace('%27', '\'')
    
    return names

def getLyrics():
    #   Clear the text file
    open("lyrics.txt", "w").close()
    #   Open to write in the file
    f = open("lyrics.txt", "w")
    
    lyrics = ""

    names = getNames()
    for name in names:
        try:
            lyrics = lw.get_lyrics(artist, name)
        except:
            print("Couldn't find a song. Song name: " + name)
        
        f.write(lyrics)
        f.write("\n\n!separator\n\n")
    f.close()

if __name__ == '__main__':
    getLyrics()
    words, swears, division = meter()
    print("I have detected %s curse words, in a total of %s words. This means that in average, every %i words is a slang." % (swears, words, division))
    print("Finished")
