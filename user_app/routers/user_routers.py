from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter
from fastapi.responses import JSONResponse

user_router = APIRouter(
    prefix='/users'
)


class User(BaseModel):
    id: int
    name: str
    age: Optional[int] = None
    city: str
    married: bool

USERS = {
    1: {'name': 'danish', 'age': 28, 'city': 'srinagar'},
    2: {'name': 'owais', 'age': 28, 'city': 'srinagar'},
    3: {'name': 'basit', 'age': 28, 'city': 'srinagar'},
    4: {'name': 'qais', 'age': 28, 'city': 'srinagar'},
}

@user_router.get('/')
def get_users():
    return JSONResponse(USERS)


@user_router.get('/{user_id}/')
def get_user(user_id: int):
    return JSONResponse(USERS.get(user_id, {'Error': 'User with this id not found;'}))



if __name__ == '__main__':
    user = User(id=1, name='danish wani', age=28, city='Srinagar', married=False)
    # print(User, '????? User????', dir(User))
    print(User.validate(user))
