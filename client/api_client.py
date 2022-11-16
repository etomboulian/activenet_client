from .base_client import BaseClient
from typing import List, Tuple
from .models import *


class ApiClient(BaseClient):
    def __init__(self, org_name, api_key, shared_secret):
        super().__init__(org_name=org_name, api_key=api_key, shared_secret=shared_secret)


    def GetOrganization(self) -> 'Organization':
        """GetOrganizations API 
        doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetOrganization        

        Params: None

        Returns:
            an object representing the organization
        """
        return self.get('organization').body[0]

    
    def GetSites(self) -> List[Site]:
        """GetSites API 
        doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetSites

        Params: None

        Returns:
            a list of site records
        """
        return self.get('sites').body

    
    def GetCenters(self, options: dict = None) -> List[Center]:
        """GetCenters API 
        doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetCenters

        Params:
            show_on_member_app: ("Y" | "N"), optional 
                Filter for centers by their 'Show On the ACTIVE Net Captivate App' flag
        Returns:
            a list of centers
        """
        return self.get('centers').body

    
    def GetSkills(self) -> List[Skill]:
        """GetSkills API 
        doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetSkills
        
        Params: None

        Returns:
            a list of the available skill records
        """
        return self.get('skills').body

    
    def GetSkipDates(self, facility_id: int, 
        additional_params: dict = {}, 
        sort_by: Tuple[str, str] = None) -> List[SkipDate]:
        """GetSkipDates API (Paginated)
        doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetSkipDates
        
        Params:
            facility_id: int, required 
                The facility id of the facility.

            sort: Tuple[str, str], optional
                The primary sort option for results, example - ('start_date', 'ASC')

        Returns:
            a list of skip date records
        """
        route = 'skip_dates'
        additional_params['facility_id'] = facility_id

        if not self.validate_required_params(route, additional_params):
            raise Exception('Not all required parameters were included')
        
        return PaginatedResult(self.get(route, options=additional_params, sort=sort_by))

    
    def GetSeasons(self) -> List[Season]:
        """GetSeasons API 
        doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetSeasons

        Params: None

        Returns:
            a list of season records
        """
        return self.get('seasons').body

    
    def GetActivities(self, options: dict = None):
        """GetActivities API
        doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetActivities

        Returns:
            a list of activity records
        """
        return self.get('activities', options=options).body


class PaginatedResult:
    pass