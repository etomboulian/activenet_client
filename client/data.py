from .models.base import Root


class SinglePageResult:
    def __init__(self) -> None:
        pass

class PaginatedResult:
    def __init__(self, api_client, route, first_page: Root, filters: dict, sort: dict = None):
        self.api_client = api_client
        self.api_name = route
        self.filtr = filters
        self.sort = sort
        self.headers = first_page.headers
        self._data = first_page.body
        self.current_page_number = first_page.headers.page_info.page_number
        self.records_per_page = first_page.headers.page_info.total_records_per_page
        self.total_pages = first_page.headers.page_info.total_page

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def next(self):
        if self.current_page_number < self.total_pages:
            self.current_page_number = self.current_page_number + 1
            page_info = {
                "total_records_per_page": self.records_per_page,
                "page_number": self.current_page_number
            }
            next_page = self.api_client.get(self.api_name, url_params=self.params, page_info=page_info, sort=self.sort)
            return PaginatedResult(self.api_client, self.api_name, next_page, filters=self.filters, sort=self.sort)
        else:
            return None

    def __getitem__(self, key):
        return self._data[key]