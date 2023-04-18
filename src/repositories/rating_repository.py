from src.models import *
from google.oauth2 import id_token
from google.auth.transport import requests

class RatingRepository:

    def get_all_ratings(self):
        ratings = Ratings.query.all()
        return ratings
    
    def get_rating_by_id(self, rating_id):
        single_rating = Ratings.query.get(rating_id)
        return single_rating

    def get_ratings_by_prof_course(prof_first_name, prof_last_name, subject, course_num):
        professor = Professors.query.filter_by(first_name=prof_first_name, last_name=prof_last_name).first()
        course = Courses.query.filter_by(subject=subject, course_num=course_num).first()

        if professor and course:
            professor_course = Professor_course.query.filter_by(professor_id=professor.professor_id, course_id=course.course_id).first()
            if professor_course:
                ratings = Ratings.query.filter_by(professor_course_id=professor_course.professor_course_id).all()
                return ratings
        return None

    def create_rating(user_id, first_name, last_name, subject, course_num, rating, semester, comments):

    # Get the professor_id
        get_prof_id_by_name(first_name, last_name)
        
    # Get the course_id
        course = Courses.query.filter_by(subject=subject, course_num=course_num).first()
        course_id = course.course_id
    # Get user_id
        user = Users.query.filter_by(email=idinfo['email']).first()
        user_id = user.user_id
    # Create a new Rating object
        new_rating = Ratings(user_id=user_id, professor_id=professor_id, course_id=course_id, rating=rating, semester=semester, comments=comments)

    # Add the new rating to the session and commit to the database
        db.session.add(new_rating)
        db.session.commit()

    # Return the new rating object
        return new_rating
    
    

    def get_reviews_by_class(self, class_name):
        #Abstract
        return

    def get_prof_id_by_name(self, first_name, last_name):
        professor = Professors.query.filter_by(first_name=first_name, last_name=last_name).first()
        professor_id = professor.professor_id
        return professor_id
    
    def get_course_id_by_subj_num(self, subject, course_num):
        return

    def get_user_by_email(self, email):
        return Users.query.filter_by(email=email).first()
    
    def create_user(self, first_name, last_name, email, google_id):
        new_user = Users(first_name=first_name, last_name=last_name, email=email, google_id=google_id)
        db.session.add(new_user)
        db.session.commit()
        return new_user
        



# Singleton to be used in other modules
rating_repository_singleton = RatingRepository()
