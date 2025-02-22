
from schema import get_recommendation_dict

class Recommendation:
    def __init__(self,connectons={}):
       
        self.connections = connectons

        # print(self.connections)

    def neighbour(self ,user):
        
        if user not in self.connections:
            return []
        
        recommended_people = set()

        for friend in self.connections[user]:
            if friend in self.connections:
                for friend_of_friend in self.connections[friend]:
                    if friend_of_friend != user and friend_of_friend  not in self.connections[user]:
                        recommended_people.add(friend_of_friend)
    
        return list(recommended_people)
        
        

# dic = {'yugi':['charan','sibi'],'charan':['kiran','vimal'],'sibi':['roshini','samuel'],'kiran':['abc','bbc']}
if __name__ == '__main__':
    data= get_recommendation_dict()
    obj = Recommendation(connectons=data)
    print(obj.neighbour(user='yugeshkaran001@gmail.com'))

