from ninja.pagination import PaginationBase
from ninja import Field, Schema
from ninja.conf import settings


class CustomPagination(PaginationBase):
    class Input(Schema):
        limit: int = Field(settings.PAGINATION_PER_PAGE, ge=1)
        offset: int = Field(0, ge=0)

    def paginate_queryset(
        self,
        queryset,
        pagination,
        **params,
    ):
        offset = pagination.offset
        if offset > self._items_count(queryset):
            offset = 0
        limit: int = pagination.limit

        return {
            "items": queryset[offset : offset + limit],  # noqa: E203
            "count": self._items_count(queryset),
        }