"""
Main Module file for driving the server
and initial setup of database
"""
import os
from src import api_service
from database import database
from config.dev import DB_NAME, target_path


"""Initalize and setup database schema and tables meta data"""
if not os.path.exists(target_path):
    database.main()

"""Fire up the api services"""
api_service.run()