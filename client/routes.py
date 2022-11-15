from .models import *

routes = {
    'organization': {
        'api_name': 'GetOrganizations',
        'endpoint': 'organization',
        'details': {
            'return_class': Organization,
            'paginated': False,
            'sortable': False,
            'parameters': None
        }
    },
    'sites': {
        'api_name': 'GetSites',
        'endpoint': 'sites',
        'details': {
            'return_class': Sites,
            'paginated': False,
            'sortable': False,
            'parameters': None
        }
    },
    'centers': {
        'api_name': 'GetCenters',
        'endpoint': 'centers',
        'details': {
            'return_class': Centers,
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
        }
    },
    'skills': {
        'api_name': 'GetSkills',
        'endpoint': 'skills',
        'details': {
            'return_class': Skills,
            'paginated': False,
            'sortable': False,
            'parameters': None
        }
    },
    'skip_dates': {
        'api_name': 'GetSkipDates',
        'endpoint': 'skipdates',
        'details': {
            'return_class': SkipDates,
            'paginated': True,
            'sortable': True,
            'parameters': [
                {
                    'facility_id': {
                        'type': int,
                        'required': True
                    }
                }
            ],
            'sort_options': [
                {'start_date': ['ASC', 'DESC'] },
                {'start_time': ['ASC', 'DESC'] }
            ]

        }
    },
    'activities': {
        'api_name': 'GetActivities',
        'endpoint': 'activities',
        'return_class': Activities
    },
    'seasons': {
        'api_name': 'GetSeasons',
        'endpoint': 'seasons',
        'details': {
            'return_class': Seasons,
            'paginated': False,
            'sortable': False,
        }
    }
}


