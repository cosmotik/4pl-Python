from fastapi import APIRouter

from repository import main_repository as repo

router = APIRouter(
    prefix="/api/main",
    tags=['Main']
)


@router.get('')
def root():
    return repo.root()
