# 計理作業 Line Bot

加入此聊天機器人：

<img src="./img/644bohuz.png" style="zoom:40%" />



---

一個有以下功能的聊天機器人（非常的雜）：

* 蝦皮評論：生成蝦皮評論用模板，包含文字跟圖片，複製貼上就不用拍跟想了
* 此刻運勢：非常即時的運勢抽籤，過了0.1秒後運勢會大不相同！？
* 可愛貓貓：作者是貓派，每天需要一點貓以撫平厭世的作者
* [輸入其他字串]：以此字串為關鍵字上Google隨機找一張圖

圖片部分本來想用serpapi的GoogleSearch跟BeautifulSoup4，但無奈失敗了嗚嗚

## 如何使用

### 使用ngrok

1. 執行app.py

	在app.py的目錄下執行

	```console
	python app.py
	```
2. 執行ngrok

	在有ngrok執行檔的目錄下執行
	沒有token的話要登入拿

	```console
	./ngrok authtoken <token>
	```
	```console
	./ngrok http 8000
	```
3. 得到Forwarding網址

	例：https://b391-61-70-50-24.ngrok.io

**聊天機器人**

1. 在Messaging API>Webhook settings>Webhook URL把剛剛的Forwarding網址貼上並加上結尾"/webhook"

	例：https://b391-61-70-50-24.ngrok.io/webhook

2. 打開Use webhook

3. 點Webhook URL下的Verify（此時app.py與ngrok皆還在執行），若成功會顯示Success，app.py的Terminal也會開始接收訊息

4. 成功啟用。執行期間每有檔案變更存檔皆會更新。

**FSM Diagram生成**

1. 在網址列貼上剛剛的Forwarding網址，結尾加上"/show-fsm"

	例：https://b391-61-70-50-24.ngrok.io/show-fsm

2. 前往該網址，即可得FSM Diagram

### 使用Heroku

還沒研究但我相信demo前弄得出來(

對目前只在ngrok上跑過QQ

## 部分研究資料

來不及放了啊啊啊

---
Template: https://github.com/NCKU-CCS/TOC-Project-2020

以下為原README.md內容：
# TOC Project 2020

[![Maintainability](https://api.codeclimate.com/v1/badges/dc7fa47fcd809b99d087/maintainability)](https://codeclimate.com/github/NCKU-CCS/TOC-Project-2020/maintainability)

[![Known Vulnerabilities](https://snyk.io/test/github/NCKU-CCS/TOC-Project-2020/badge.svg)](https://snyk.io/test/github/NCKU-CCS/TOC-Project-2020)


Template Code for TOC Project 2020

A Line bot based on a finite state machine

More details in the [Slides](https://hackmd.io/@TTW/ToC-2019-Project#) and [FAQ](https://hackmd.io/s/B1Xw7E8kN)

## Setup

### Prerequisite
* Python 3.6
* Pipenv
* Facebook Page and App
* HTTPS Server

#### Install Dependency
```sh
pip3 install pipenv

pipenv --three

pipenv install

pipenv shell
```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)
	* [Note: macOS Install error](https://github.com/pygraphviz/pygraphviz/issues/100)


#### Secret Data
You should generate a `.env` file to set Environment Variables refer to our `.env.sample`.
`LINE_CHANNEL_SECRET` and `LINE_CHANNEL_ACCESS_TOKEN` **MUST** be set to proper values.
Otherwise, you might not be able to run your code.

#### Run Locally
You can either setup https server or using `ngrok` as a proxy.

#### a. Ngrok installation
* [ macOS, Windows, Linux](https://ngrok.com/download)

or you can use Homebrew (MAC)
```sh
brew cask install ngrok
```

**`ngrok` would be used in the following instruction**

```sh
ngrok http 8000
```

After that, `ngrok` would generate a https URL.

#### Run the sever

```sh
python3 app.py
```

#### b. Servo

Or You can use [servo](http://serveo.net/) to expose local servers to the internet.


## Finite State Machine
![fsm](./img/show-fsm.png)

## Usage
The initial state is set to `user`.

Every time `user` state is triggered to `advance` to another state, it will `go_back` to `user` state after the bot replies corresponding message.

* user
	* Input: "go to state1"
		* Reply: "I'm entering state1"

	* Input: "go to state2"
		* Reply: "I'm entering state2"

## Deploy
Setting to deploy webhooks on Heroku.

### Heroku CLI installation

* [macOS, Windows](https://devcenter.heroku.com/articles/heroku-cli)

or you can use Homebrew (MAC)
```sh
brew tap heroku/brew && brew install heroku
```

or you can use Snap (Ubuntu 16+)
```sh
sudo snap install --classic heroku
```

### Connect to Heroku

1. Register Heroku: https://signup.heroku.com

2. Create Heroku project from website

3. CLI Login

	`heroku login`

### Upload project to Heroku

1. Add local project to Heroku project

	heroku git:remote -a {HEROKU_APP_NAME}

2. Upload project

	```
	git add .
	git commit -m "Add code"
	git push -f heroku master
	```

3. Set Environment - Line Messaging API Secret Keys

	```
	heroku config:set LINE_CHANNEL_SECRET=your_line_channel_secret
	heroku config:set LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
	```

4. Your Project is now running on Heroku!

	url: `{HEROKU_APP_NAME}.herokuapp.com/callback`

	debug command: `heroku logs --tail --app {HEROKU_APP_NAME}`

5. If fail with `pygraphviz` install errors

	run commands below can solve the problems
	```
	heroku buildpacks:set heroku/python
	heroku buildpacks:add --index 1 heroku-community/apt
	```

	refference: https://hackmd.io/@ccw/B1Xw7E8kN?type=view#Q2-如何在-Heroku-使用-pygraphviz

## Reference
[Pipenv](https://medium.com/@chihsuan/pipenv-更簡單-更快速的-python-套件管理工具-135a47e504f4) ❤️ [@chihsuan](https://github.com/chihsuan)

[TOC-Project-2019](https://github.com/winonecheng/TOC-Project-2019) ❤️ [@winonecheng](https://github.com/winonecheng)

Flask Architecture ❤️ [@Sirius207](https://github.com/Sirius207)

[Line line-bot-sdk-python](https://github.com/line/line-bot-sdk-python/tree/master/examples/flask-echo)
