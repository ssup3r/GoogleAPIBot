import get_api
import questionary
import get_api
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.errors import HttpError
from get_api import api

api_class = api(None)
access_api = api_class.access_api()


creds = api_class.creds

if __name__ == '__main__':
    api_class.access_api()

try:
    api = build('classroom', 'v1', credentials=creds)
    courses = api.courses().list().execute()
    courses_alias = api.courses().aliases().list().execute()
except HttpError as error:
    print('An error occurred: %s' % error)

def get_courses_all():
    all_courses = courses.get('courses', [])
    # all_courses_aliases = courses_alias.get('aliases', [])
    
    if not courses:
        print("No courses found!")
        return
    
    courses_name_list = []
    courses_id_list = []
    courses_alias_list = []

    for course in all_courses:
        get_courses_name = course['name']
        get_courses_id = course['id']
        courses_name_list.append(get_courses_name)
        courses_id_list.append(get_courses_id)
    # for course_alias in all_courses_aliases:
    #     get_courses_alias = course_alias['alias']
    #     courses_alias_list.append(get_courses_alias)

    courses_list_formatted = '\n'.join(courses_name_list, courses_id_list, courses_alias_list)
    return courses_list_formatted

get_all_courses = get_courses_all()

print(get_all_courses)

# Wait for discord's data to be passed to the bot
# def get_specific_course_data():
#    specific_course = courses.get('courses', [course_id])