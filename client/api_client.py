from .base_client import BaseClient
from typing import List, Tuple
from .models import *
from .models.base import Root


class ApiClient(BaseClient):
    def __init__(self, org_name, api_key, shared_secret):
        super().__init__(org_name=org_name, api_key=api_key, shared_secret=shared_secret)

    def GetOrganization(self) -> 'Organization':
        """GetOrganizations API 
        doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetOrganization        

        Params: None
        Returns: Organization - an object representing the organization
        """
        return self.get('organization').body[0]
    
    def GetSites(self) -> List[Site]:
        """GetSites API 
        doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetSites
        
        Params: None
        Returns: List[Site] - a list of site records
        """
        return self.get('sites').body
    
    def GetCenters(self, options: dict = None) -> List[Center]:
        """GetCenters API 
        doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetCenters

        Params: show_on_member_app: ("Y" | "N"), optional - Filter for centers by their 'Show On the ACTIVE Net Captivate App' flag
        Returns: List[Center] - a list of centers
        """
        return self.get('centers').body
    
    def GetSkills(self) -> List[Skill]:
        """GetSkills API 
        doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetSkills
        
        Params: None

        Returns: List[Skill] - a list of the available skill records
        """
        return self.get('skills').body
    
    def GetSkipDates(self, facility_id: int, filters: dict = {}, sort_by: Tuple[str, str] = None) -> List[SkipDate]:
        """GetSkipDates API
        doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetSkipDates
        
        Paginated, Sortable

        param: facility_id: int, required - The facility id of the facility.
        sort: Tuple[str, str], optional - The primary sort option for results, example - ('start_date', 'ASC')
        returns: List[SkipDates] - A list of skip dates
        """
        route = 'skip_dates'
        filters['facility_id'] = facility_id
        
        first_page = self.get(route, filters=filters, sort=sort_by)
        
        return PaginatedResult(self, route, first_page, filters=filters, sort=sort_by) if first_page else first_page
    
    def GetSeasons(self) -> List[Season]:
        """GetSeasons API 
        doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetSeasons

        Params: None
        Returns: List[Season] - a list of season records
        """
        return self.get('seasons').body
    
    def GetActivities(self, options: dict = None):
        """GetActivities API
        doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetActivities

        Paginated, Sortable

        Returns: List[Activity] - a list of activity records
        """
        route = 'activities'
        first_page = self.get('activities', filters=options)
        return PaginatedResult(self, route, first_page, filters=options) if first_page else first_page


class PaginatedResult:
    def __init__(self, api_client: ApiClient, route, first_page: Root, filters: dict, sort: dict = None):
        self.api_client = api_client
        self.api_name = route
        self.filtr = filters
        self.sort = sort
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
    
