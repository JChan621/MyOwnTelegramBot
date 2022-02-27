import sys
sys.path.append('/home/jamesbot/.local/lib/python3.8/site-packages')
import schedule
from random import randint, seed
seed()
import MySQLdb
db_connection = MySQLdb.connect('jamesbot.mysql.pythonanywhere-services.com', 'jamesbot', '1Hakimi2', 'jamesbot$mydb')
mycursor = db_connection.cursor()
mycursor.execute('SET SESSION wait_timeout = 99999')
#['DataError', 'DatabaseError', 'Error', 'IntegrityError', 'InterfaceError', 'InternalError', 'MySQLError', 'NotSupportedError', 'OperationalError', 'ProgrammingError', 'Warning', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_check_executed', '_do_execute_many', '_do_get_result', '_escape_args', '_executed', '_fetch_row', '_fetch_type', '_get_db', '_get_result', '_last_executed', '_post_get_result', '_query', '_result', '_rows', '_warnings', 'arraysize', 'callproc', 'close', 'connection', 'description', 'description_flags', 'execute', 'executemany', 'fetchall', 'fetchmany', 'fetchone', 'lastrowid', 'max_stmt_length', 'messages', 'nextset', 'rowcount', 'rownumber', 'scroll', 'setinputsizes', 'setoutputsizes']
#mycursor.execute("CREATE TABLE UsersPlastic (ChatID INT, UserID INT, FirstName VARCHAR(255), Plastic INT, BEER INT, PlasticToday INT, BEERToday INT)")
columns = ['ChatID', 'UserID', 'FirstName', 'Plastic', 'BEER', 'PlasticToday', 'BEERToday']
digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

import telepot
from telepot.namedtuple import InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton
import urllib3
import json
#import logging
import imageio
import os
import requests
#from urllib.request import urlopen
#from urllib.parse import urlparse, parse_qs, unquote, quote
from urllib.parse import parse_qs, quote
import time
base = time.time()
#open('/home/jamesbot/mybotfiles/videoplayback3.mp4', 'wb').write(requests.get('https://r3---sn-i3b7knse.googlevideo.com/videoplayback?expire=1584008279&ei=97dpXuj4HYaZ4AKOn6l4&ip=113.28.144.183&id=o-AELmRAl4Urdj2gYjZsYExhGQp2_zwJxCimygkbjKCFkZ&itag=243&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C271%2C278%2C298%2C299%2C302%2C303%2C308&source=youtube&requiressl=yes&mm=31%2C26&mn=sn-i3b7knse%2Csn-npoeene7&ms=au%2Conr&mv=m&mvi=2&pl=19&initcwndbps=1036250&vprv=1&mime=video%2Fwebm&gir=yes&clen=6115173&dur=536.166&lmt=1583694111806804&mt=1583986605&fvip=3&keepalive=yes&fexp=23842630&c=web&txp=5531432&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=ADKhkGMwRQIhAOrbfAZfCOpCNXnB7FbdXDuJzGTQR81rlcLyE0szDZoHAiBFl80MDz1AABDEqpESeStugX6O2BpmvbdodD25aVmnSA%3D%3D&lsparams=mm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=ABSNjpQwRQIhAI1H0jo7Zimh1wPSx8paP_RWGmZPXfmC7ItzduQ2Up3XAiAMA65HNzLF7H1HNSVa2Gw1xldPBLOY8g8A93OvjUN5rg%3D%3D&alr=yes&cpn=B9dfGEd0OpDBekVz&cver=html5&range=0-82486&rn=1&rbuf=0', allow_redirects=True).content)
#import asyncio
#from telepot.aio.loop import MessageLoop
#from telepot.aio.delegate import pave_event_space, per_chat_id, create_open
proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url,
    num_pools = 3,
    maxsize = 10,
    retries = False,
    timeout = 30),
}
hr = 0
#maxid = 337690936
#fourierid = 199823643
#aecomchat : -391498384
me = 199823643
bad = 954104230
fargp = -1001156503383
maple = 486439692
modules = set(__builtins__).union(set(dict(sys.modules)))
sticker={
    "sorhi" : "CAACAgIAAxkBAAIByl5q4P3oRLROcYmiVCCMx3T1iYCgAAKmAAOrV8QLqUBfSGp88l8YBA",
    "sad" : "CAACAgIAAxkBAAIB2V5q5QrMNv7x33VIWAo1Y0vrJ4mbAAJaAAMsyqoHJWwfhyyBODEYBA"
    }
