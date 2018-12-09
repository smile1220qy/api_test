import unittest
import requests
import json
from lib import db
from lib.test_log import log_case_info
from data import load_data
from conf import config


class TestUserReg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sheet = load_data.get_sheet(config.data_path,"注册")
    def test_user_reg_normal(self):
        #获取用例中需要清理的姓名
        name_cell = self.sheet.cell(1,3).value
        NAME = json.loads(name_cell)['name']
        if db.check_user(NAME):  # 环境准备
            db.del_user(NAME)
        case_data = load_data.get_case(self.sheet,"test_user_reg_normal")
        url = case_data[2]
        try:
            data = json.loads(case_data[3])
            excpeted_res = json.loads(case_data[4])
        except json.decoder.JSONDecodeError as e:
            config.logging.error("用例数据不是合法json")
        res = requests.post(url=url,json=data)
        log_case_info("test_user_reg_normal", url, case_data[3], case_data[4], res.text)
        try:
            res_json = res.json()
        except json.decoder.JSONDecodeError as e:
            config.logging.error("返回结果不是json格式")
        self.assertEqual(excpeted_res,res_json)
        self.assertTrue(db.check_user(NAME))
        db.del_user(NAME)   # 环境清理

    def test_user_reg_use_exist(self):
        data_case = load_data.get_case(self.sheet,"test_user_reg_use_exist")
        url = data_case[2]
        data = json.loads(data_case[3])
        excepted_res = json.loads(data_case[4])
        res = requests.post(url=url, json=data)
        log_case_info("test_user_reg_normal", url, data_case[3], data_case[4], res.text)
        self.assertEqual(excepted_res, res.json())