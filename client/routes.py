from .models import (
    OrganizationResponse,
    SitesResponse,
    CentersResponse,
    SeasonList,
    SkillList,
    SkipDateList,
    ActivityList
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
        'parameters': [
                {
                    'show_on_member_app': {
                        'type': str,
                        'valid_options': ['Y', 'N'],
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
        'parameters':
            {
                'facility_id': {
                    'type': int,
                    'required': True
                }
                
            }
        ,
        'sortable': True,
        'sort_options': [
            {'start_date': ['ASC', 'DESC'] },
            {'start_time': ['ASC', 'DESC'] }
        ]
    },

    'activities': {
        'api_name': 'GetActivities',
        'endpoint': 'activities',
        'return_class': ActivityList,
        'paginated': True,
        'parameters': {
            'activity_name': {
                'type': str,
                'required': False
            },

            'activity_number': {
                'type': int,
                'required': False
            },

            'activity_type_id': {
                'type': int,
                'required': False
            },

            'parent_season_id': {
                'type': int,
                'required': False
            },

            'activity_status_id': {
                'type': int,
                'required': False
            },

            'category_id': {
                'type': int,
                'required': False
            },

            'other_category_id': {
                'type': int,
                'required': False
            },

            'site_ids': {
                'type': str,
                'required': False
            },

            'center_ids': {
                'type': str,
                'required': False
            },

            


        },
        'sortable': True,
        'sort_options': [

        ]
    },

    'seasons': {
        'api_name': 'GetSeasons',
        'endpoint': 'seasons',
        'return_class': SeasonList,
        'paginated': False,
        'sortable': False,
    }
}
