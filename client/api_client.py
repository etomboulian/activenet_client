from .base_client import BaseClient
from typing import List
from .models.base import Root


class ApiClient(BaseClient):
    def __init__(self, org_name, api_key, shared_secret):
        super().__init__(org_name=org_name, api_key=api_key, shared_secret=shared_secret)

    # Returns the result of an API call to the GetOrganizations API
    # doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetOrganization
    @property
    def GetOrganization(self):
        return ResultItem(self, 'organization')

    # Returns the result of an API call to the GetSites API
    # doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetSites
    @property
    def GetSites(self):
        return ResultItem(self, 'sites')

    # Returns the result of an API call to the GetCenters API
    # doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetCenters
    @property
    def GetCenters(self):
        return ResultItem(self, 'sites')

    # Returns the result of an API call to the GetSkills API
    # doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetSkills
    @property
    def GetSkills(self):
        return ResultItem(self, 'skills')

    # Returns the result of an API call to the GetSkipDates API
    # doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetSkipDates
    def GetSkipDates(self, facility_id: int, options: dict = {}):
        # TODO: Add the ability to add required options automatically
        options['facility_id'] = facility_id
        return ResultItem(self, 'skip_dates', options=options)

    # Returns the result of an API call to the GetSeasons API
    # doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetSeasons
    def GetSeasons(self):
        return self.get('seasons')

    # Returns the result of an API call to the GetActivities API
    # doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetActivities
    def GetActivities(self, options: dict = None):
        return self.get('activities', options=options)

   
class ResultItem:
    def __init__(self, api_client: ApiClient, api_name: str, options: dict = None):
        self.api_client = api_client
        self.api_name = api_name

    def all(self) -> 'Root':
        return self.api_client.get(self.api_name).body