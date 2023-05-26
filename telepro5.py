import requests
from time import *
from threading import *
from random import *
import os
import telebot
import json
import hashlib
import datetime
import uuid
if os.name == 'nt':os.system('cls')
else:os.system('clear')

print(f'\tKhởi Chạy Bot! / {datetime.datetime.now()}')


with open('token.json', 'r') as f:
    data = json.load(f)

TOKEN = data['botToken']
class Pro5:
    def __init__(self,cookie):
        self.cookie = cookie
        self.id_pro5 = cookie.split('i_user=')[1].split(';')[0]
        self.headers = {
                'authority': 'www.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'vi',
                'cookie': cookie,
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                'viewport-width': '1366',
            }
        
        page = requests.get('https://www.facebook.com/forced_account_switch?next=https://m.facebook.com/login/identify?ctx=recover&_rdr',headers=self.headers).text
        self.fb_dtsg = page.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
        self.jazoet = page.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]


    def Follow(self,id):
        try:
            headers = self.headers.copy()
            headers['x-fb-friendly-name'] = 'CometUserFollowMutation'
            data = {
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoet,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'CometUserFollowMutation',
                'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1667114418950,431532,190055527696468,","subscribe_location":"PROFILE","subscribee_id":"'+id+'","actor_id":"'+self.id_pro5+'","client_mutation_id":"1"},"scale":1}',
                'server_timestamps': 'true',
                'doc_id': '5032256523527306',
            }
            subscribe = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
        except:
            pass
    
    def Reaction(self,id,type):
        try:
            headers = self.headers.copy()
            headers['x-fb-friendly-name'] = 'CometUFIFeedbackReactMutation'
            if type == 'LOVE':
                camxuc = '1678524932434102'
            if type == 'CARE':
                camxuc = '613557422527858'
            if type == 'HAHA':
                camxuc = '115940658764963'
            if type == 'WOW':
                camxuc = '478547315650144'
            if type == 'SAD':
                camxuc = '908563459236466'
            if type == 'ANGRY':
                camxuc = '444813342392137'   
            url = requests.get('https://www.facebook.com/'+id, headers=self.headers).url
            data = {
                'av':  self.id_pro5,
                '__user':  self.id_pro5,
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoet,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'CometUFIShareActionLinkMenuQuery',
                'variables': '{"hasParentStory":false,"shareableParams":{"url":"'+url+'"},"storyParams":{}}',
                'server_timestamps': 'true',
                'doc_id': '3807512182705839',
            }
            response = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
            feedback_id = response.split('"id":"')[3].split('"')[0]
            data = {
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoet,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation',
                'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1667106623951,429237,190055527696468,","feedback_id":"'+feedback_id+'","feedback_reaction_id":"'+camxuc+'","feedback_source":"PROFILE","is_tracking_encrypted":true,"tracking":["AZXg8_yM_zhwrTY7oSTw1K93G-sycXrSreRnRk66aBJ9mWkbSuyIgNqL0zHEY_XgxepV1XWYkuv2C5PuM14WXUB9NGsSO8pPe8qDZbqCw5FLQlsGTnh5w9IyC_JmDiRKOVh4gWEJKaTdTOYlGT7k5vUcSrvUk7lJ-DXs3YZsw994NV2tRrv_zq1SuYfVKqDboaAFSD0a9FKPiFbJLSfhJbi6ti2CaCYLBWc_UgRsK1iRcLTZQhV3QLYfYOLxcKw4s2b1GeSr-JWpxu1acVX_G8d_lGbvkYimd3_kdh1waZzVW333356_JAEiUMU_nmg7gd7RxDv72EkiAxPM6BA-ClqDcJ_krJ_Cg-qdhGiPa_oFTkGMzSh8VnMaeMPmLh6lULnJwvpJL_4E3PBTHk3tIcMXbSPo05m4q_Xn9ijOuB5-KB5_9ftPLc3RS3C24_7Z2bg4DfhaM4fHYC1sg3oFFsRfPVf-0k27EDJM0HZ5tszMHQ"],"session_id":"'+str(uuid.uuid4())+'","actor_id":"'+self.id_pro5+'","client_mutation_id":"1"},"useDefaultActor":false,"scale":1}',
                'server_timestamps': 'true',
                'doc_id': '5703418209680126',
            }

            reaction = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
        except:
            pass

    def Share(self,id):
        try:
            headers = self.headers.copy()
            headers['x-fb-friendly-name'] = 'useCometFeedToFeedReshare_FeedToFeedMutation'
            data = {
                'av': self.id_pro5,
                '__user': self.id_pro5,
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoet,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'useCometFeedToFeedReshare_FeedToFeedMutation',
                'variables': '{"input":{"attachments":{"link":{"share_scrape_data":"{\\"share_type\\":22,\\"share_params\\":['+id+']}"}},"audiences":{"undirected":{"privacy":{"allow":[],"base_state":"EVERYONE","deny":[],"tag_expansion_state":"UNSPECIFIED"}}},"is_tracking_encrypted":true,"navigation_data":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1664893636390,706285,190055527696468,"},"source":"www","tracking":["AZUddfeekpM0aHSr3XWS0jfF_fFr6ATMj3kF8vPvUlU793DAoa1OE9PlotVNXb2f2SKzraB1Rkewbho5CFDKej2t3gIjZLYg2q5Ujq66bnLJayHWWMXonMv6NEn46gZTUCjnDd_UpQkyBw41F9Kim2WZM9TFohUWfL1qgiCQnIRSGgaw4qWAHm41wpPyPA64R6vvQAQNkoJdWTi4t48b7XSldGhp5kK91K7eAOUQ8czDGwZRFZYkHlQg5K9avCaV_oiidWDf9sdhiS6VNcdGyTuQtP2XYSjo_Npfdq0UtcXbIjUwD41_K3-LgElpo7ZfBzkFndVUP7sUs_QwA5jXKVZXZusLaie0u2JfdsuFVmXpK6sz_5kCX1SJP8IEb0qJE3CEFyew48Q90b-k7lCR3ZK2taOhQvyuvQg432gk5vPOoypn9vOA7io8t9wi6IoGlIQdRP29X7-Kj7ev5BouFxyv8b0Q-jw0h0-AHfNzyipZ9WOUXeRwk6IlVF6W-5tkE32hQqGyaplireNtaiiZXgnLRKd4_f7PUcNKllIB5PWyUhTunp_mveS0992-Im_A4PZ0gBg5mhK0mppyXvSqeppkRFz-l4aBuRezEqh9vhtBTj94-QJk83oiDYudSpnB2V0c7zVRcgRSm9Lquacfl6LvU8fl4r81F82FtageLZU0kA"],"actor_id":"'+self.id_pro5+'","client_mutation_id":"3"},"renderLocation":"homepage_stream","scale":1,"privacySelectorRenderLocation":"COMET_STREAM","useDefaultActor":false,"displayCommentsContextEnableComment":null,"feedLocation":"NEWSFEED","displayCommentsContextIsAdPreview":null,"displayCommentsContextIsAggregatedShare":null,"displayCommentsContextIsStorySet":null,"displayCommentsFeedbackContext":null,"feedbackSource":1,"focusCommentID":null,"UFI2CommentsProvider_commentsKey":"CometModernHomeFeedQuery","__relay_internal__pv__FBReelsEnableDeferrelayprovider":true}',
                'server_timestamps': 'true',
                'doc_id': '5403968569656274',
            }
            share = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
        except:
            pass

    def Comment(self,id,content):
        try:
            headers = self.headers.copy()
            headers['x-fb-friendly-name'] = 'CometUFICreateCommentMutation'
            url = requests.get('https://www.facebook.com/'+id, headers=self.headers).url
            response = requests.post(url, headers=self.headers).text
            feedback_id = response.split('"CommentComposerGIFPlugin","feedback_id":"')[1].split('"')[0]
            data = {
                'av': self.id_pro5,
                '__user': self.id_pro5,
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoet,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'CometUFICreateCommentMutation',
                'variables': '{"displayCommentsFeedbackContext":null,"displayCommentsContextEnableComment":null,"displayCommentsContextIsAdPreview":null,"displayCommentsContextIsAggregatedShare":null,"displayCommentsContextIsStorySet":null,"feedLocation":"PERMALINK","feedbackSource":2,"focusCommentID":null,"groupID":null,"includeNestedComments":false,"input":{"attachments":null,"feedback_id":"'+feedback_id+'","formatting_style":null,"message":{"ranges":[],"text":"'+content+'"},"attribution_id_v2":"CometSinglePostRoot.react,comet.post.single,via_cold_start,1678182746354,299722,,","is_tracking_encrypted":true,"tracking":["AZX4Cb5U0NCZSreFp_oaOA32RxpiMu4EwR07zM-wEuiBsWirv9b6REyatmkd7dMspRK6QTbwPlN0iU9X8YYaMDP93l8uO9bkxdITLMF3qwyaB6-K4vV9SFYXEgcqjOxZ1tyvqbg-Z2-aiq7kRtm2J0WZgt6__7Ya_vgnoHmVwMPmEuaXGr6VFFmFCFn_LrQO6CDFt55jNeg_y_sxOAokZJmjMSHMcQ5IghJpBT0uQUFuH2hFX0tk1SePTgWBPSATEsTRApXdywkuyBS_c5BhSJx_0o4QsLUDa5yu7UIlyXAAD7YfUVG9fq2OhNmZ9B9T9yAWT0tWzwwaa8YWPqNb5owE78iXzCt1ast4OhiOvRzf8UPyPWjFOeG3syNEGW_hzH-iOkADrc88nIX19fIcB9l39RXH2n6G9yJIchh717hn1F0dXCVeS0AazwOX7so9wwUBGOMuHd7p9T6hqI9oYrGhVl1owgKpN23wLx9TGtgyxIk-ItP0XWinlPpyl1XMkmA","{\\"assistant_caller\\":\\"comet_above_composer\\",\\"conversation_guide_session_id\\":\\"6ad214e6-6efe-40f7-81a8-58a54401b67a\\",\\"conversation_guide_shown\\":null}"],"feedback_source":"OBJECT","idempotence_token":"client:a4e6e19d-8d2c-44f6-9d2f-ee6a0d415c72","session_id":"432f58f8-5613-4f47-97a4-1b69c37a8657","actor_id":"'+self.id_pro5+'","client_mutation_id":"3"},"inviteShortLinkKey":null,"renderLocation":null,"scale":1,"useDefaultActor":false,"UFI2CommentsProvider_commentsKey":"CometSinglePostRoute"}',
                'server_timestamps': 'true',
                'doc_id': '6387920014553527',
            }

            comment = requests.post('https://www.facebook.com/api/graphql/',headers=headers, data=data)
        except:
            pass

    def JoinGroup(self,id):
        try:
            headers = self.headers.copy()
            headers['x-fb-friendly-name'] = 'GroupCometJoinForumMutation'
            url = requests.get('https://www.facebook.com/'+id, headers=self.headers).url
            response = requests.post(url, headers=self.headers).text
            app_id = response.split('app_id":"')[1].split('"')[0]
            data = {
                'av': '100086313108343',
                '__user': '100086313108343',
                'fb_dtsg': 'NAcMNHIWGJ7EcUvyrwNO9JykEcaclAl68aJkLoJc8mcWEvpQ2Sjpg5g:6:1677476745',
                'jazoest': '25508',
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'GroupCometJoinForumMutation',
                'variables': '{"feedType":"DISCUSSION","groupID":"'+id+'","imageMediaType":"image/x-auto","input":{"action_source":"GROUP_MALL","attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,via_cold_start,1678183270519,858401,2361831622,","group_id":"'+id+'","group_share_tracking_params":{"app_id":"'+app_id+'","exp_id":"null","is_from_share":false},"actor_id":"'+self.id_pro5+'","client_mutation_id":"1"},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"isEntityMenu":true,"scale":1,"source":"GROUP_MALL","renderLocation":"group_mall","__relay_internal__pv__GroupsCometEntityMenuEmbeddedrelayprovider":true,"__relay_internal__pv__GlobalPanelEnabledrelayprovider":false}',
                'server_timestamps': 'true',
                'doc_id': '9323864867623656',
                'fb_api_analytics_tags': '["qpl_active_flow_ids=431626709"]',
            }
            join = requests.post('https://www.facebook.com/api/graphql/',headers=headers, data=data)
        except:
            pass


