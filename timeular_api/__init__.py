# coding: utf-8

# flake8: noqa

"""
    Timeular Public API

     Welcome to the documentation of Timeular Public API v2. If you want to have a look at the older and deprecated API v1 please just click on the following link: [Timeular Public API v1](./?v=v1)  You can try all requests here, in documentation, with use of `Try it out` button (available in each endpoint description after folding it out).  Most of endpoints are secured. In order to access them you have to provide *Access Token*. To do so, click on `Authorize` button below and provide `'Bearer *your_access_token*'` as a value for `Authorization` request header. To obtain *Access Token* you have to sign-in with pair of *API Key* and *API Secret* first. API Key & API Secret can be generated on [Profile website](https://profile.timeular.com/#/app/) or, if you have Access Token already, with `POST` request to `/developer/api-access`.  **Warning:** authentication flow may change soon due to active development of Timeular and its API.  If you have any questions, please visit [Support page](http://support.timeular.com) and ask them there.  Happy API browsing!  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from timeular_api.api.authentication_api import AuthenticationApi
from timeular_api.api.integrations_api import IntegrationsApi
from timeular_api.api.time_tracking__activities_api import TimeTrackingActivitiesApi
from timeular_api.api.time_tracking__current_tracking_api import TimeTrackingCurrentTrackingApi
from timeular_api.api.time_tracking__devices_api import TimeTrackingDevicesApi
from timeular_api.api.time_tracking__reports_api import TimeTrackingReportsApi
from timeular_api.api.time_tracking__tags__mentions_api import TimeTrackingTagsMentionsApi
from timeular_api.api.time_tracking__time_entries_api import TimeTrackingTimeEntriesApi

# import ApiClient
from timeular_api.api_client import ApiClient
from timeular_api.configuration import Configuration
# import models into sdk package
from timeular_api.models.activities_configuration_response import ActivitiesConfigurationResponse
from timeular_api.models.activity_configuration_response import ActivityConfigurationResponse
from timeular_api.models.activity_creation_request import ActivityCreationRequest
from timeular_api.models.activity_edition_request import ActivityEditionRequest
from timeular_api.models.archived_activities_response import ArchivedActivitiesResponse
from timeular_api.models.archived_activity_response import ArchivedActivityResponse
from timeular_api.models.current_tracking_response import CurrentTrackingResponse
from timeular_api.models.developer_api_access_response import DeveloperApiAccessResponse
from timeular_api.models.developer_full_api_access_response import DeveloperFullApiAccessResponse
from timeular_api.models.developer_sign_in_request import DeveloperSignInRequest
from timeular_api.models.developer_sign_in_response import DeveloperSignInResponse
from timeular_api.models.device_edition_request import DeviceEditionRequest
from timeular_api.models.device_response import DeviceResponse
from timeular_api.models.devices_response import DevicesResponse
from timeular_api.models.edit_tracking_request import EditTrackingRequest
from timeular_api.models.edit_tracking_response import EditTrackingResponse
from timeular_api.models.error_response import ErrorResponse
from timeular_api.models.integrations_response import IntegrationsResponse
from timeular_api.models.mention_response import MentionResponse
from timeular_api.models.note import Note
from timeular_api.models.note_mention import NoteMention
from timeular_api.models.note_tag import NoteTag
from timeular_api.models.start_tracking_request import StartTrackingRequest
from timeular_api.models.started_tracking_response import StartedTrackingResponse
from timeular_api.models.stop_tracking_request import StopTrackingRequest
from timeular_api.models.stopped_tracking_response import StoppedTrackingResponse
from timeular_api.models.success_with_ignored_errors_response import SuccessWithIgnoredErrorsResponse
from timeular_api.models.tag_response import TagResponse
from timeular_api.models.tags_and_mentions_response import TagsAndMentionsResponse
from timeular_api.models.time_entries_response import TimeEntriesResponse
from timeular_api.models.time_entry_activity_response import TimeEntryActivityResponse
from timeular_api.models.time_entry_creation_request import TimeEntryCreationRequest
from timeular_api.models.time_entry_duration_response import TimeEntryDurationResponse
from timeular_api.models.time_entry_edition_request import TimeEntryEditionRequest
from timeular_api.models.time_entry_response import TimeEntryResponse
from timeular_api.models.tracking_activity_response import TrackingActivityResponse
from timeular_api.models.tracking_response import TrackingResponse
