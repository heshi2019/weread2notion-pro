import hashlib
import json
import re
import os
import requests
from requests.utils import cookiejar_from_dict
from retrying import retry


Flyme_URL = "https://cloud.flyme.cn/"
# 分类请求，post，无载荷
Flyme_fellei_URL = "https://notes.flyme.cn/c/browser/note/gettags"

# 数据请求，post，载荷start=0&length=1000&groupUuid=-1
Flyme_data_URL = "https://notes.flyme.cn/c/browser/note/getnotegroups?start=0&length=1000&groupUuid=-1"



class FlymeApi:
    pass
    cookie = "lang=zh_CN; DSESSIONID=84606f70-442c-472e-aefe-6cff8fc3832d; _islogin=true; _uid=114155673; _keyLogin=86a80de50f5f1a0b88d091a784f204; _rmtk=e44242fb8e83ae40314485c3635351; _uticket=sz_25c46cf72cc26e534b3c2abe0f3fc8bd; _ckk=sz_9ca3c423c0095d7edf3190233ccb13c3; _cct=313734bfdb2996efbc18d9a57d; JSESSIONID=node012jttrdwh5emu1go0tbmimih591594368.node0"