class TDS:
    def __init__(self,token):
        self.token = token
        
    def infomation(self):
        try:
            info = requests.get(f'https://traodoisub.com/api/?fields=profile&access_token={self.token}').json()['data']
            user = info['user']
            xu = info['xu']
            xudie = info['xudie']
            return {'user':user,'xu':xu,'xudie':xudie}
        except:
            return False
    
    def Config(self,id):
        try:
            config = requests.get(f'https://traodoisub.com/api/?fields=run&id={id}&access_token={self.token}').json()
            if 'success' in config:
                return True
            else: 
                return False
        except: return False

with open('token.json','r+') as f:
    TOKEN = json.loads(f.read())['botToken']

def TimeStamp():
    now = str(datetime.date.today())
    return now
print('\n\t\tSTART BOT')

class BOT:
    def __init__(self):
        self.run = False
        self.stop = False
        self.cookie = None
        self.token = None
        self.proxy = None
        self.delay = 5
        self.id_pro5 = None


        bot = telebot.TeleBot(TOKEN)
        @bot.message_handler(commands=['start'])
        def start(message):
            if message.chat.username is not None:
                username = message.chat.username
            else:
                username = f"{message.chat.first_name} {message.chat.last_name}"

            text = f'''
            Xin Chào {username.upper()} Đã Đến Với Bot Tdspro5
             - Xem Cách Chạy Bot DÙng Lệnh [/how]
             - Xem Thông TIn Admin DÙng Lệnh [/admin]
            '''
            bot.send_message(message.chat.id, text)

        @bot.message_handler(commands=['admin'])
        def admin(message):
            info = '''
- THÔNG TIN CƠ BẢN 🧑🏻‍💻
 + NAME: Trương Ngọc Khánh
 + NICKNAME: K07VN
 + DATE OF BIRTH: 03/09/2007

- THÔNG TIN LIÊN HỆ 📞
 + ZALO: zalo.me/0964243159
 + FACEBOOK: facebook.com/TNKhanh39
            '''
            bot.reply_to(message, text=info)

        @bot.message_handler(commands=['how'])
        def how(message):
            text = '''
⚙️ CÁCH CHẠY BOT ⚙️
 B1. Dùng Lệnh [/start_pro5] để bắt đầu chạy
 B2. Dùng Lệnh [/cookie {cookie_pro5}] để add cookie
 B3. Dùng Lệnh [/token {token_tds}] để add token
 B4. Dùng Lệnh [/run_pro5 {Số Job Muốn Làm}]

⚙️ MỘT SỐ CHỨC NĂNG KHÁC ⚙️
 - Dùng lệnh /delay {delay} để thêm delay (nếu không dùng thì delay mặc định là 5s)
 - Dùng lệnh /proxy {proxy} (dùng lệnh /type_proxy để xem định dạng)
 - Để tạm dừng tương tác khi bot đang chạy dùng lệnh [/stop]
 - Để tiếp tục chạy sau khi dùng [/stop] dùng lệnh [/restart]
            '''
            bot.send_message(message.chat.id, text)
        
        @bot.message_handler(commands=['stop'])
        def stop(message):
            if self.stop == False:
                self.stop == True
                bot.send_message(message.chat.id, text='Đã tạm dừng tương tác, để tiếp tục chạy sử dụng lệnh [/restart]')
            else:
                bot.send_message(message.chat.id, text='BOT đang dừng, để tiếp tục chạy sử dụng lệnh [/restart]')
        
        @bot.message_handler(commands=['restart'])
        def start(message):
            if self.stop == True:
                self.stop == False
                bot.send_message(message.chat.id, text='Bắt đầu chạy tương tác, để tạm dừng dùng lệnh [/stop]')
            else:
                bot.send_message(message.chat.id, text='BOT đang chạy tương tác, để tạm dừng dùng lệnh [/stop]')

        @bot.message_handler(commands=['start_pro5'])
        def start_pro5(message):
            bot.reply_to(message, text='Vui Lòng Đợi Trong Giây Lát!')
            with open('key.txt','a') as f:
                f.close()
            self.username = message.from_user.username
            string = f'darling-{self.username}+{TimeStamp()}'
            hash_object = hashlib.md5(string.encode())
            self.key = str(hash_object.hexdigest())
            url_key = requests.get(f'https://link1s.com/api?api=f176c6f1a202a2f64ca491136933bfbccde15381&url=https://darling-api.000webhostapp.com/key/?key={self.key}').json()['shortenedUrl']
            text = f'''
- Link Lấy Key {TimeStamp()} là : {url_key} -
- Khi lấy key xong dùng lệnh /key {{key}} để check key
- Nếu đã nhập key thì chỉ cần /key True
            '''
            bot.send_message(message.chat.id,text)

        @bot.message_handler(commands=['key'])
        def key(message):
            try:
                self.username = message.from_user.username
                string = f'darling-{self.username}+{TimeStamp()}'
                hash_object = hashlib.md5(string.encode())
                self.key = str(hash_object.hexdigest())
                key_ =  message.text.split(' ', 1)[1]
                text = '''
    Key đúng! 🔓
    - Dùng lệnh /cookie {cookie_pro5} để add cookie
    - Dùng lệnh /token {token_tds} dá»ƒ add token
                '''
                if self.key in str(open('key.txt','r+').read().split('\n')[0]):
                    self.run = True
                    bot.send_message(message.chat.id, text)
                elif key_ == self.key:
                    self.run = True
                    with open('key.txt','w+') as f:
                        f.write(self.key)
                    bot.send_message(message.chat.id, text)
                else:
                    text = '''
    Key Sai! 🔒
    - Vui lòng nhập đúng định dạng /key {key}
                    '''
                    self.run = False
                    bot.send_message(message.chat.id, text)
            except:
                bot.send_message(message.chat.id, 'Key Không Hợp Lệ ❌!')
        
        @bot.message_handler(commands=['cookie'])
        def cookie(message):
            if self.run == True:
                try:
                    cookie = message.text.split(' ', 1)[1]
                    try:
                        self.pro5 = Pro5(cookie)
                        self.id_pro5 = self.pro5.id_pro5
                        self.cookie = cookie
                        bot.send_message(message.chat.id, text=f'Add cookie thành công - User {self.id_pro5}')
                    except:
                        bot.send_message(message.chat.id, text='Cookie Die! ❌')
                except:
                    bot.send_message(message.chat.id, text='Cookie không hợp lệ! ❌')
            else:
                bot.send_message(message.chat.id, text='Bạn chưa nhập key cho hôm nay! ❌')
        
        @bot.message_handler(commands=['token'])
        def token(message):
            if self.run == True:
                try:
                    token = message.text.split(' ', 1)[1]
                    self.tds = TDS(token)
                    if self.tds.infomation() != False:
                        self.token = token
                        bot.send_message(message.chat.id, text=f'Add token thành công - User {self.tds.infomation()["user"]} - Xu {self.tds.infomation()["xu"]}')
                    else:
                        bot.send_message(message.chat.id, text='Token không hợp lệ! ❌')
                except:
                    bot.send_message(message.chat.id, text='Token không hợp lệ! ❌')
            else:
                bot.send_message(message.chat.id, text='Bạn chưa nhập key cho hôm nay!! ❌')
                
        @bot.message_handler(commands=['delay'])
        def delay(message):
            if self.run == True:
                try:
                    delay = int(message.text.split(' ', 1)[1])
                    self.delay = delay
                    bot.send_message(message.chat.id, text=f'Add Delay {delay}s Thành Công')
                except:
                    bot.send_message(message.chat.id, text='Delay phải là số nguyên tố! vd: /delay 10')
            else:
                bot.send_message(message.chat.id, text='Bạn chưa nhập key cho hôm nay!! ❌')

        @bot.message_handler(commands=['run_pro5'])
        def run_pro5(message):
            if self.run == True:
                if self.cookie!= None or self.token != None:
                    try:
                        limit = int(message.text.split(' ', 1)[1])
                        def pro5_():
                            cauhinh = self.tds.Config(id=self.id_pro5)
                            if cauhinh == True:
                                bot.send_message(message.chat.id, text='Cấu Hình Thành Công!')
                                def jobfollow(sj:list):
                                    try:
                                        id = requests.get(f'https://traodoisub.com/api/?fields=follow&access_token={self.token}').json()[0]['id']
                                        self.pro5.Follow(id)
                                        nhan = requests.get(f'https://traodoisub.com/api/coin/?type=FOLLOW&id={id}&access_token={self.token}').json()
                                        if'success' in nhan:
                                            xu = nhan['data']['xu']
                                            msg = nhan['data']['msg']
                                            text =f'''
JOB SUCCESS ✅
+ JOB:  FOLLOW
+ MSG: {msg}
+ COIN: {xu}
+ UID: {id}
+ TIME: {datetime.datetime.now()}
                                            '''
                                            bot.send_message(message.chat.id, text)
                                            sj.append(1)
                                            sleep(self.delay)
                                        else:
                                            bot.send_message(message.chat.id, text=f'Job Follow Fail! 😭')
                                            sleep(3)
                                    except:
                                        bot.send_message(message.chat.id, text=f'Tạm Thời Hết Job Follow! 😭')
                                    
                                def jobreaction(sj:list):
                                    try:
                                        job = requests.get(f'https://traodoisub.com/api/?fields=reaction&access_token={self.token}').json()[0]
                                        id = job['id']
                                        type = job['type']
                                        self.pro5.Reaction(id, type)
                                        nhan = requests.get(f'https://traodoisub.com/api/coin/?type={type}&id={id}&access_token={self.token}').json()
                                        if'success' in nhan:
                                            xu = nhan['data']['xu']
                                            msg = nhan['data']['msg']
                                            text =f'''
JOB SUCCESS ✅
+ JOB:  {type}
+ MSG: {msg}
+ COIN: {xu}
+ UID: {id}
+ TIME: {datetime.datetime.now()}
                                            '''
                                            bot.send_message(message.chat.id, text)
                                            sj.append(1)
                                            sleep(self.delay)
                                        else:
                                            bot.send_message(message.chat.id, text=f'Job Reaction Fail! 😭')
                                            sleep(3)

                                    except:
                                        bot.send_message(message.chat.id, text=f'Tạm Thời Hết job Reaction! 😭')
                                    
                                def jobjoin(sj:list):
                                    try:
                                        id = requests.get(f'https://traodoisub.com/api/?fields=group&access_token={self.token}').json()[0]['id']
                                        self.pro5.JoinGroup(id)
                                        nhan = requests.get(f'https://traodoisub.com/api/coin/?type=GROUP&id={id}&access_token={self.token}').json()
                                        if'success' in nhan:
                                            xu = nhan['data']['xu']
                                            msg = nhan['data']['msg']
                                            text =f'''
JOB SUCCESS ✅
+ JOB:  GROUP
+ MSG: {msg}
+ COIN: {xu}
+ UID: {id}
+ TIME: {datetime.datetime.now()}
                                            '''
                                            bot.send_message(message.chat.id, text)
                                            sj.append(1)
                                            sleep(self.delay)
                                        else:
                                            bot.send_message(message.chat.id, text=f'Job Group Fail! 😭')
                                            sleep(3)
                                    except:
                                        bot.send_message(message.chat.id, text=f'Tạm Thời Hết Job Group! 😭')
                                
                                def run():
                                    sj = []
                                    while len(sj) < limit:
                                        if self.stop == False:
                                            jobreaction(sj)
                                        else:
                                            pass
                                    

                                    bot.send_message(message.chat.id, text=f'Đã Hoàn Thành {limit} Jobs!')
                                run()
                        t = Thread(target=pro5_)
                        t.start()
                                    

                    except:
                        bot.send_message(message.chat.id, text='Số Job Muốn Làm Phải Là Số Nguyên Tố vd: /run_pro5 10')
                else:
                    bot.send_message(message.chat.id, text='Bạn Add Thiếu Cookie Hoặc Token!')
            else:
                bot.send_message(message.chat.id, text='Bạn chưa nhập key cho hôm nay!! ❌')


        bot.polling()

bot = BOT()