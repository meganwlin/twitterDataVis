# twitterDataVis
This project won the UIUC HackThis 2020 Data Science Challenge!

Creating word clouds for various twitter users and separate word clouds for their tweets about specific topics.

The twitter data was gathered using a tool called Vicinitas which can be accessed at: https://www.vicinitas.io/free-tools/download-user-tweets

This tool was able to gather the last 3,200 tweets from the given twitter user in a downloadable file I saved in the tweets folder.

Once this data was gathered, pictures for each of the subjects I wanted to compare were found and downloaded into a folder called masks. These will be used as outlines for the word clouds.

The tweets were then run through a code to generate word clouds with a American color theme and the outlines previously mentioned were used for each user.

The second part of the project, which calls the function userTopicTweets, makes word clouds for each of these Twitter users for specific topics. These tweets were filtered and kept only if they had certain keywords in them. Thus, these word clouds are able to depict frequent wordings these Twitter users used when addressing the chosen subject.

The full explanation in addition to some comparisons using this seconds part of the project can be found in the Explanations and Graphs pdf.
