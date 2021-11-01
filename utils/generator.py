#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/11
# @Author  : Mik
# 数据类（构造常用数据类型、UUID、文本、词组、文件链接、文件路径）
# 安全类（构造操作系统信息、HASH加密、密码）
# 信息类（构造个人信息数据和表单信息数据：姓名、地址、电话、工作、证件号、
# 银行卡号、公司、邮箱、生日)
# 网络类（构造IP MAC HTTP的客户端类型和文件类型，反反爬）


from faker import Factory


fake = Factory().create('zh_CN')


def random_python_data():
    return fake.pystr(), \
           fake.pyint(), \
           fake.pybool(), \
           fake.pyfloat(), \
           fake.pytuple(nb_elements=2), \
           fake.pylist(nb_elements=2), \
           fake.pydict(nb_elements=2)


def random_uuid():
    return fake.uuid4()


def random_text():
    return fake.text()


def random_word():
    return fake.word(), fake.words()


def random_image_url():
    return fake.image_url()


def random_file_path():
    return fake.file_path()


def random_os_info(os_type: str = 'win'):
    if os_type == 'win':
        return fake.windows_platform_token() + ' ' + fake.linux_processor()
    if os_type == 'linux':
        return fake.linux_processor()
    if os_type == 'mac':
        return fake.mac_platform_token()
    if os_type == 'ios':
        return fake.ios_platform_token()
    if os_type == 'android':
        return fake.android_platform_token()
    return None


def random_hash(raw_output: bool = False):
    return {'md5': fake.md5(raw_output), 'sha1': fake.sha1(raw_output), 'sha256': fake.sha256(raw_output)}


def random_password(length=10, special_chars=False, digits=True, upper_case=False, lower_case=False):
    return fake.password(length=length,
                         special_chars=special_chars,
                         digits=digits,
                         upper_case=upper_case,
                         lower_case=lower_case)


def random_name():
    return fake.name()


def random_address():
    return fake.address()


def random_phone_number():
    return fake.phone_number()


def random_job():
    return fake.job()


def random_ssn(*args):
    return fake.ssn(*args)


def random_credit_card():
    return fake.credit_card_full(), fake.credit_card_number()


def random_company():
    return fake.company()


def random_email(domain):
    return fake.email(domain)


def random_birth(minimum_age=18, maximum_age=25):
    return fake.date_of_birth(minimum_age=minimum_age, maximum_age=maximum_age)


def random_profile():
    return fake.profile()


def random_ip4(private=False, public=False):
    if private:
        return fake.ipv4_private()
    if public:
        return fake.ipv4_public()
    return fake.ipv4()


def random_ip6():
    return fake.ipv6()


def random_mac_address():
    return fake.mac_address()


def random_user_agent():
    return fake.user_agent()


def random_mime_type(mime_type: str = 'application'):
    return fake.mime_type(mime_type)


# print(random_mime_type('image'))
