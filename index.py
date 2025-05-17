from flask import Flask, request, jsonify, render_template
from flask_cors import CORS 

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
        


app = Flask(__name__)
CORS(app)   


@app.route("/")
def home():
    return render_template('index.html')    


@app.route('/recommended',methods=['POST'])
def recommended_people():
    data = request.json
    email = data.get('email')
    people_network = Recommendation(connectons=get_recommendation_dict())

    recommend_people = people_network.neighbour(user = email)

    return jsonify({'remonneded_people':recommend_people})

if __name__=='__main__':
    app.run(debug=True)
   