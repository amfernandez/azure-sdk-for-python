# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class HttpErrorRangeParameters(Model):
    """The JSON object that represents the range for http status codes.

    :param begin: The inclusive start of the http status code range.
    :type begin: int
    :param end: The inclusive end of the http status code range.
    :type end: int
    """

    _validation = {
        'begin': {'maximum': 999, 'minimum': 100},
        'end': {'maximum': 999, 'minimum': 100},
    }

    _attribute_map = {
        'begin': {'key': 'begin', 'type': 'int'},
        'end': {'key': 'end', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(HttpErrorRangeParameters, self).__init__(**kwargs)
        self.begin = kwargs.get('begin', None)
        self.end = kwargs.get('end', None)
