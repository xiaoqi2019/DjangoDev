"""
Django settings for DjangoDev03 project.

Generated by 'django-admin startproject' using Django 3.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import datetime
import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, 'apps'))  # 加到系统路径列表的尾部
# sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))  # 加到系统路径列表的头部


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0qgx5+#ej(s!y&#xz%0^7&g_onma($v%gentp_0ksgzaxo6jp7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ["外网ip", "localhost", "127.0.0.1"]
# 设置可以用于访问项目的地址（ip,域名）
# 默认只能使用本地地址访问项目，*表示都可以
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # 引入DRF框架
    'django_filters',  # 过滤引擎添加
    'corsheaders',  # 解决前后端跨域问题


    'projects.apps.ProjectsConfig',  # 子应用添加应用名.apps.应用名Config
    'interfaces.apps.InterfacesConfig',
    'users.apps.UsersConfig',
    'testcases.apps.TestcasesConfig',
    'testsuits.apps.TestsuitsConfig',
    'reports.apps.ReportsConfig',
    'envs.apps.EnvsConfig',
    'debugtalks.apps.DebugtalksConfig',
    'configures.apps.ConfiguresConfig',
    'summary.apps.SummaryConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 解决跨域需要添加的中间件，必须添加在CommonMiddleware之前
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware', # 自己注释是因为post请求时总是提示：CSRF验证失败. 请求被中断
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS_ORIGIN_ALLOW_ALL为True，指定所有域名（ip）都可以访问后端接口，默认为False
CORS_ORIGIN_ALLOW_ALL = True

# CORS_ORIGIN_WHITELIST指定能够访问后端接口的ip或者域名列表(和上面的允许所以二选一)
# CORS_ORIGIN_WHITELIST = [
#     "http://127.0.0.1:8080",
#     "http://localhost:8080"
# ]

# 允许跨域携带Cookie，默认为False
CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'DjangoDev03.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoDev03.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 指定数据库引擎
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'dev_django', # 指定数据库名
        'USER': 'root', # 数据库用户名
        'PASSWORD': 'root', # 数据库密码
        'HOST': 'localhost', # 数据库主机域名或者ip
        'PORT': '3306' # 数据库端口号
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    # 默认响应渲染类
    # 'DEFAULT_RENDERER_CLASSES': [
    #     # Json渲染器为第一优先级
    #     'rest_framework.renderers.JSONRenderer',
    #     # 可浏览的API渲染器为第二优先级--不需要可以注释掉即可
    #     # 'rest_framework.renderers.TemplateHTMLRenderer',
    # ],

    # 默认过滤引擎，默认路径
    "DEFAULT_FILTER_BACKENDS":
        [
            'django_filters.rest_framework.backends.DjangoFilterBackend',  # 过滤引擎路径
            'rest_framework.filters.OrderingFilter'  # 排序引擎路径
        ],
    # 全局指定分页引擎类
    'DEFAULT_PAGINATION_CLASS':
	    # 'rest_framework.pagination.PageNumberPagination',
      # 指定下面的就是使用'http://localhost:9000/projects/?p=1&s=3'格式
        'utils.pagination.ManualPageNumberPagination',
    # 一定要指定每页获取的条数
    'PAGE_SIZE': 10,
    "DEFAULT_SCHEMA_CLASS":
        # 指定用于支持cpreapi的Schema,DRF>3.10需要添加如下配置
        "rest_framework.schemas.coreapi.AutoSchema",
    # 指定认证类（指定是认证的方式）
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 可同时支持下面两种认证SESSION和Token认证
        # 指定使用JWT Token认证
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        # DRF默认情况下，使用的是会话认证
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    ],
    # 认定授权类(指的是认证成功之后能干嘛)--
    # ---------全局默认允许所有，在需要制定授权类视图里面单独制定权限
    # 'DEFAULT_PERMISSION_CLASSES':
    #     # DER默认情况下的权限AllowAny（允许所以用户访问）
    #     # IsAuthenticated 只有登录之后可以请求
    #     ['rest_framework.permissions.IsAuthenticated'],
}

# Token过期时间设置
JWT_AUTH = {
    # 默认token的过期时间为5分钟（seconds=300），可以指定过期时间为1天
    # 'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
        # 修改token值的前缀，默认JWT，可以修改成Bearer
        # 前端在传递token值时，Authorization作为key,值为token
    # 'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    # 指定返回前端的数据进行重写
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'utils.jwt_handle.jwt_response_payload_handler',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(asctime)s - [%(levelname)s] - %(name)s - [msg]%(message)s - [%(filename)s:%(lineno)d]'
        },
        'simple': {
            'format': '%(asctime)s - [%(levelname)s] - [msg]%(message)s'
        }
    },
    'handlers': {
        'file': {
             'level': 'INFO',
             'class': 'logging.handlers.RotatingFileHandler',
             'filename': os.path.join(BASE_DIR, 'logs/test.log'),  # 日志文件位置
             'maxBytes': 100 * 1024 * 1024,  # 日志文件大小
             'backupCount': 10,  # 日志文件最大个数
             'formatter': 'verbose',
             'encoding': 'utf-8' # 防止输出的日志乱码
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'test': {  # 定义了一个名为test的日志器
            'handlers': ['console', 'file'],
            'level': 'DEBUG',  # 日志器接受的最低日志级别
            'propagate': True  # 是否继承父类的log信息
        },
    }
}

# 在全局配置文件中，添加全局变量信息
REPORTS_DIR = os.path.join(BASE_DIR, 'reports')

# 在全局配置文件中，指定用例存放的目录
SUITES_DIR = os.path.join(BASE_DIR, 'suites')

# 创建STATIC_ROOT, 存放静态文件的目录
STATIC_ROOT = os.path.join(BASE_DIR, "static")


