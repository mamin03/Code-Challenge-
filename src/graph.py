import math

def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n

def calculate_avg(graph):
  nodes = 0.00
  count = 0.00
  for i in graph:
     nodes+=len(set(graph[i]))
     count += 1
  if count>0:
    return '{:0.2f}'.format(truncate((nodes/count),2),2)
  else:
    return '{:0.2f}'.format(0.00)


def make_graph(tweets):
  graph={}
  for i in tweets:
    n = len(i.nodes)
    if n>1:                    # to count for disconnected nodes
      edges=[]
      for j in xrange(n):
        edges.append(i.nodes[j])
        d = i.nodes[j]
        if d not in graph:
          graph[d]=[i.nodes[x] for x in xrange(j+1, n)]+edges[0:j]
        else: # and in 60s time frame
          graph[d]+=[i.nodes[x] for x in xrange(j+1, n)]+edges[0:j]
  return graph


def update_list(tweets, new_tweet):
  n = len(tweets)
  if n==0:
    tweets.append(new_tweet)
    return tweets
  d = new_tweet.time_stamp - tweets[-1].time_stamp
  if d.total_seconds() <= -60:
    return tweets
  index = 0
  for i in tweets:
      d = new_tweet.time_stamp - i.time_stamp
      if d.total_seconds() < 60:
        tweets.append(new_tweet)
        return tweets[index:]

      elif d.total_seconds() > -60 and d.total_seconds() < 0:
        tweets.append(new_tweet)
        newlist = sorted(tweets, key=lambda x: x.time_stamp, reverse=True)

      elif d.total_seconds() >= 60:
        index+=1
  return tweets[index:]
 
