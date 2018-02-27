"""
==============================
Inelastica (:mod:`Inelastica`)
==============================

.. module:: Inelastica

All classes defined in Inelastica.

All classes
===========

.. autosummary::
   :toctree:

   Geom
   SpectralMatrix
   savedData
   step
   SigDir
   SavedSigClass
   ElectrodeSelfEnergy
   GF
   FCrun
   OTSrun
   OSrun
   DynamicalMatrix
   Supercell_DynamicalMatrix
   Symmetry

"""

# Import version string and the major, minor, micro as well
from . import info
from .info import git_revision as __git_revision__
from .info import version as __version__
from .info import major as __major__
from .info import minor as __minor__
from .info import micro as __micro__

__all__ = [s for s in dir() if not s.startswith('_')]
__all__ += ['__{}__'.format(s) for s in ['version', 'major', 'minor', 'micro', 'git_revision']]
