from enum import Enum
from fastapi import APIRouter, Path
from fastapi.param_functions import Query
from fastapi.responses import JSONResponse
from user_app.schemas.user_schemas import User


user_router = APIRouter(
    prefix='/users'
)


class Profession(str, Enum):
    backend_engineer = 'backend_engineer'
    frontend_engineer = 'frontend_engineer'
    data_engineer = 'data_engineer'
    full_stack_engineer = 'full_stack_engineer'



USERS = {
    1: {'name': 'danish', 'age': 28, 'city': 'srinagar', 'profession': 'backend_engineer'},
    2: {'name': 'owais', 'age': 28, 'city': 'srinagar', 'profession': 'backend_engineer'},
    3: {'name': 'basit', 'age': 28, 'city': 'srinagar', 'profession': 'frontend_engineer'},
    4: {'name': 'qais', 'age': 28, 'city': 'srinagar', 'profession': 'data_engineer'},
}


@user_router.get('/')
def users(user_id: int = Query(None, gt=0, title='ID of the User;', descritpion='Please Enter the ID of the User;'),
        profession: Profession = Query(None, title='Profession of the User;', descritpion='Please Enter the Profession of the User;')):
    
    if user_id:
        return JSONResponse(USERS.get(user_id, {'Error': 'User with this id not found;'}))

    elif profession:
        users = list()
        for bio in USERS.values():
            if bio.get('profession') == profession.value:
                users.append(bio)

        return JSONResponse(users)
    
    else:
        return JSONResponse(USERS)


# @user_router.get('/{user_id}/')
# def get_user(user_id: int = Path(..., gt=0, title='ID of the User;', descritpion='Please Enter the ID of the User;')):
#     return JSONResponse(USERS.get(user_id, {'Error': 'User with this id not found;'}))


# @user_router.get('/{profession}/')
# def get_users_by_profession(profession: Profession):
    
#     users = list()
#     print(profession, '...profession...')
#     for bio in USERS.values():
#         if bio.get('profession') == profession.value:
#             users.append(bio)

#     return JSONResponse(users)


if __name__ == '__main__':
    user = User(id=1, name='danish wani', age=28, city='Srinagar', married=False)
    # print(User, '????? User????', dir(User))
    print(User.validate(user))
