# -*- coding: utf-8 -*-

__all__ = ["corner", "hist2d", "quantile"]

from .corner import corner, hist2d, quantile
from .corner_version import __version__  # noqa

__author__ = "Dan Foreman-Mackey"
__email__ = "foreman.mackey@gmail.com"
__uri__ = "https://corner.readthedocs.io"
__description__ = "Make some beautiful corner plots"
__copyright__ = "Copyright 2013-2020 Daniel Foreman-Mackey and contributors"
__contributors__ = [
    # Alphabetical by first name.
    "Adrian Price-Whelan @adrn",
    "Brendon Brewer @eggplantbren",
    "Brigitta Sipocz @bsipocz",
    "Ekta Patel @ekta1224",
    "Emily Rice @emilurice",
    "Geoff Ryan @geoffryan",
    "Guillaume @ceyzeriat",
    "Gregory Ashton @ga7g08",
    "Hanno Rein @hannorein",
    "Jeremy Heyl @jsheyl",
    "Kelle Cruz @kelle",
    "Kyle Barbary @kbarbary",
    "Marco Tazzari @mtazzari",
    "Matt Pitkin @mattpitkin",
    "Phil Marshall @drphilmarshall",
    "Pierre Gratier @pirg",
    "Stephan Hoyer @shoyer",
    "Víctor Zabalza @zblz",
    "Will Vousden @willvousden",
    "Wolfgang Kerzendorf @wkerzendorf",
]
__bibtex__ = __citation__ = """
@article{corner,
  doi = {10.21105/joss.00024},
  url = {https://doi.org/10.21105/joss.00024},
  year  = {2016},
  month = {jun},
  publisher = {The Open Journal},
  volume = {1},
  number = {2},
  pages = {24},
  author = {Daniel Foreman-Mackey},
  title = {corner.py: Scatterplot matrices in Python},
  journal = {The Journal of Open Source Software}
}
"""
