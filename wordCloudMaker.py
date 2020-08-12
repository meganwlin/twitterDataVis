from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import csv
from nltk.corpus import stopwords
import os
from os import listdir
import os.path

#got tweets from https://www.vicinitas.io/free-tools/download-user-tweets
STOPWORDS=["#",":",".",",",";","@","&","https","http","RT","co","Thank","today","country","amp","realDonaldTrump","get","let","American","people","AOC","America","one","us","like"]
STOPWORDS.extend(stopwords.words('english'))


def extractTweets(path):
    text=""
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for row in reader:
            text+=" "+row[0]
    return text
    
# Choosing the color palette for the words in your word cloud
def multi_color_func(word=None, font_size=None,
                         position=None, orientation=None,
                         font_path=None, random_state=None):
        colors = [[352, 70, 42],
                  [218, 58, 62],
                  [0, 1, 51],
                  [241, 30, 33],
                  [215, 35, 44],
                  [0, 70, 42]]
        rand = random_state.randint(0, len(colors) - 1)
        return "hsl({}, {}%, {}%)".format(colors[rand][0], colors[rand][1], colors[rand][2])

def userTopicTweets(user, topic_list):
    path='tweets/'+user+"_user_tweets.csv"
    text=""
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for row in reader:
            tweet=row[0]
            for topic in topic_list:
                if topic in tweet.lower(): #if the tweet is associated with the topic
                    text+=" "+row[0]
                    break
        
    return text
    
# generate word cloud for each twitter user
twitter_path="tweets/"
tweet_files = [f for f in listdir(twitter_path) if (os.path.isfile(os.path.join(twitter_path, f)) and (f.endswith('.csv')))] 
users=[]
for file in tweet_files:
    username=file.split("_user_tweets")[0]
    users.append(username)
    
    path='tweets/'+file
    text=extractTweets(path)
    
    mask = np.array(Image.open('masks/'+username+".jpg"))
    
    wc = WordCloud(background_color="white", max_words=400,
                   stopwords=STOPWORDS, max_font_size=200,
                   random_state=42, width=mask.shape[1],
                   height=mask.shape[0], mask=mask,color_func=multi_color_func,
                  collocations=False)
    wc.generate(text)

    plt.figure( figsize=(20,10), facecolor='k')
    plt.title('Wordcloud of key '+username)
    plt.imshow(wc)
    plt.axis("off")
    
    if not os.path.isdir('word clouds/'+username+'/'):  
        os.mkdir('word clouds/'+username)  
    plt.savefig('word clouds/'+username+'/'+username+'_wordcloud.png', facecolor='k')


#generate word cloud for each twitter user about specific topics
topics={}
topics["Black Americans"]=["african", "black","african-american"]
topics["China"]=["china", "chinese","chinese-american"]
topics["Coronavirus"]=["coronavirus", "covid","covid-19","cdc","outbreak","symptom",'mask']
topics["Trump"]=["donald", "trump"]
topics["Obama"]=["barack", "obama"]
topics["News"]=["news", "cnn",'abc','foxnews','nytimes','usatoday','washingtonpost','media', 'report','reporter','reporters','media','press','interview']

for user in users:
    for topic in topics.keys():
        text=userTopicTweets(user,topics.get(topic))
        if len(text)>0: #skips over if there aren't enough tweets about the topic
            mask = np.array(Image.open('masks/'+user+".jpg"))
            
            wc = WordCloud(background_color="white", max_words=400,
                           stopwords=STOPWORDS, max_font_size=400,
                           random_state=42, width=mask.shape[1],
                           height=mask.shape[0], mask=mask,color_func=multi_color_func,
                          collocations=False)
            wc.generate(text)
            plt.figure( figsize=(20,10), facecolor='k')
            plt.imshow(wc)
            plt.axis("off")
            plt.savefig('word clouds/'+user+'/'+user+"_"+topic+'_wordcloud.png', facecolor='k')
        print("User: ",user, ", Topic: ",topic)
        print(len(text))
