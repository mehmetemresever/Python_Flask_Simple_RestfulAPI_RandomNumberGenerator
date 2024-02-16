from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
import random


app = Flask("RandomNumberGenerator")
api = Api(app)


class RNG(Resource):

	def get(self): # Calling API

		return jsonify({'random_number': random.randint(0, 1000) }) #Return a random number between 0 to 1000 as Default.
	
	def post(self): # Calling API with Paramaters
		parser = reqparse.RequestParser()
		parser.add_argument('start', type=int, required=True, help="Start must be an integer and is required.")
		parser.add_argument('end', type=int, required=True, help="End must be an integer and is required.")
		args = parser.parse_args()
		print(args)
		print(random.randint(args['start'], args['end']))
		return jsonify({'random_number': random.randint(args['start'], args['end'])})
	
	
api.add_resource(RNG, '/rng')


if __name__=='__main__':
	app.run()