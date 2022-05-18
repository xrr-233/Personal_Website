## 开发日志

+ 2022/1/8

舍弃旧有的flask-script，改用flask.cli表示方法来连结flask-migrate

+ 2022/1/10

选择使用gunicorn和nginx将网站挂上

gunicorn -D -w 1 -b 127.0.0.1:5000 app:app

参考文章：

https://zhuanlan.zhihu.com/p/92003835

https://www.cnblogs.com/homeworknotes/p/11219902.html

+ 2022/1/13

移植数据库，创建账号

通过bootstrap（主要是modal）和ajax与flask结合成功完成登录模块开发

+ 2022/1/16

测试博客插件marked

+ 2022/1/22

个人中心网页初步开发，以允许博客上传

通过jquery.on实现标签切换，开发修改密码界面充当占位符（暂无功能）

+ 2022/3/12

补充：gunicorn重启：killall -9 gunicorn

允许以POST方式上传博客markdown文件（但尚未将博客在首页显示）

增加SystemStatus表以追踪博客数以及命名规范

待开发：提交博客表单后的反馈信息及动作

+ 2022/4/13

修复了bootstrap图标显示bug（更换为emoji）

追加博客主页显示功能

+ 2022/4/14

尝试vue模块化部分代码

https://learnku.com/python/t/24985

https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/

https://zhuanlan.zhihu.com/p/101544546

运行vue-cli:

cd client

npm run serve

+ 2022/4/15

正确的Flask+Vue框架整合：

https://juejin.cn/post/6909732949378203662

+ 2022/5/17

经过慎重斟酌，为使项目框架更加规范，欲参考https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/ 的描述，进行vue+flask混合的前后端分离开发，废弃jinja模板

+ 2022/5/18

采用新时钟样式 https://github.com/SlyTy7/clock

已经较为系统化地掌握了Vue模块的开发，以及通过axios实现的vue前端与flask后端（api与数据库）的交互