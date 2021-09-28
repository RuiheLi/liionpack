r'''
=======
liionpack
=======

liionpack is a tool for simulating battery packs with pybamm. It can design the
pack with a combination of batteries connected in series and parallel or can
read a netlist.
'''
from .simulations import *
from .load_data import *
from .utils import *
from .netlist_utils import *
from .sim_utils import *
from .solver_utils import *
from .protocols import *

__version__ = "0.0.1"
