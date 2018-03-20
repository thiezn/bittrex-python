import re
import json
import time

TIMESTAMP_FIELDS = [
    'Created', 'TimeStamp', 'Opened', 'Closed',
    'LastChecked', 'T', 'LastUpdated'
]  # T is used for api v2 candle timestamp...


class Response:
    """Class representing a single response item from Bittrex api"""

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in TIMESTAMP_FIELDS and value is not None:
                try:
                    timestamp = time.mktime(
                        time.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    )
                except ValueError:
                    # Some returns do not have the microsecond
                    timestamp = time.mktime(
                        time.strptime(value, '%Y-%m-%dT%H:%M:%S')
                    )
                except TypeError:
                    # value is None
                    timestamp = value

                setattr(self, self._convert_to_camel(key), timestamp)
            else:
                setattr(self, self._convert_to_camel(key), value)

    def __repr__(self):
        description = f"<Response"

        for key, value in self.__dict__.items():
            description += f" {key}={value}"

        description += ">"
        return description

    @staticmethod
    def _convert_to_camel(name):
        """Converts CamelCase to snake_case"""
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    @classmethod
    def load_from_json(cls, response_type, data):
        """Load Reponse from json data"""

        kwargs = json.loads(data)
        return cls(response_type, kwargs)
