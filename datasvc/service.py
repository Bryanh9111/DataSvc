# Databricks notebook source
import os
import csv
from datasvc.models import DataModel

def get_data_from_csv():
    data = []
    # Get the current directory of the script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Define the relative path to the CSV file
    file_path = os.path.join(base_dir, '..', 'data', 'file1.csv')
    
    # Open and read the CSV file
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data_model = DataModel(row['H1'], row['H2'], row['H3'], row['H4'], row['H5'], row['H6'])
            data.append(data_model.to_dict())
    
    return data