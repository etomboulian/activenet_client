from .base_client import BaseClient

class ApiClient(BaseClient):
    def __init__(self, org_name, api_key, shared_secret):
        super().__init__(org_name=org_name, api_key=api_key, shared_secret=shared_secret)

    # Returns the result of an API call to the GetOrganizations API
    # doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetOrganization
    def GetOrganization(self):
        return self.get('organization')

    # Returns the result of an API call to the GetSites API
    # doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetSites
    def GetSites(self):
        return self.get('sites')

    def GetCenters(self):
        return self.get('centers')

    def GetSkills(self):
        return self.get('skills')

    def GetSkipDates(self, facility_id: int, options: dict = {}):
        options['facility_id'] = facility_id
        return self.get('skip_dates', options=options)

    def GetSeasons(self):
        return self.get('seasons')

    # Returns the result of an API call to the GetActivities API
    # doc link: https://help.aw.active.com/ActiveNet/22.13/en_US/api_specification.htm#GetActivities
    def GetActivities(self, options: dict = None):
        return self.get('activities', options=options)

   
