#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""assign some simple numeric types"""
import decimal
import fractions
INTVAL = 1
FLOATVAL = 0.1
DECVAL = decimal.Decimal('0.1')
FRACVAL =fractions.Fraction(1,10)

print FLOATVAL
print DECVAL
print FRACVAL
