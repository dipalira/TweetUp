This is the complete repo for final project of CS598 Social Sensing at University of Illinois at Urbana-Champaign.


**Abstract** —This paper proposes a new method of recommending events and twitter accounts to follow, by fusing the best features of two social medias- Twitter and Meetup. We aim to connect people possible having similar social interest, who can potentially meet and increase the impact in their communities. This would help in increasing the number of social movements and social reform campaigns in community. We answer three main questions in this paper, - Do people share same ideas on both social media, Can we recommend meetups based on users profile, Is it better to recommend users from twitter or from meetup.

   Our proposed Algorithm is shown in Fig. 1, where we take the user’s tweets, clean it then we input the clean data invthe multi classification model, the model classifies the set of tweets into category(i.e. social interest) the user is interested in, based on that result we get the events in this category at the user’s specific location, we get the organizers’ of these events twitter data, and apply topic modeling the ones with the most frequent words resembling the category are suggested to the
user.
    We also rank the events in descending order starting from the events the most similar to user’s twitter profile. Last thing we recommend, is topics that they can follow on meetup, which can increase their meetup activity.
![alt text](https://github.com/dipalira/TweetUp/blob/master/image.png "Data Pipeline Flow")
### Author - Shaima AbdulMajeed and  Dipali Ranjan
Department of Computer Science,  University of Illinois at Urbana-Champaign
