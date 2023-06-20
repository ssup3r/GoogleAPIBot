import get_api
import questionary

# print(get-api_get_assingments())

all_assingments = get_api.get_assingments()

coursechoices = [
    {
        'type': 'select',
        'message': "Please Sign-In before accessing the database",
        'name': 'login',
        "choices": all_assingments.keys()
    }
]

course = questionary.prompt(coursechoices)

all_assingments.get(course)

# for course, assingments in all_assingments.items():
#     print(course)
#     for assingment in assingments:
#         if isinstance(assingment.get('description'), str):
#             if "Import grade" in assingment.get('description'):
#                 continue
#         for key, value in assingment.items():
#             if key == 'description':
#                 print(f"{key}:\n{value}")
#             else:
#                 print(f"\t{key}: {value}")
#     print('\n')