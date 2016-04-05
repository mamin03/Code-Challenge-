import sys
import json
import dateutil.parser
from graph import calculate_avg, make_graph, update_list

input = sys.argv[1]
output = sys.argv[2]
f = open(input)
out = open(output, 'w+') 


class Item:
  def __init__(self, nodes, time_stamp):
    self.nodes = nodes
    self.time_stamp = time_stamp


tweets=[] 
for i in f:
  json_data = json.loads(i)
  if 'limit' not in json_data:   # ignore the limiting message
    t = json_data['created_at']
    t = dateutil.parser.parse(t)
    hashtags = json_data['entities']['hashtags']
    nodes=[]
    for j in hashtags:
      nodes.append(j['text'])
    new_tweet = Item(nodes, t)
    tweets = update_list(tweets, new_tweet)
    g=make_graph(tweets)
    out.write(str(calculate_avg(g))+'\n')
