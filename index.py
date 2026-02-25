import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS 

from schema import get_recommendation_dict
from rcmd import Recommendation
from middleware.auth_token import token_required
      


app = Flask(__name__)
CORS(app)   
frontend_url = os.getenv('FRONTEND_END_URL')
CORS(app, resources={
    r"/recommended": {"origins": [frontend_url,"http://localhost:5173"]}
})

@app.route("/")
@token_required
def home():
    return render_template('index.html')    


@app.route('/recommended',methods=['POST'])
@token_required
def recommended_people():
    # data = request.json
     # email = data.get('email')

    user_data = request.user #from token
    email = user_data.get("email")
    
    people_network = Recommendation(connectons=get_recommendation_dict())

    recommend_people = people_network.neighbour(user = email)
    

    return jsonify({'recommended_people':recommend_people})

if __name__=='__main__':
    app.run(debug=False)
   