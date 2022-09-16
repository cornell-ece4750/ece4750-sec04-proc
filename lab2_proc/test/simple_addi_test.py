#=========================================================================
# ProcSimple_addi_test.py
#=========================================================================

import pytest
import random

from pymtl3 import *
from .harness import *
from lab2_proc.ProcSimple import ProcSimple

#-------------------------------------------------------------------------
# test_addi
#-------------------------------------------------------------------------

def test_addi( cmdline_opts ):

  prog="""
    # write your test case here!
    csrr x1, mngr2proc, < 5
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    addi x3, x1, 0x0004
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    csrw proc2mngr, x3 > 9
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
  """

  run_test( ProcSimple, prog, cmdline_opts=cmdline_opts )

