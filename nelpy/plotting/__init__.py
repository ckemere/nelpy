<<<<<<< HEAD
"""
nelpy.plotting
=====

This is the nelpy plotting module.
"""

# from ..objects import (EventArray,
#                        EpochArray,
#                        AnalogSignal,
#                        AnalogSignalArray,
#                        SpikeTrain,
#                        SpikeTrainArray,
#                        BinnedSpikeTrain,
#                        BinnedSpikeTrainArray)

from .core import (plot,
                   comboplot,
                   raster,
                   matshow,
                   overviewstrip,
                   epoch_plot)

from .scalebar import add_scalebar

=======
"""
nelpy.plotting
=====

This is the nelpy plotting module.
"""

# from ..objects import (EventArray,
#                        EpochArray,
#                        AnalogSignal,
#                        AnalogSignalArray,
#                        SpikeTrain,
#                        SpikeTrainArray,
#                        BinnedSpikeTrain,
#                        BinnedSpikeTrainArray)

from .core import (plot,
                   comboplot,
                   raster,
                   matshow,
                   overviewstrip,
                   epoch_plot)

from .scalebar import add_scalebar

>>>>>>> feature/plotting
__version__ = '0.0.2'  # should I maintain a separate version for this?