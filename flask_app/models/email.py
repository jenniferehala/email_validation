from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Email:
    def __init__(self,data):
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def save(cls,data):
        query="INSERT INTO email (email) VALUES (%(email)s);"
        return connectToMySQL("dojo_survey_schema").query_db(query,data)
    
    @staticmethod
    def validate_email(email_data):
        email_reg = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        if len(email_data["email"]) < 1:
            flash("We need email")
            is_valid = False
        if not email_reg.match(email_data['email']):
            flash("Invalid email ADDRESS/password")
            is_valid = False
        return is_valid
    
    @classmethod
    def get_emails():
        query="SELECT email, created_at FROM email"
        survey_db = connectToMySQL("email_db").query_db(query)
        users = []
        for survey in survey_db:
            users.append(Email(survey))
        return users