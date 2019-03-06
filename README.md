# abianji
Abianji is a blog system with Django

## 创建数据库

```mysql
CREATE DATABASE `abianji` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLL
ATE utf8mb4_unicode_ci */;
```

## 安装驱动

```
$ pipenv install mysqlclient
```

## 运行前端打包
```
$ npm run serve
```

注意前端打包的静态资源文件需要在浏览器内禁用缓存当执行build任务的时候会添加hash

## Installation
```
$ git clone git@github.com:liseen315/abianji.git
$ cd abianji
$ pipenv install
$ pipenv shell
$ python manage.py runserver 
```

## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).