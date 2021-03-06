#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:Lijiacai
Email:1050518702@qq.com
===========================================
CopyRight@JackLee.com
===========================================
"""

import os
import re
import sys
import json
import graphene
from common.view import BaseApi
from resource.lijiacai.utils import utils
from sql import *
from sql.aggregate import *
from sql.functions import *
from sql.conditionals import *


class TEST(utils.Business, BaseApi, utils.MySQLCrud):
    name = "TEST"
    description = "测试(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # 参数处理，加数据权限参数
        response = self.backend_service()
