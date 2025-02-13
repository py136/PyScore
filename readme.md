# PyScore

PyScore 是一个基于 Django 的积分管理系统，允许用户添加、删除、查看和申诉积分记录，并进行用户排名。

## 功能

- 用户注册和登录
- 添加积分项目和积分详情
- 删除积分项目和积分详情
- 查看积分历史记录
- 申诉积分记录
- 查看和处理申诉记录
- 用户排名
- OP界面
- 管理后台
- 个人中心

## 文件结构
.
├── .vscode
│   └── launch.json
├── Score
│   ├── add
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── templates/
│   │   │   └── add
│   │   │       ├── 403.html
│   │   │       ├── new_score_topic.html
│   │   │       ├── new_score.html
│   │   │       ├── no_user.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── check
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── templates/
│   │   │   └── check
│   │   │       ├── 403.html
│   │   │       ├── all_details.html
│   │   │       ├── all_score_topics.html
│   │   │       ├── no_user.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── complaint
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── templates/
│   │   │   └── complaint
│   │   │       ├── 403.html
│   │   │       ├── check_complaint_histories.html
│   │   │       ├── check_complaint_his.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── delete
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── templates/
│   │   │   └── delete
│   │   │       ├── 403.html
│   │   │       ├── delete_complaint_histories.html
│   │   │       ├── delete_complaint_histories_user.html
│   │   │       ├── delete_histories.html
│   │   │       ├── delete_score_detail.html
│   │   │       ├── delete_score_topic.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── manage.py
│   ├── op
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── templates/
│   │   │   └── op
│   │   │       ├── 403.html
│   │   │       ├── op_index.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── person
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── templates/
│   │   │   └── person
│   │   │       ├── person_index.html
│   │   │       ├── repair_info.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── ranking
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── templates/
│   │   │   └── ranking
│   │   │       ├── rank.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── Score
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   ├── users
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── templates/
│   │   │   └── users
│   │   │       ├── login.html
│   │   │       ├── register.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── templates/
│   │   ├── 404.html
│   │   ├── 500.html
└── requirements.txt

## 对应URL
 ```
1."users/login/"&"users/register/"    #用户登录/注册
2."users/logout/"       #用户注销
3."score_topics/"       #查看自己的积分项目
4."entry/(topic_id)/"     #查看自己的积分详情
5."complaint_detail/(entry_id)/"     #申诉计分记录
6."complaint/check_complaint_histories_user/"         #查看申诉历史
7."detele/delete_complaint_histories_user/"          #删除申诉历史
8."check_rankings/"                 #查看排名
9."ranking/rank/"                  #对用户进行排名
10."check_histories/"                #查看积分历史
11."detele/delete_histories/"         #删除积分历史
12."person/person/"                #个人中心
13."person/repair_info/"            #修改个人信息
14."op/"                           #OP界面
15."all_score_topics/"           #查看所有用户积分记录
16."add/new_score_topic/"             #添加积分记录
17."detele/delete_score_topic/(topic_id)/"      #删除某条积分记录
18."all_details/(topic_id)/"              #查看该用户积分详情
19."add/new_score/(topic_id)/"            #添加积分详情
20."detele/delete_score_detail/(entry_id)/"      #撤销某条积分详情
21."complaint/complaint_index"                    #申诉主界面
22."complaint/check_complaint_details/"         #查看待审核的申诉
23."complaint/deal_complaint_detail/(entry_id)/"       #处理申诉
24."complaint/check_complaint_histories/"             #查看已申诉的条目
25."detele/delete_complaint_histories/"             #删除已申诉的条目
26."admin/"                                   #Django管理后台
```


## 安装并用开发服务器运行此项目

1. 克隆此仓库：

    ```sh
    git clone https://github.com/py136/PyScore.git
    ```

2. 创建并激活虚拟环境：

    ```sh
    python -m venv venv
    source venv/bin/activate  # 对于 Windows 系统，使用 `venv\Scripts\activate`
    ```

3. 安装依赖：

    ```sh
    pip install -r requirements.txt
    ```

4. 创建数据库：

    ```SQL
    CREATE DATABASE yourdatabase CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    ```

5. 打开Score/settings.py，并按照如下设置：

    ```python
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',#填入你的数据库名称
        'USER' : '',#填入访问用户名
        'PASSWORD' : '',#填入密码
        'HOST' : 'localhost',
        'PORT' : '3306',
        'OPTIONS' : {
            'charset' : 'utf8mb4'
        }
    }
    }
    ```

6. 进行数据库迁移：

    ```sh
    python manage.py migrate
    ```

7. 创建超级用户：

    ```sh
    python manage.py createsuperuser
    ```

8. 启动开发服务器：

    ```sh
    python manage.py runserver
    ```
9. 在 http://127.0.0.1:8000/admin/auth/group/ 中添加以下用户组名，并将超级用户加入到"super_users"用户组中：

    ```
    super_users,document_users,monitor_users
    ```
## 使用

1. 访问 [http://127.0.0.1:8000] 以查看主页。
2. 通过 [http://127.0.0.1:8000/admin] 访问 Django 管理后台。
3. 用户可以注册、登录并管理他们的积分记录。

## 关于用户组

1. 用户组名称及其作用：
    ```
    super_users:超级用户，可以访问所有界面和Django admin
    document_users:计分用户，只能管理用户积分
    monitor_users：监管用户，可以管理用户积分、进行排名以及处理用户申诉，但不能访问Django admin
    ```
2. 将用户加入到特定用户组中：
    需要超级用户通过Django admin手动添加

## 注意
# 此项目仅为DEMO,请勿直接应用于生产环境

## 贡献

欢迎贡献！请 fork 此仓库并提交 pull request。

## 许可证

此项目使用 MIT 许可证。有关更多信息，请参阅 LICENSE 文件。
