# UI自动化测试框架

#### 介绍
基于selenium,python语言的WebUI自动化测试框架


#### 软件结构
- 语言：python
- 自动化框架：selenium
- 设计模式:POM/关键字驱动/数据驱动
- 自动化用例组织框架：pytest
- 自动化报告：allure


#### 设计原则
1.  公共方法为页面提供操作服务
2.  封装细节，对外只提供方法名（或者接口）
3.  断言放在用例
4.  通过return跳转到新页面
5.  页面中重要元素进行PO管理
6.  对相同行为产生不同结果进行封装


#### 安装教程
1.  git@gitee.com:mikb/web_framework.git       拉取代码
2.  pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/      安装依赖库
3.  修改config,setting配置文件,确保driver路径和版本正确
4.  项目根目录执行pytest，默认启动chrome。也可以通过--browser 参数配置启动浏览器。（栗：pytest --browser=ie）


#### 目录结构
```shell
|-- 自动化测试 # 主目录
    ├─config
    │  └─*.ini	# 配置文件
    ├─data
    │  └─test_data.yaml	# 测试数据
    ├─log
    │  └─...x.log	# 日志文件
    ├─drivers       
    │  └─*_driver    # 驱动文件
    ├─imgs
    │  └─...x.png	# 截图文件
    ├─report
    │  ├─tmp                # 报告临时数据
    │  └─report		# allure报告
    ├─page      # 页面资源类
    │  └─*_page.py
    ├─pom               # 业务管理
    │  └─*.py         # 业务类
    ├─testcases        # 用例目录
    │  ├─conftest.py	# 用例依赖对象初始化
    │  └─test_*.py	   # 测试用例
    ├─common
    │  ├─basepage.py	     # 页面操作基类
    │  └─browser.py        # 浏览器初始化
    ├─utils                # 常用工具
    │  ├─clear.py          # 清理工具
    │  ├─logs.py          # 日志工具
    │  ├─mail.py          # 邮件工具
    │  ├─http_client.py   # http请求工具
    │  └─*_*.py           # 其他各种工具
    ├─conftest.py         # 全局依赖初始化
    ├─pytest.ini	   # pytest启动配置文件
    ├─requirements.txt    # 项目依赖库文件
    ├─README.md          # 自述文件
    ├─.gitignore         # git管理文件
    └─setting.py         #项目通用配置文件
```


#### 使用说明
1.  本框架基础已经封装，只需要更改配置文件即可使用,项目配置在setting.py文件，数据库配置邮件配置在config文件
2.  BasePage提供页面基本操作，封装常用操作。如果没有的操作可以在page层或者pom调用driver实现或者封装进BasePage供调用
3.  page层页面为单位，采用枚举封装页面资源(定位，url, 页面断言资源)。采用函数封装页面基本操作和断言操作供上层调用
4.  pom采用类继承basepage类封装跨页面业务逻辑供case层调用，常用业务操作可封装成common类供pom层调用
5.  case层提供driver，测试数据，调用pom完成用例并进行断言操作
6.  本框架使用遵循上述原则，方便后期维护最好相关方法不要乱写
4.  本框架会陆续优化，如果各位有什么建议 欢迎给我留言，会尽力解决~~


#### 实现功能
1.  底层操作方法采用异常处理，log和EC模块封装，提高框架执行效率和稳定性
2.  支持双端运行
3.  log模块采用元素描述，实现快速定位问题
4.  全局共用一个浏览器，提高执行效率
5.  自动生成测试数据
6.  自动清除上次执行的截图以及log
7.  测试失败截图，并加入allure报告
8.  定制美观的allure报告
9.  用例失败重跑
10. 采用通用配置文件，增强框架可维护性
11. 采用yaml文件管理测试数据
12. 采用枚举管理页面资源，方便后期维护
13. 底层方法大多与selenium接口同名或者见名知其意，方便团队其他人使用
14. 支持谷歌，火狐，IE，Safari Edge浏览器以及远程启动

#### 待开发
1.  分布式多线程执行


