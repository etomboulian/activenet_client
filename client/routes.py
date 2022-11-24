from .models import (
    OrganizationResponse,
    SitesResponse,
    CentersResponse,
    SeasonsResponse,
    SkillsResponse,
    SkipDatesResponse,
    ActivitiesResponse
)

routes = {
    'organization': {
        'api_name': 'GetOrganizations',
        'endpoint': 'organization',
        'return_class': OrganizationResponse,
        'paginated': False,
        'sortable': False,
        'parameters': None
    },

    'sites': {
        'api_name': 'GetSites',
        'endpoint': 'sites',
        'return_class': SitesResponse,
        'paginated': False,
        'sortable': False,
        'parameters': None
    },

    'centers': {
        'api_name': 'GetCenters',
        'endpoint': 'centers',
        'return_class': CentersResponse,
        'paginated': False,
        'sortable': False,
        'optional_parameters': [
                {
                    'show_on_member_app': {
                        'type': str,
                        'valid_options': ['Y', 'N'],
                        'description': "Filter for centers by their 'Show On the ACTIVE Net Captivate App' flag: Y or N."
                    },
                }
            ]
    },

    'skills': {
        'api_name': 'GetSkills',
        'endpoint': 'skills',
        'return_class': SkillsResponse,
        'paginated': False,
        'sortable': False,
        'parameters': None
    },

    'skip_dates': {
        'api_name': 'GetSkipDates',
        'endpoint': 'skipdates',
        'return_class': SkipDatesResponse,
        'paginated': True,
        'required_parameters':{
            'facility_id': {
                'type': int,
            }        
        },
        'optional_parameters': {

        },
        'sortable': True,
        'sort_options': {
            'start_date': ['ASC', 'DESC'],
            'start_time': ['ASC', 'DESC'] 
        }
    },

    'activities': {
        'api_name': 'GetActivities',
        'endpoint': 'activities',
        'return_class': ActivitiesResponse,
        'paginated': True,
        'required_parameters': {
        },
        'optional_parameters': {
            'activity_name': {'type': str},
            'activity_number': {'type': int},
            'activity_type_id': {'type': int},
            'parent_season_id': {'type': int},
            'activity_status_id': {'type': int},
            'category_id': {'type': int},
            'other_category_id': {'type': int},
            'site_ids': {'type': str},
            'center_ids': {'type': str},
        },
        'sortable': True,
        'sort_options': [

        ]
    },

    'seasons': {
        'api_name': 'GetSeasons',
        'endpoint': 'seasons',
        'return_class': SeasonsResponse,
        'paginated': False,
        'sortable': False,
    }
}
