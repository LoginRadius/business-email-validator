__title__ = 'business-email-validator'
__author__ = 'Dhruvacube'
__license__ = 'GNU General Public License v2.0'
__copyright__ = 'Copyright 2021-present Login Radius'
__version__ = '1.0.0candidate'
__path__ = __import__('pkgutil').extend_path(__path__, __name__)

# import logging
from typing import NamedTuple, Literal

from .validate_class import *
from .errors import *

class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(major=1, minor=0, micro=0, releaselevel='beta', serial=0)

# logging.getLogger(__name__).addHandler(logging.NullHandler())