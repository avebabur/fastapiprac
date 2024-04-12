from fastapi import APIRouter, status, Response, Depends
from enum import Enum
from typing import Optional
from router.blog_post import required_functionality


router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


@router.get(
        '/all',
        summary='retrieve all blogs',
        description='this api call simulates fetching all blogs.',
        response_description='list of available blogs'
        )
def get_all_blogs(page = 1, page_size: Optional[int] = None, req_parameter: dict = Depends(required_functionality)):
    return {'mgs': f'All the {page_size} blogs on page {page}', 'req': req_parameter}

@router.get(
        '/{id}/comments/{comment_id}',
        tags=['comment']
        )
def get_comment(id: int, comment_id: int, valid: bool=True, username: Optional[str]=None):
    """
    Simulates retrieving a comment of a blog
    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **valid** optional query parameter
    - **username** optional query parameter
    """
    return{'msg': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@router.get(
        '/type/{type}',
         )
def get_blog_type(type: BlogType):
    return {'msg': f'Blog type {type}'}

@router.get(
        '/{id}',
        status_code=status.HTTP_200_OK,
        )
def index2(id: int, response: Response):
    if id < 10:
        response.status_code = status.HTTP_200_OK
        return {'msg': f'Page with the number {id}'}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Page with the number {id} not found'}
