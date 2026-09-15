# PyScore 1.1

PyScore 是一个基于 Django 的积分管理系统，允许用户添加、删除、查看和申诉积分记录，并进行用户排名。

## 更新了什么
1. 重写项目所有代码，使代码更符合编程习惯，提高运行效率
2. 添加用户管理功能，管理员可以修改用户信息和对应用户组
3. 更改排名系统逻辑，让系统每五分钟进行一次排名（AI实现）
4. 新增排名API，让用户可以实时查看自己的排名（AI实现）
5. 用户查看自己的积分条目时，可以查看自己的总分
6. 删除“历史记录”功能
7. 在op下新增authority.py，专门负责检查用户权限和发送403界面
8. 细化用户组，删除document_user和monitor_user，新增ordinary，作为普通用户组
9. 为用户积分数据设置索引，提高排名效率（AI实现）
10. 改良查看用户积分和排名界面
11. 设置权限，防止用户自行进行申诉批准、添加积分和修改用户组

## 功能

- 用户注册和登录
- 为单个用户添加或删除积分项目
- 用户管理界面
- 查看和处理申诉记录
- 用户排名
- OP界面
- 管理后台
- 个人中心


## 对应URL
 ```
1."users/login/"&"users/register/"    #用户登录/注册
2."users/logout/"       #用户注销
3."entry/"               #查看积分
4."users/"                #查看所有用户
5."details/(user_name)/"       #查看用户积分情况
6."add_score/"        #添加用户积分
7."complaints/"             #查看用户申诉
8."complain_details/(entry_id)/"        #对积分进行申诉
9."deal_complaint/(complaint_id)/"        #处理申诉
10."delete_sccore/(entry_id)"          #撤销积分
11.."user_info/(user_name)/"        #查看用户信息（op界面）
12.."op/"            #op主页
13."user_admin/"          #用户管理
14."repair_user/"           #修改用户信息
15."ramking/"               #积分排行榜
16."ranking/api/my-rank/"      #查看用户排名、积分（API）
17."login/"                   #用户登录
18."logout/"                  #退出登录
19."register/"                 #用户注册
20."personal_index/"           #查看个人信息
21."repair_info/"              #修改个人信息
22."admin/"                                   #Django管理后台
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
        'HOST' : '',#数据库配置
        'PORT' : '',
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
    python manage.py createsuperuser superusername
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
    ordinary:普通用户，仅可以访问基础界面
    super_users:超级用户，可以访问所有界面
    ```
2. 将用户加入到特定用户组中：
    需要超级用户通过Django admin手动添加

## 注意
# 此项目仅为DEMO,请勿直接应用于生产环境

## 贡献

欢迎贡献！请 fork 此仓库并提交 pull request。

## 许可证

此项目使用 MIT 许可证。有关更多信息，请参阅 LICENSE 文件。