jj = 'CgACAgUAAxkDAAIEEV55Zm9UI6eyJbV9z17bSeLjBz9sAAIoAQACBHrBV4Gi0aYQLihDGAQ'
dex = "CgACAgUAAx0CRO7XVwACFzheeYYiZIj4JN3ezBtfwrme6AABBGgAAuMAA5iWyVfy-rCVao3hixgE"
sen = "CgACAgUAAxkBAAIEH156tdEILcEf3ovgdLb4pEfcRJd7AALqAAOQSslX-Juz_oVvxoQYBA"
gbig = "CgACAgUAAxkBAAIEkF6HD6-Q0bQ9DKuBlQF5qrdx0UjBAALiAAO89AhUE-T3ieL5AvoYBA"
shit = 'AgACAgQAAxkDAAIEol6ejwPXp36hwrP-C8eZYZwhlfzFAALRqjEbKMf8UIGV8l6UDj08AAFL0SJdAAMBAAMCAANtAAOWDQEAARgE'
far = "CAACAgUAAxkBAAIEv16gAAFkrma7WnBFP36gVMTALLxgpAACLQADDuO_IsogrwzLG7_dGAQ"
farunique = 'AgADLQADDuO_Ig'
farsad = "AgADpgADq1fECw"
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url = proxy_url, num_pools = 1, maxsize = 1, retries = False, timeout = 30))
bot = telepot.Bot('YourBotToken')
gavin = bot.getStickerSet('GavinReactionsUltimate')['stickers']
blackhonka = bot.getStickerSet('BlackHonka')['stickers']
honka_memes = bot.getStickerSet('honka_memes')['stickers']
def handle(msg):
    if msg['date'] + 10 > time.time():
        try:
            content_type, chat_type, chat_id = telepot.glance(msg)
            print(content_type, chat_type, chat_id)
            #print(msg)
            #bot.sendMessage(199823643,msg)
            if content_type == 'text' and not 'edit_date' in msg.keys():
                #if msg['text'] in ['是午','是日午餐','是早','是日早餐','是日晚餐','是晚']:
                #    bot.sendPhoto(chat_id,shit,msg['text'],None,None,msg['message_id'])
                #if msg['from']['id']==337690936:
                #    bot.sendMessage(chat_id,'屌你老母',None,None,None,msg['message_id'])
                #if msg['text'].startswith("/exec2 "):
                #    if msg['from']['id']==199823643:
                #        try:
                #            eval(msg['text'][7:].strip())
                #        except:
                #            bot.sendMessage(chat_id,"有bug，run唔到",None,None,None,msg['message_id'])
                #    else:
                #        bot.sendMessage(chat_id,"關唔關你事牙",None,None,None,msg['message_id'])
                #elif msg['from']['id']==me:
                   # if ({',','，','.','．','-','—','=','。'} & set(msg['text'])):
                        #print (1)
                        #bot.deleteMessage((chat_id,msg['message_id']))
                        #bot.sendMessage(chat_id,'表情撚必死')
                if msg['text'].lower().startswith("/exec "):
                    if msg['from']['id'] == 199823643:
                        try:
                            bot.sendMessage(chat_id, str(eval(msg['text'][6:].strip())), None, None, None, msg['message_id'])
                        except:
                            bot.sendMessage(chat_id, "有bug，run唔到", None, None, None, msg['message_id'])
                    elif any(pack in msg['text'][6:] for pack in modules) or 'bot' in msg['text']:
                        bot.sendMessage(chat_id, "關唔關你事牙", None, None, None, msg['message_id'])
                    else:
                        try:
                            bot.sendMessage(chat_id, str(eval(msg['text'][6:].strip())), None, None, None, msg['message_id'])
                        except:
                            bot.sendMessage(chat_id, "有bug，run唔到", None, None, None, msg['message_id'])
                elif msg['text'].startswith('/youtube ') and msg['from']['id'] == me:
                    deleteid = bot.sendMessage(chat_id, "請等等...", None, None, None, msg['message_id'])['message_id']
                    r = requests.get("https://www.youtube.com/results?search_query=" + quote(msg['text'][9:].strip())).content
                    time.sleep(2)
                    k = 0
                    #bot.sendMessage(me,len(r))
                    while True:
                        start = r[k:].find(b'data-context-item-id="') + 22
                        vid = r[k + start: r[k + start:].find(b'data-visi') + k + start - 2].decode('utf-8')
                        #bot.sendMessage(me,len(vid))
                        info = requests.get('https://www.youtube.com/get_video_info?video_id=' + vid).content.decode('utf-8') #OlJ2IBf_Im8
                        if 'videoplayback' in info:
                            break
                        k += start+22
                        time.sleep(2)
                    parsed = json.loads(parse_qs(info)['player_response'][0])
                    urllink = parsed['streamingData']['formats'][0]['url']
                    bot.sendMessage(me, urllink)
                    title = parsed['videoDetails']['title']
                    open('/home/jamesbot/mybotfiles/' + quote(title)[0: 10] + '.mp4','wb').write(requests.get(urllink).content)
                    reader = imageio.get_reader(r'/home/jamesbot/mybotfiles/' + quote(title)[0: 10] + '.mp4')
                    kargs = { 'macro_block_size': None }
                    counts = reader.get_meta_data()['fps']
                    writer = imageio.get_writer(r'/home/jamesbot/mybotfiles/' + quote(title)[0: 10] + '2.mp4', fps = reader.get_meta_data()['fps'], **kargs)
                    frames = reader.count_frames() // 2
                    count = 0
                    for i in reader:
                        if count in range(frames - int(counts * 3), frames + int(counts * 3)):
                            writer.append_data(i, meta = {'size':(480,320)})
                        count += 1
                    writer.close()
                    bot.sendDocument(chat_id, open('/home/jamesbot/mybotfiles/' + quote(title)[0: 10] + '2.mp4', 'rb'), title, None, None, msg['message_id'])
                    bot.deleteMessage((chat_id, deleteid))
                    os.remove('/home/jamesbot/mybotfiles/' + quote(title)[0: 10] + '2.mp4')
                    os.remove('/home/jamesbot/mybotfiles/' + quote(title)[0: 10] + '.mp4')
                elif msg['text'].startswith('/youtube '):
                    bot.sendMessage(chat_id, '本功能將於近日推出，請密切留意！', None, None, None, msg['message_id'])
                #elif 'HKU' in msg['text'].upper():
                #    bot.sendMessage(chat_id, "Kong U Civil 冇靚女 (我嗰屆)")
                    #bot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))
                #elif 'MAX' in msg['text'].upper():
                #    bot.sendMessage(chat_id,'勿演冷肉錢走，Thx！')
                #if msg['text'].st
                #if msg['text'].upper()=="sorhi":
                #    bot.sendMessage(chat_id,'屌你老母',None,None,None,msg['id'])
                elif msg['text'] in ["早", '早晨', '早。']:
                  if ((int(time.strftime('%H')) + 8) % 24) > 11:
                    bot.sendMessage(chat_id, str((int(time.strftime('%H')) + 7) % 12 + 1) + '點幾重早晨?', None, None, None, msg['message_id'])
                  else:
                    bot.sendMessage(chat_id, '早晨', None, None, None, msg['message_id'])
                elif msg['text'] in ['おはよう', 'お早う', 'おはよございます']:
                    if ((int(time.strftime('%H')) + 8) % 24) > 11:
                        return 0
                    elif ((int(time.strftime('%H')) + 8) % 24) > 6:
                        bot.sendMessage(chat_id, 'おはよございます', None, None, None, msg['message_id'])
                elif msg['text'] in ['找','找晨']:
                    if ((int(time.strftime('%H')) + 8) % 24) > 11:
                        bot.sendMessage(chat_id, '禾找你老母', None, None, None, msg['message_id'])
                    elif ((int(time.strftime('%H')) + 8) % 24) > 6:
                        bot.sendMessage(chat_id, '你找禾咩事牙-.-', None, None, None, msg['message_id'])
                elif msg['text'] in ['午','午安']:
                    if ((int(time.strftime('%H')) + 8) % 24) > 17:
                        bot.sendMessage(chat_id, '午你老母，' + str((int(time.strftime('%H')) + 7) % 12 + 1) + '點幾就早啲抖啦😪', None, None, None, msg['message_id'])
                    elif ((int(time.strftime('%H')) + 8) % 24) < 12:
                        bot.sendMessage(chat_id, '瞓醒未，晨早流流午乜鳩?', None, None, None, msg['message_id'])
                    else:
                        bot.sendMessage(chat_id, '午安，食咗飯未?', None, None, None, msg['message_id'])
                elif msg['text'] in ['牛']:
                    bot.sendMessage(chat_id, '字都唔識打，你係咪sen？', None, None, None, msg['message_id'])
                elif msg['text'] in ['晚','晚安']:
                    if ((int(time.strftime('%H')) + 8) % 24) > 17:
                        bot.sendMessage(chat_id, '早抖啦你', None, None, None, msg['message_id'])
                    else:
                        bot.sendMessage(chat_id, '早登極樂啦傻閪', None, None, None, msg['message_id'])
                elif any(i in msg['text'].upper() for i in ['牙龙', '牙遠', '思遠', '牙远', '思远', '牙龍', 'FAR']):
                    bot.sendMessage(chat_id, 'MK 大組長-.-')
                elif ({'龙','叶'} & set(msg['text'])):
                    bot.sendMessage(chat_id, '用乜撚嘢殘體呀，當呢度中国啊？', None, None, None, msg['message_id'])
                elif msg['text'] == '/log':
                    bot.sendMessage(chat_id, msg['reply_to_message'], None, None, None, msg['message_id'])
                elif 'JJ' in msg['text'].upper():
                    bot.sendDocument(chat_id, jj)
                elif 'dex' in msg['text'].lower():
                    bot.sendDocument(chat_id, dex)
                elif 'sen' in msg['text'].lower():
                    bot.sendDocument(chat_id, sen)
                elif '支大狗' in msg['text']:
                    #bot.sendPhoto(chat_id,"AAMCBQADGQEAAgflXxF38elJINxWc0MJ14aEjGZBkAIAAgQBAAKrdpBU0w_lcLZydK_8X-VrdAADAQAHbQAD8Z4AAhoE")
                    bot.sendDocument(chat_id, "CgACAgUAAxkDAAIH_F8ReXfe3v-wlcM_8Mi2eTMm7JAVAAIIAQACq3aQVNIDxVVC-3_MGgQ")
                    #bot.sendDocument(chat_id,gbig)
                elif msg['text'].upper() == ('/STAT@JOFOURIERBOT') or msg['text'].upper() == '/STAT':
                    groupStat(chat_id, msg['message_id'])
                elif msg['text'].upper() == '/CHECK' or msg['text'].upper() == '/CHECK@JOFOURIERBOT':
                    checkYourStat(chat_id, msg['from']['id'], msg['message_id'])
                elif msg['text'] in ['加油。','加油']:
                    if 'reply_to_message' in msg.keys():
                        bot.sendMessage(chat_id,'加油。', None, None, None, msg['reply_to_message']['message_id'])
                    else:
                        bot.sendMessage(chat_id,'加油。', None, None, None, msg['message_id'])
                elif msg['text'].upper().startswith('/D ') or msg['text'].upper() == '/D':
                    if msg['from']['id'] != me and(msg['from']['id'] == msg['reply_to_message']['from']['id']):
                        bot.sendMessage(chat_id, '冇得賜酒畀自己。', None, None, None, msg['message_id'])
                    elif len(msg['text'][3:].strip()) == 0:
                        bot.sendMessage(chat_id, '你想對' + msg['reply_to_message']['from']['first_name'] + '賜酒定派膠？', reply_markup = InlineKeyboardMarkup(inline_keyboard = [
                                        [InlineKeyboardButton(text = "賜酒", callback_data = '[2,1,' + str(msg['reply_to_message']['from']['id']) + ',' + str(msg['from']['id']) + ']'),
                                        InlineKeyboardButton(text = "派膠", callback_data = '[1,1,' + str(msg['reply_to_message']['from']['id']) + ',' + str(msg['from']['id']) + ']')]]
                                        ), reply_to_message_id = msg['message_id'])
                        #return 0
                    else:
                        short = msg['text'][3:].strip()
                        if not short[0] in digit:
                            BadRequests(chat_id, msg['message_id'])
                        else:
                            k = len(short)
                            for i in short:
                                if not i in digit:
                                    k = short.index(i)
                                    #integer=int(short[0:k])
                                    break
                            integer = int(short[0:k])
                            if (integer < 1 or integer > 100) and msg['from']['id'] != me:
                                BadRequests(chat_id, msg['message_id'])
                            else:
                                bot.sendMessage(chat_id, '你想對' + msg['reply_to_message']['from']['first_name'] + '賜酒定派膠？', reply_markup = InlineKeyboardMarkup(inline_keyboard = [
                                            [InlineKeyboardButton(text = "賜酒", callback_data = '[2,' + str(integer) + ',' + str(msg['reply_to_message']['from']['id']) + ',' + str(msg['from']['id']) + ']'),
                                            InlineKeyboardButton(text = "派膠", callback_data = '[1,'+str(integer) + ',' + str(msg['reply_to_message']['from']['id']) + ',' + str(msg['from']['id']) + ']')]]
                                            ), reply_to_message_id = msg['message_id'])

                    #for i in msg['text'][3:]:
                        #if not i in digit:
            #elif content_type=='photo'and 'caption' in msg.keys():
            #    if msg['caption'] in ['是午','是日午餐','是早','是日早餐','是日晚餐','是晚']:
            #        bot.sendPhoto(chat_id,shit,msg['caption'],None,None,msg['message_id'])
            elif content_type == 'sticker':
                if msg['sticker']['file_unique_id'] == farunique:
                    bot.sendDocument(chat_id, far, None, None, None, msg['message_id'])
                elif msg['sticker']['file_unique_id'] == farsad or msg['sticker']['file_unique_id'] == 'AgADSgADq1fECw':
                    bot.sendDocument(chat_id, gavin[randint(0, 120 - 1)]['file_id'], None, None, None, msg['message_id'])
                elif msg['sticker']['file_unique_id'] == "AgAD6gUAAq05MEo":
                    bot.sendDocument(chat_id, blackhonka[randint(0, len(blackhonka) - 1)]['file_id'], None, None, None, msg['message_id'])
                elif msg['sticker']['file_unique_id'] == "AgADqwADq1fECw":
                    bot.sendDocument(chat_id, honka_memes[randint(0, len(honka_memes) - 1)]['file_id'], None, None, None, msg['message_id'])
        except telepot.exception.TelegramError:
            bot.kickChatMember(-1001188563796, 1065532169)

