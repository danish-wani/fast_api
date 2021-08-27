
from typing import List
from fastapi import APIRouter
from fastapi.param_functions import Body, Query, Path
from fastapi.responses import JSONResponse
from user_app.schemas.user_schemas import User,Profession


user_router = APIRouter(
    prefix='/users'
)



USERS = {
    1: {'name': 'danish', 'age': 28, 'city': 'srinagar', 'profession': Profession.backend_engineer},
    2: {'name': 'owais', 'age': 28, 'city': 'srinagar', 'profession': Profession.backend_engineer},
    3: {'name': 'basit', 'age': 28, 'city': 'srinagar', 'profession': Profession.frontend_engineer},
    4: {'name': 'qais', 'age': 28, 'city': 'srinagar', 'profession': Profession.data_engineer},
}


@user_router.get('/')
def users(
    user_id: int = Query(None, gt=0, title='ID of the User;', descritpion='Please Enter the ID of the User;'), 
    profession: Profession = Query(None, title='Profession of the User;', descritpion='Please Enter the Profession of the User;')
    ):
    
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


@user_router.get('/files/{file_path:path}/')
def get_file_from_path(file_path: str = Path(..., max_length=50, min_length=2, description='Enter path of the file')):
    
    print(file_path, '....file path...')
    return JSONResponse({'File Path': file_path})


@user_router.post('/users/{keyword}/')
def post_user(*, user: User = Body(..., embed=True), keyword: str, words: List[str] = Query(None)):
    print(user, '...user...', keyword, '....keyword...')
    next_id = max(USERS.keys()) + 1

    USERS.update(
        {
            next_id: user
        }
    )
    return USERS



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
