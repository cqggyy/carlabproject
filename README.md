# carlabproject 说明

## 安装部分命令列表
- 新建虚拟环境
`virtualenv blogproject_env`
- 激活和退出虚拟环境
`activate`
`deactivate`

- 安装django
`pip install django`

- 安装mysql连接
`pip install pymysql`
`pip install mysqlclient`

- 连接mysql的设置代码
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '*****',
        'USER': '****',
        'PASSWORD': '*******',
        'HOST': 'ip',
        'PORT': '3306',
    }
}
```



- 建立Django工程
`django-admin startproject *****project`

- 运行服务器
`python manage.py runserver`

- 修改语言
```
blogproject/blogproject/settings.py

## 其它配置代码...

LANGUAGE_CODE = 'en-us'  'zh-hans'
TIME_ZONE = 'UTC'   'Asia/Shanghai'

## 其它配置代码...
```

## 编程部分命令列表

- 建立应用
  进入工程目录，建立应用
`python manage.py startapp blog`
- 数据库迁移
`python manage.py makemigrations`
`python manage.py migrate`
