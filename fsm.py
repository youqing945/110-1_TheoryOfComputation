from transitions.extensions import GraphMachine

from utils import *
import random


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_sShopee(self, event):
        text = event.message.text
        return text.lower() == "蝦皮評論"

    def is_going_to_sFortune(self, event):
        text = event.message.text
        return text.lower() == "此刻運勢"

    def is_going_to_sCat(self, event):
        text = event.message.text
        return text.lower() == "可愛貓貓"

    #sShopee
    def on_enter_sShopee(self, event):
        print("I'm entering sShopee")

        reply_token = event.reply_token
        message = [add_text("蝦皮好評模板（30字+圖），複製使用唷"),
                    add_text("賣場大大您好您賣的東西真的是好極了大家不用看了這絕對是超級讚的東西"),
                    add_image(get_random_google_image('讚'))]
        send_all_message(reply_token, message)
        self.go_back()

    def on_exit_sShopee(self):
        print("Leaving sShopee")

    #sFortune
    def on_enter_sFortune(self, event):
        print("I'm entering sFortune")

        f_kind = ['大吉', '中吉', '小吉', '吉', '末吉', '凶', '大凶']

        ran = random.randint(0,6)

        reply_token = event.reply_token
        message = [add_text(str("你此時此刻抽到了" + f_kind[ran] + ",下面這張圖是你的命定圖：")),
                    add_image(get_random_google_image(str("運勢 " + f_kind[ran]))),
                    add_text("這只是你此刻的運勢，過了0.1秒後可能就不一樣囉，結果僅供參考或者跟個人業障有關，啾咪<3")]
        send_all_message(reply_token, message)
        self.go_back()

    def on_exit_sFortune(self):
        print("Leaving sFortune")

    #sCat
    def on_enter_sCat(self, event):
        print("I'm entering sCat")
        
        reply_token = event.reply_token
        message = [add_text('給你可愛貓貓！'),
                    add_image(get_random_google_image('cute cat kitten'))]
        send_all_message(reply_token, message)
        self.go_back()

    def on_exit_sCat(self):
        print("Leaving sCat")
