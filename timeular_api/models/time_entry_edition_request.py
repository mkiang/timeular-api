# coding: utf-8

"""
    Timeular Public API

     Welcome to the documentation of Timeular Public API v2. If you want to have a look at the older and deprecated API v1 please just click on the following link: [Timeular Public API v1](./?v=v1)  You can try all requests here, in documentation, with use of `Try it out` button (available in each endpoint description after folding it out).  Most of endpoints are secured. In order to access them you have to provide *Access Token*. To do so, click on `Authorize` button below and provide `'Bearer *your_access_token*'` as a value for `Authorization` request header. To obtain *Access Token* you have to sign-in with pair of *API Key* and *API Secret* first. API Key & API Secret can be generated on [Profile website](https://profile.timeular.com/#/app/) or, if you have Access Token already, with `POST` request to `/developer/api-access`.  **Warning:** authentication flow may change soon due to active development of Timeular and its API.  If you have any questions, please visit [Support page](http://support.timeular.com) and ask them there.  Happy API browsing!  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from timeular_api.models.note import Note  # noqa: F401,E501


class TimeEntryEditionRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'activity_id': 'str',
        'started_at': 'str',
        'stopped_at': 'str',
        'note': 'Note'
    }

    attribute_map = {
        'activity_id': 'activityId',
        'started_at': 'startedAt',
        'stopped_at': 'stoppedAt',
        'note': 'note'
    }

    def __init__(self, activity_id=None, started_at=None, stopped_at=None, note=None):  # noqa: E501
        """TimeEntryEditionRequest - a model defined in Swagger"""  # noqa: E501

        self._activity_id = None
        self._started_at = None
        self._stopped_at = None
        self._note = None
        self.discriminator = None

        if activity_id is not None:
            self.activity_id = activity_id
        if started_at is not None:
            self.started_at = started_at
        if stopped_at is not None:
            self.stopped_at = stopped_at
        if note is not None:
            self.note = note

    @property
    def activity_id(self):
        """Gets the activity_id of this TimeEntryEditionRequest.  # noqa: E501


        :return: The activity_id of this TimeEntryEditionRequest.  # noqa: E501
        :rtype: str
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """Sets the activity_id of this TimeEntryEditionRequest.


        :param activity_id: The activity_id of this TimeEntryEditionRequest.  # noqa: E501
        :type: str
        """

        self._activity_id = activity_id

    @property
    def started_at(self):
        """Gets the started_at of this TimeEntryEditionRequest.  # noqa: E501


        :return: The started_at of this TimeEntryEditionRequest.  # noqa: E501
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this TimeEntryEditionRequest.


        :param started_at: The started_at of this TimeEntryEditionRequest.  # noqa: E501
        :type: str
        """

        self._started_at = started_at

    @property
    def stopped_at(self):
        """Gets the stopped_at of this TimeEntryEditionRequest.  # noqa: E501


        :return: The stopped_at of this TimeEntryEditionRequest.  # noqa: E501
        :rtype: str
        """
        return self._stopped_at

    @stopped_at.setter
    def stopped_at(self, stopped_at):
        """Sets the stopped_at of this TimeEntryEditionRequest.


        :param stopped_at: The stopped_at of this TimeEntryEditionRequest.  # noqa: E501
        :type: str
        """

        self._stopped_at = stopped_at

    @property
    def note(self):
        """Gets the note of this TimeEntryEditionRequest.  # noqa: E501


        :return: The note of this TimeEntryEditionRequest.  # noqa: E501
        :rtype: Note
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this TimeEntryEditionRequest.


        :param note: The note of this TimeEntryEditionRequest.  # noqa: E501
        :type: Note
        """

        self._note = note

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TimeEntryEditionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other