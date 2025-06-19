from typing import Annotated

from fastapi import APIRouter, Path


router = APIRouter(prefix="/items", tags=["Items"])

@router.get("/")
def get_list_item():
    """Возвращает объекты"""

    return ["Item1", "Item2", "Item3"]


@router.get("/latest/")
def get_latest_item():
    """Возвращает последний объект"""

    return {"item": {"id": 0, "name": "latest"}}


@router.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    """Возвращает id объекта"""

    return {
        "item": {
            "id": item_id,
        },
    }
