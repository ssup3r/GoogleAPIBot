from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token_path.
SCOPES = [
    'https://www.googleapis.com/auth/classroom.courseworkmaterials.readonly',
    'https://www.googleapis.com/auth/classroom.student-submissions.students.readonly',
    'https://www.googleapis.com/auth/classroom.courses.readonly',
    'https://www.googleapis.com/auth/classroom.student-submissions.me.readonly',
]

file_path = os.path.dirname(os.path.abspath(__file__))
secret_path = os.path.join(file_path, "GoogleSecrets")
cred_path = os.path.join(secret_path, 'credentials.json')
token_path = os.path.join(secret_path, 'OAuthToken.json')


def get_assingments():
    """Shows basic usage of the Classroom API.
    Prints the names of the first 10 courses the user has access to.
    """
    creds = None
    # The file token_path stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.log
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                cred_path, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('classroom', 'v1', credentials=creds)

        # Call the Classroom API
        results = service.courses().list().execute()
        courses = results.get('courses', [])

        if not courses:
            print('No courses found.')
            return
        # # Prints the names of the first 10 courses.
        # print('Courses:')
        # for course in courses:
        #     print(course['name'])

    except HttpError as error:
        print('An error occurred: %s' % error)
    try:
        service = build('classroom', 'v1', credentials=creds)

        # Call the Classroom API to retrieve all courses
        results = service.courses().list().execute()

        courses = results.get('courses', [])

        if not courses:
            print('No courses found.')
            return

        # Prints the details of the assignments for each course
        # print('Assignments:')

        all_assingments = {}

        for course in courses:
            course_id = course.get('id')
            course_name = course.get('name')

            # Call the Classroom API to retrieve assignments for the course
            results = service.courses().courseWork().list(courseId=course_id).execute()
            assignments = results.get('courseWork', [])

            all_assingments[course_name] = assignments
        
        return all_assingments

        """# if not assignments:
        #     print(f'No assignments found for course: {course_name}')
        # else:
        #     print(f'Assignments for course: {course_name}')
        #     return assignments
            # for assignment in assignments:
            #     for key, value in assignment.items():
            #         print(f'{key}: {value}')
                # courseId
                # id
                # title
                # description
                # materials
                # state
                # alternateLink
                # creationTime
                # updateTime
                # dueDate
                # dueTime
                # maxPoints
                # workType
                # submissionModificationMode
                # creatorUserId
                # topicId
        """


    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    get_assingments()