import unittest
import requests
import json
from lib import db
from data import load_data
from conf import config
from lib.test_log import log_case_info
from conf import config


class TestUserLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sheet= load_data.get_sheet(config.data_path,"登录")

    @unittest.skipUnless(db.check_user("李元芳"), "跳过该测试用例")
    def test_user_login_normal(self):
        case_data = load_data.get_case(self.sheet,"test_user_login_normal")
        url = case_data[2]
        data = json.loads(case_data[3])
        res = requests.post(url=url, data=data)
        excpted_res = case_data[4]
        log_case_info("test_user_login_normal",url,case_data[3],case_data[4],res.text)
        self.assertEqual(excpted_res,case_data[4])

    def test_user_login_password_wrong(self):
        case_data = load_data.get_case(self.sheet, "test_user_login_password_wrong")
        url = case_data[2]
        data = json.loads(case_data[3])
        res = requests.post(url=url, data=data)
        excpted_res = case_data[4]
        log_case_info("test_user_login_password_wrong", url, case_data[3], case_data[4], res.text)
        self.assertEqual(excpted_res, case_data[4])


if __name__ == "__main__":
    unittest.main(verbosity=2)