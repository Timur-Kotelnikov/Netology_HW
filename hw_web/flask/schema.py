from pydantic import BaseModel, ValidationError
from errors import HttpError


class CreateAdv(BaseModel):
    title: str
    text: str


def validate_create_ad(json_data):
    try:
        adv_schema = CreateAdv(**json_data)
        return adv_schema.dict()
    except ValidationError as er:
        raise HttpError(status_code=400, message=er.errors())
