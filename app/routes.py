from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def test():
    return {'message': 'test'}
