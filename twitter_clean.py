import twitter

class Tweet(object):

    def __init__(self):
        self.api = twitter.Api(
        #add your consumer key
        consumer_key='', 
        #add your consumer secret
        consumer_secret='', 
        #add your access token key
        access_token_key='', 
        #add your access token secret
        access_token_secret='')
       
    def sendingtweet(self, enter):
        self.enter = enter
        status = self.api.PostUpdate(self.enter)
        print "Tweet sent"
        print status.text
        
if __name__ == '__main__':        
    twitters = Tweet()
    twitters.sendingtweet(raw_input("Enter tweet here > "))
