#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The cat must have slept on the keyboard!!!

Strip this terribly formatted string of its excess characters.
"""


NERVOUS_AS = """




 //////////A long-tailed cat in a room full of rockin' chairs.,,,,,,,,,, 





"""
#2 use strip
NERVOUS_AS = NERVOUS_AS.strip( )

#3 use rstrip() and lstrip()
NERVOUS_AS = NERVOUS_AS.rstrip(",").lstrip("/")

print NERVOUS_AS
