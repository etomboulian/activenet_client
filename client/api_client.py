from .base_client import BaseClient
from typing import List
from .models import *


class ApiClient(BaseClient):
    def __init__(self, org_name, api_key, shared_secret):
        super().__init__(org_name=org_name, api_key=api_key, shared_secret=shared_secret)


    def GetOrganization(self) -> 'Organization':
        '''
        GetOrganizations API 
        doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetOrganization        

        Returns:
            an object representing the organization
        '''
        return self.get('organization').body[0]

    
    def GetSites(self) -> List[Site]:
        '''
        GetSites API 
        doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetSites

        Returns:
            a list of site records
        '''
        return self.get('sites').body

    
    def GetCenters(self) -> List[Center]:
        '''
        GetCenters API 
        doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetCenters

        Returns:
            a list of centers
        '''
        return self.get('centers').body

    
    def GetSkills(self) -> List[Skill]:
        '''
        GetSkills API 
        doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetSkills
        
        Returns:
            a list of the available skill records
        '''
        return self.get('skills').body

    
    def GetSkipDates(self, facility_id: int, options: dict = {}):
        '''
        GetSkipDates API 
        doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetSkipDates
        
        Returns:
            a list of skip date records
        '''
        # TODO: Add the ability to add required options automatically
        options['facility_id'] = facility_id
        return self.get('skip_dates', options=options).body

    
    def GetSeasons(self):
        '''
        GetSeasons API 
        doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetSeasons

        Returns:
            a list of season records
        '''
        return self.get('seasons')

    
    def GetActivities(self, options: dict = None):
        '''
        GetActivities API
        doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetActivities

        Returns:
            a list of activity records
        '''
        return self.get('activities', options=options)

