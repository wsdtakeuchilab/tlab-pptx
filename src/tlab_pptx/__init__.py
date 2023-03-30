__version__ = "0.1.2"

import sys

if sys.version_info >= (3, 10):  # BUG: https://github.com/scanny/python-pptx/issues/762
    import collections.abc

from . import presentation, typing
from .core import Presentation as Presentation
from .core import Slide as Slide
from .core import new_presentation as new_presentation
from .figure import get_date_annotation as get_date_annotation
from .figure import get_default_axis as get_default_axis
from .figure import get_default_layout as get_default_layout
