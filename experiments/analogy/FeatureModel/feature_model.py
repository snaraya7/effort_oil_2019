#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2018, Jianfeng Chen <jchen37@ncsu.edu>, Tianpei Xia <txia4@ncsu.edu>
# vim: set ts=4 sts=4 sw=4 expandtab smartindent:
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.

from __future__ import division, print_function
from FeatureModel.Feature_tree import FeatureTree
import random
import pdb

"""
This module handles the transactions of feature model. All feature model  are formatted as SPLOT xml file,
such as http://52.32.1.180:8080/SPLOT/models/model_20170930_228024571.xml
"""

if __name__ == '__main__':
    # Step 1. Load SPLIT model. Use load_ft_from_url()
    # here url can be www url OR file path

    # url = "http://52.32.1.180:8080/SPLOT/models/model_20170930_228024571.xml"
    url = "./FeatureModel/tree_model.xml"
    ft = FeatureTree()
    ft.load_ft_from_url(url)

    # Step 2. Check feature model information
    print('This model has\n'
          ' {0} constraints\n'
          ' {1} features\n'
          ' {2} depth'.format(
        ft.get_cons_num(),
        ft.get_feature_num(),
        ft.get_tree_height()
    ))

    # Step 3. generate the configurations
    given = {f: random.choice([0, 1]) for f in ft.leaves}
    X = ft.get_full_feature_configure_by_partial_def(given, dict)
    pdb.set_trace()
    print(ft.leaves[0].name)
    # Step 4. checking whether our configuration is correct
    isvalid = ft.check_fulfill_valid(X)
    print("Valid configure? %s" % isvalid)
