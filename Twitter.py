from collections import Counter
import re
hashtagRegex = re.compile(r"#[\w]+")

class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.tagList = []

    def tweet(self,mensaje):
        tags = hashtagRegex.findall(mensaje)
        self.tagList.extend(tags)
        l_sorted = Counter(self.tagList).most_common()
        self.trending_topics = [i[0] for i in l_sorted]
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           
