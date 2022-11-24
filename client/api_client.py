from .base_client import BaseClient
from typing import List, Tuple
from .models import *
from .data import SinglePageResult, PaginatedResult

class ApiClient(BaseClient):
    def __init__(self, org_name, country, api_key, shared_secret):
        super().__init__(
            org_name=org_name, 
            country=country, 
            api_key=api_key, 
            shared_secret=shared_secret
            )

    def GetOrganization(self) -> 'Organization':
        """GetOrganizations API doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetOrganization        
        Params: None
        Returns: Organization - an object representing the organization
        """
        return self.get('organization').body[0]
    
    def GetSites(self) -> List[Site]:
        """GetSites API doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetSites
        Params: None
        Returns: List[Site] - a list of site records
        """
        return self.get('sites').body
    
    def GetCenters(self, options: dict = None) -> List[Center]:
        """GetCenters API doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetCenters
        Params: show_on_member_app: ("Y" | "N"), optional - Filter for centers by their 'Show On the ACTIVE Net Captivate App' flag
        Returns: List[Center] - a list of centers
        """
        return self.get('centers')
    
    def GetSkills(self) -> List[Skill]:
        """GetSkills API doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetSkills
        Params: None
        Returns: List[Skill] - a list of the available skill records
        """
        return self.get('skills')
    
    def GetSkipDates(self, facility_id: int, filters: dict = {}, sort_by: Tuple[str, str] = None) -> 'PaginatedResult':
        """GetSkipDates API doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetSkipDates
        param: facility_id: int, required - The facility id of the facility.
        param: sort_by: Tuple[str, str] - The primary sort option for results, example - ('start_date', 'ASC')
        returns: List[SkipDates] - A list of skip dates
        """
        route = 'skip_dates'
        filters['facility_id'] = facility_id
        
        first_page = self.get(route, filters=filters, sort=sort_by)
        
        return PaginatedResult(self, route, first_page, filters=filters, sort=sort_by) if first_page else first_page
    
    def GetSeasons(self) -> List[Season]:
        """GetSeasons API doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetSeasons
        Params: None
        Returns: List[Season] - a list of season records
        """
        return self.get('seasons').body
    
    def GetActivities(self, options: dict = None, sort_by: dict = None) -> 'PaginatedResult':
        """GetActivities API
        doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetActivities
        Returns: List[Activity] - a list of activity records
        """
        route = 'activities'
        first_page = self.get('activities', filters=options)
        return PaginatedResult(self, route, first_page, filters=options) if first_page else first_page



    
