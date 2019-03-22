{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Team 3 Project 1\n",
    "\n",
    "Team 3 project is done to uncover patterns in parking activity around the Las Angeles area. We will examine realtionships between vehicle makes and parking citations, vehicle model and parking citation, and vehicle color and parking citations.\n",
    "\n",
    "### Purpose of the Analysis\n",
    "we have three man purposes for the analysis\n",
    "\n",
    "    * The first purpose is to examine if a relatioship exists between vehicle make and parking citations\n",
    "    * The second purpose is to examine if a relatioship exists between vehicle model and parking citations\n",
    "    * The third purpose is to examine if a relatioship exists beteen vehicle color andd parking citations\n",
    "    * The team will examine and plot citation locations to evaluate a possible corilation with the sourding area\n",
    "        * Dining\n",
    "        * Housing\n",
    "        * Bar\n",
    "        * Night club\n",
    "\n",
    "### Key Documents \n",
    "Data sets used throught the project\n",
    "\n",
    "    * a dataset was downloaded from the City of Los Angeles for the months of May through July 2018 in csv format\n",
    "    * a dataset was downloaded from the California DMV in csv format.\n",
    "    * and APi call from citipy is used\n",
    "    * an API call to Google places is used\n",
    "\n",
    "\n",
    "### And coding style \n",
    "Jupyter notebooks will be used\n",
    "\n",
    "```\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import requests\n",
    "import time\n",
    "import pprint\n",
    "from citipy import citipy\n",
    "import gmaps\n",
    "import gmaps.datasets\n",
    "```\n",
    "API Calls\n",
    "* [City of Las Angels](https://data.lacity.org/resource/8yfh-4gug.json)\n",
    "* [Google API](https://developers.google.com/places/web-service/search)\n",
    "\n",
    "Coding Documentation\n",
    "* [gmaps](https://jupyter-gmaps.readthedocs.io/en/latest/tutorial.html)\n",
    "* [Citipy](https://github.com/wingchen/citipy)\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "## Authors\n",
    "\n",
    "* **Ka-Ri Walker* - *Initial work* - [SMU DataTeam](https://github.com/ButtonWalker)\n",
    "* **Sujita Kapali* - *Inital Work* - [SMU DataTeam](https://github.com/SujiKap)\n",
    "* **Sisay Teketele* - *Inital Wark* - [SMU DataTeam](https://github.com/sisayyt)\n",
    "\n",
    "## Acknowledgments\n",
    "\n",
    "* Hat tip to anyone whose code was used\n",
    "* Inspiration\n",
    "* etc\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