#bot.getMe()
#bot.getUpdates()
def handle2(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor = 'callback_query')
    #print(msg)
    print(query_id, from_id, query_data)
    a = eval(query_data)
    if from_id != a[3]:
        bot.answerCallbackQuery(query_id, '咪搞人哋啲嘢')
        return 0
    receiver_id = a[2]
    if not memberExists(msg['message']['chat']['id'], from_id):
        addToDB(msg['message']['chat']['id'], from_id)
    if not memberExists(msg['message']['chat']['id'], receiver_id):
        addToDB(msg['message']['chat']['id'], receiver_id)
    count = a[1]
    type = a[0]
    if not plasticEnough(msg['message']['chat']['id'], from_id, count, type) and from_id != me:
        bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']), text = '唔夠' + ['膠', '酒'][type - 1] + '！', disable_web_page_preview = False, reply_markup = None)
        return 0
    if receiver_id == me:
        type = 2
    #else:
    DisPlastic(msg['message']['chat']['id'], receiver_id, from_id, count, type)
    bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']), text = '已' + ['派膠', '賜酒'][type - 1] + '！', disable_web_page_preview = False, reply_markup = None)
    #plasticEnough(msg['message']['chat']['id'], from_id, count, type)
    #msg['message']
#bot.message_loop({'chat': handle, 'callback_query': handle2}, timeout = 100, run_forever = True)
def addToDB(chat_id, user_id):
    mycursor.execute("INSERT INTO UsersPlastic ("
                        + columns[0] + ", "
                        + columns[1] + ", "
                        + columns[3] + ", "
                        + columns[4] + ", "
                        + columns[5] + ", "
                        + columns[6] + ") VALUES ("
                        + str(chat_id) + ", " + str(user_id) + ", 0, 0, 100, 100)")#columns=['ChatID','UserID','FirstName','Plastic','BEER','PlasticToday','BEERToday']
    db_connection.commit()
