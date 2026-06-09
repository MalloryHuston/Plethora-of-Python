#!/usr/bin/env python3

import sys
import pygame as pg
from data.main import main
import cProfile

__author__ = "Mallory Huston"

"""
This is an attempt ot recreate the first level of
Super Mario Bros. (1985) for the NES.
"""


if __name__ == "__main__":
    main()
    cProfile.run('main()')
    pg.quit()
    sys.exit()
