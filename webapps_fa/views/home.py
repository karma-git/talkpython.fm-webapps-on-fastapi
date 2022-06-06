import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()


@router.get('/')
@template()
def index(user: str = 'unknown'):
    return {
        'user_name': user,
    }


@router.get('/about')
def about():
    return {}