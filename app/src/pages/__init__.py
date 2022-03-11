from collections import OrderedDict

from .business_understanding import Business_understanding
from .data_preparation import Data_preparation
from .data_understanding import Data_understanding
from .modeling import Modeling
from .evaluation import Evaluation
from .deployment_prototype import Deployment_prototype


PAGE_MAP = OrderedDict({
    'Business Understanding': Business_understanding,
    'Data Understanding': Data_understanding,
    'Data Preparation': Data_preparation,
    'Modeling': Modeling,
    'Evaluation': Evaluation,
    'Deployment Prototype': Deployment_prototype
})

__all__ = ['PAGE_MAP']