def resetPlastic():
    mycursor.execute("UPDATE UsersPlastic SET PlasticToday=100, BEERToday=100")
    db_connection.commit()
    bot.sendMessage(me,'Stat Reset.')
def memberExists(chat_id,user_id):
    mycursor.execute("SELECT * FROM UsersPlastic WHERE "+columns[0]+" = " + str(chat_id) +" AND "+columns[1]+" = "+str(user_id))
    result=mycursor.fetchall()
    if len(result)==0:
        return False
    else:
        return True
def plasticEnough(chat_id, user_id, count, type):#type=1 or 2
    mycursor.execute("SELECT * FROM UsersPlastic WHERE " + columns[0] + " = " + str(chat_id) + " AND " + columns[1] + " = " + str(user_id))
    result = mycursor.fetchall()
    if result[0][4 + type] < count:
        return False
    else:
        return True
def dis_Plastic(chat_id, receiver_id, Distributor_id, count, type):#type=1 or 2
    mycursor.execute("UPDATE UsersPlastic SET " + columns[2 + type] + " = "+columns[2 + type] + " + " + str(count) + " WHERE " + columns[0] + " = " + str(chat_id) + " AND " + columns[1] + " = " + str(receiver_id))
    mycursor.execute("UPDATE UsersPlastic SET " + columns[4 + type] + " = "+columns[4 + type] + " - " + str(count) + " WHERE " + columns[0] + " = " + str(chat_id) + " AND " + columns[1] + " = " + str(Distributor_id))
    db_connection.commit()
