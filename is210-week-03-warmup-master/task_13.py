#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Imports values from task 13 to test equality.

.. hint::

    You can access task_12 data in the following example type:

.. code:: python

    print task_12.FLOATVAL
"""

import task_12

#from task_12 import DECVAL, FLOATVAL <= I did this before reading hint, would it loose points?
    
FRAC_DEC_EQUAL = task_12.DECVAL == task_12.FLOATVAL
print FRAC_DEC_EQUAL
DEC_FLOAT_INEQUAL = task_12.DECVAL != task_12.FLOATVAL
print DEC_FLOAT_INEQUAL

