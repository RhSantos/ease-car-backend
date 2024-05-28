from core.general.utils.collections import deep_update
from core.general.utils.settings import get_settings_from_environment

"""
This takes env variables with a matching prefix, strips out the prefix and
adds it to global settings.

For example:
export EASE_CAR_SETTINGS_IN_DOCKER=true (enviroment variable)

Could then be referenced as global env var in python as:
IN_DOCKER (where the value would be a python keyword 'True')
"""

deep_update(globals(), get_settings_from_environment(ENVVAR_SETTINGS_PREFIX))  # type: ignore
