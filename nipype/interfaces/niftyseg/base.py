# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:

"""
The niftyseg module provides classes for interfacing with `niftyseg
<https://sourceforge.net/projects/niftyseg/>`_ command line tools.
These are the base tools for working with niftyseg.
EM Statistical Segmentation tool is found in niftyseg/em.py
Fill lesions tool is found in niftyseg/lesions.py
Mathematical operation tool is found in niftyseg/maths.py
Patch Match tool is found in niftyseg/patchmatch.py
Statistical operation tool is found in niftyseg/stats.py
Label Fusion and CalcTopNcc tools are in niftyseg/steps.py
Examples
--------
See the docstrings of the individual classes for examples.
"""

from nipype.interfaces.niftyreg.base import no_nifty_package
from nipype.interfaces.niftyfit.base import NiftyFitCommand
import subprocess
import warnings


warn = warnings.warn
warnings.filterwarnings('always', category=UserWarning)


class NiftySegCommand(NiftyFitCommand):
    """
    Base support interface for NiftySeg commands.
    """
    _suffix = '_ns'
    _min_version = None

    def __init__(self, **inputs):
        super(NiftySegCommand, self).__init__(**inputs)

    def get_version(self):
        if no_nifty_package(cmd=self.cmd):
            return None
        # exec_cmd = ''.join((self.cmd, ' --version'))
        exec_cmd = 'seg_EM --version'
        # Using seg_EM for version (E.G: seg_stats --version doesn't work)
        return subprocess.check_output(exec_cmd, shell=True).strip('\n')
