import meetup.api
import json
import tweepy
import csv


####input your credentials here
consumer_key = 'Pq3To6LvqW9YVA5OxvMvKiqad'
consumer_secret = 'tmxB28Fi7Z4nlbVBeiSYreFop5QfKi5v9oUkyZt9Fdj91h0byF'
access_token = '910003033945362432-km5fG4uNtuBsheRTHwvhq4qo5Da43XP'
access_token_secret = 'ylU23ezVBOpYcgVfeNsodgxTeiRXR24uAmm4nYJuew37p'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


from pprint import pprint
client = meetup.api.Client('294e1d2d1d3814291a13773f781c792a')

def get_group_zip():
    with open("groups_01_fin.json", 'w') as output_file:
        with open('zipcodes_orig.txt', 'r') as input_file:
            #for i in range(13,15):
            count = 0
            json_data = []
            for zip in input_file.readlines():
                if count == 10000:
                    break
                count += 1
                try:
                    group_info = client.GetFindGroups({'category': 13, 'zip': zip.strip(), 'radius': 1, 'fallback_suggestions': 0})
                except:
                    pass
                #print group_info.__dict__.keys()
                json_data.append(group_info.items)
                try:
                    if group_info.items[0]['state'] != "IL":
                        json_data.append(group_info.items)
                except:
                    pass
            json.dump(json_data, output_file)
def get_members_place():
    with open("groups_02_fin.json", 'r') as f:
        data = json.load(f)
        members_ids = []
        for d in data:
            if d != []:
                pprint(d)
                members_ids.append(d[0]["organizer"]["id"])
        #print data["member"]["id"]
    count = 1
    for member in members_ids:
        client_data = client.GetMembers({'member_id': member}).results
        alltweets = []
        for cli in client_data:
            try:
                screen_name = cli["other_services"]["twitter"]["identifier"]
                # make initial request for most recent tweets (200 is the maximum allowed count)
                new_tweets = api.user_timeline(screen_name=screen_name, count=200)
                # save most recent tweets
                outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in new_tweets]
                alltweets.extend(new_tweets)
                if outtweets != []:
                    with open('UsersData/%s_tweets.csv' % screen_name, 'wb') as f:
                        writer = csv.writer(f)
                        writer.writerow(["id", "created_at", "text"])
                        writer.writerows(outtweets)
                #print(outtweets)
                #o_f.writelines(outtweets)
                #json.dump(new_tweets, o_f)
                    count += 1
            except:
                pass


if __name__ == '__main__':
    get_members_place()
    #get_group_zip()
    print "that's main"