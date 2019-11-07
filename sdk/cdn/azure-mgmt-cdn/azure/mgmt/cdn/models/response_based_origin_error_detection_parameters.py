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


class ResponseBasedOriginErrorDetectionParameters(Model):
    """The JSON object that contains the properties to determine origin health
    using real requests/responses.

    :param response_based_detected_error_types: Type of response errors for
     real user requests for which origin will be deemed unhealthy. Possible
     values include: 'None', 'TcpErrorsOnly', 'TcpAndHttpErrors'
    :type response_based_detected_error_types: str or
     ~azure.mgmt.cdn.models.ResponseBasedDetectedErrorTypes
    :param response_based_failover_threshold_percentage: The percentage of
     failed requests in the sample where failover should trigger.
    :type response_based_failover_threshold_percentage: int
    :param http_error_ranges: The list of Http status code ranges that are
     considered as server errors for origin and it is marked as unhealthy.
    :type http_error_ranges:
     list[~azure.mgmt.cdn.models.HttpErrorRangeParameters]
    """

    _validation = {
        'response_based_failover_threshold_percentage': {'maximum': 100, 'minimum': 0},
    }

    _attribute_map = {
        'response_based_detected_error_types': {'key': 'responseBasedDetectedErrorTypes', 'type': 'ResponseBasedDetectedErrorTypes'},
        'response_based_failover_threshold_percentage': {'key': 'responseBasedFailoverThresholdPercentage', 'type': 'int'},
        'http_error_ranges': {'key': 'httpErrorRanges', 'type': '[HttpErrorRangeParameters]'},
    }

    def __init__(self, **kwargs):
        super(ResponseBasedOriginErrorDetectionParameters, self).__init__(**kwargs)
        self.response_based_detected_error_types = kwargs.get('response_based_detected_error_types', None)
        self.response_based_failover_threshold_percentage = kwargs.get('response_based_failover_threshold_percentage', None)
        self.http_error_ranges = kwargs.get('http_error_ranges', None)
