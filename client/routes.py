from .models import *

routes = {
    'organization': {
        'api_name': 'GetOrganizations',
        'endpoint': 'organization',
        'return_class': OrganizationList,
        'paginated': False,
        'sortable': False,
        'parameters': None
    },

    'sites': {
        'api_name': 'GetSites',
        'endpoint': 'sites',
        'return_class': SiteList,
        'paginated': False,
        'sortable': False,
        'parameters': None
    },

    'centers': {
        'api_name': 'GetCenters',
        'endpoint': 'centers',
        'return_class': CenterList,
        'paginated': False,
        'sortable': False,
        'parameters': [
                {
                    'show_on_member_app': {
                        'type': str,
                        'required': False,
                        'description': "Filter for centers by their 'Show On the ACTIVE Net Captivate App' flag: Y or N."
                    },
                }
            ]
    },

    'skills': {
        'api_name': 'GetSkills',
        'endpoint': 'skills',
        'return_class': SkillList,
        'paginated': False,
        'sortable': False,
        'parameters': None
    },

    'skip_dates': {
        'api_name': 'GetSkipDates',
        'endpoint': 'skipdates',
        'return_class': SkipDateList,
        'paginated': True,
        'parameters': [
            {
                'facility_id': {
                    'type': int,
                    'required': True
                }
            }
        ],
        'sortable': True,
        'sort_options': [
            {'start_date': ['ASC', 'DESC'] },
            {'start_time': ['ASC', 'DESC'] }
        ]
    },

    'activities': {
        'api_name': 'GetActivities',
        'endpoint': 'activities',
        'return_class': ActivityList
    },
    
    'seasons': {
        'api_name': 'GetSeasons',
        'endpoint': 'seasons',
        'return_class': SeasonList,
        'paginated': False,
        'sortable': False,
    }
}


