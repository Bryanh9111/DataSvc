# Databricks notebook source
from flask import jsonify
from datasvc import app, api
from datasvc.service import get_data_from_csv
from flask_restx import Resource

ns = api.namespace('data', description='Data operations')

@ns.route('/read')
class DataRead(Resource):
    def get(self):
        """
        Read data from CSV and return as JSON
        """
        data = get_data_from_csv()
        return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