def checkYourStat(chat_id, user_id, msg_id):
    mycursor.execute("SELECT * FROM UsersPlastic WHERE " + columns[0] + " = " + str(chat_id) + " AND " + columns[1] + " = " + str(user_id))
    result = mycursor.fetchall()
    bot.sendMessage(chat_id, "你今日淨" + str(result[0][6]) + "杯酒" + str(result[0][5]) + "粒膠\n 喺度收過" + str(result[0][4]) + "杯酒" + str(result[0][3]) + "粒膠", None, None, None, msg_id)
def groupStat(chat_id, msg_id):
    mycursor.execute("SELECT * FROM UsersPlastic WHERE " + columns[0] + " = " + str(chat_id) + " AND " + columns[4] + " > 0 ORDER BY " + columns[4] + " DESC LIMIT 5")
    result1 = mycursor.fetchall()
    mycursor.execute("SELECT * FROM UsersPlastic WHERE " + columns[0] + " = " + str(chat_id) + " AND " + columns[3] + " > 0 ORDER BY " + columns[3] + " DESC LIMIT 5")
    result2 = mycursor.fetchall()
    result1_done = ""
    for i in range(min(len(result1), 5)):
        result1_done += '\n' + bot.getChatMember(chat_id, result1[i][1])['user']['first_name'] + '有' + str(result1[i][4]) + '杯酒'
    result2_done = ""
    for i in range(min(len(result2), 5)):
        result2_done += '\n' + bot.getChatMember(chat_id, result2[i][1])['user']['first_name'] + '有' + str(result2[i][3]) + '粒膠'
    bot.sendMessage(chat_id, "喺呢個群收過最多酒嘅" + str(len(result1)) + "個人：" + result1_done + "\n喺呢個群收過最多膠嘅" + str(len(result2)) + "個人：" + result2_done, None, None, None, msg_id)
def badRequests(chat_id, msg_id):
    bot.sendMessage(chat_id, '請輸入一個最小為1最大為100的整數', None, None, None, msg_id)
bot.message_loop({'chat': handle, 'callback_query': handle2}, timeout = 100)
schedule.every().day.at("16:00").do(ResetPlastic)
#print(1)
while True:
    schedule.run_pending()
    bot.kickChatMember(-1001188563796, 1065532169)
    #bot.sendChatAction(fargp, "typing")
    time.sleep(10)

#print(time.time())
#maxid = 337690936
#fourierid = 199823643
#aecomchat: -391498384
