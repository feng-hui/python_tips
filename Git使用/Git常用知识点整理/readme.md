##### 1、如何安装Git?

Git支持Linux、Unix、Mac、Windows等多个平台。

（1）Linux上安装Git

`sudo apt-get install git`

（2）Mac上安装Git

```
# 方法1 使用homebrew

brew install git

# 方法2

直接从AppStore安装Xcode，Xcode集成了Git，默认不安装，可以通过：菜单Xcode -> 选择Preferences，在弹出的窗口找到Downloads，选择Command Line Tools，点击install即可。
```

（3）Windows上安装Git

通过Git官网[下载程序](https://git-scm.com/downloads)，然后按照默认选项安装即可。

（4）安装完成后的配置

```
# --global为全局配置，不带表示对当前仓库指定用户名和Email

git config --global user.name "your name"

git config --global user.email "your email"
```

##### 2、如果配置多个密钥?

##### 3、常用方法整理?

（1）git的起源

Linus花了两周时间用C构建的分布式版本控制系统。

（2）集中式vs分布式

CVS/SVN：集中式的版本控制系统

GIT：分布式版本控制系统

（3）常用操作