# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from io import StringIO
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,sys
import re,string,os
import os.path,sys,urllib,shutil,subprocess

cl = LINETCR.LINE()
#cl.login(qr=True)
cl.login(token="EonP24ckSJ00yPeZYKp7.QTjneaJ3YUJ4UnQPQrKYTW.THlUmCWKu8DkDVw8ngFwwn5e1Yq6XaAhB3asmx39sVE=")
cl.loginResult()

#ki = LINETCR.LINE()
#ki.login(qr=True)
#ki.loginResult()

#kk = LINETCR.LINE()
#kk.login(qr=True)
#kk.loginResult()  

#ks = LINETCR.LINE() 
#ks.login(qr=True)
#ks.loginResult()  

#ka = LINETCR.LINE() 
#ka.login(qr=True)
#ka.loginResult()    

#kc = LINETCR.LINE() 
#kc.login(qr=True)
#kc.loginResult()    

        
print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')
helpMessage ="""
�w�w?��?===========?��?�w�w
        [By.???????????]
          [By.????????????]
�w�w?��?===========?��?�w�w
��������������������������������������
��???????????????
��������������������������������������
��???��?  id 
��???��?  Mid
��???��?  All mid:
��???��?  Me 
��???��?  All mid
��???��?  [K1/K2/K3/]: "Contact"
��???��?  [K1/K2/K3 fuck:]: "Kick kicker"
��???��?  [Group Id]: "Id Me Group"
��???��?  [TL : "Text"]: "Auto status TL"
��???��?  [Clock :]: "Name Clock"
��???��?  Set
��???��?  [Up clock]: "Up date Clock"
��???��?  [Name : 'text']: "Name me"
��???��?  MIC]: "mid"]: "Contact share"
��???��?  [Massage add: "text"]: 
��???��?  [Add confirmasi]: 
��???��?  [Comment set : "Text"]:
��???��?  [Comment check]: 
��???��?  [Clock: on]: "Clock name on"
��???��?  [Clock: off]: "Clock name off"
��???��?  [Ban]: "Add blacklist"
��???��?  Unban]: "Dalate blacklist"
��???��?  [Banlist]: "Check blacklist"
��???��?  [Kicker join]
��???��?  Kick
��???��?  [Contact: on/off]: 
��???��?  [Auto join: on/off]: 
��???��?  [Cancel Invite: 1 on/off]:
��???��?  [Auto share: on/off]:
��???��?  Speed / Sp
��???��?  [Auto leave: on/off]: 
��???��?  [Comment: on/off]: 
��???��?  [Auto add: on/off]: 
��???��?  [Auto like: on/off]: 
��???��?  [Ban " @Tag]: 
��???��?  [Unban " @Tag]: 
��???��?  [Urlon]: "Open urL"
��???��?  [Urloff]: "Closed urL"
��???��?  [Url]: " Check urL room"
��???��?  [Ginfo]: "~÷~ data room"
��???��?  [Invite: "mid"]: 
��???��?  [Cancel]: "Cancel invite"
��???��?  [Gn: "name"]: "Change name Group"
��������������������������������������
"""
helpMessage2 ="""?�Ť�??? βǾŦ ?��??�ាத�?ય�??�ຮี✨

??[ƤƦ?Ƭ??Ƭ: ??/???]: 
??[?Լ??? ƲƦԼ: ??/???]: 
??[??M?Լ???: ??/???]: 
??[?Լ???????Ƭ?: ??/???]:  
	
"""
KAC = [cl]
mid = cl.getProfile().mid
#Amid = ki.getProfile().mid
#kimid = kk.getProfile().mid
#ki2mid = ks.getProfile().mid
#Cmid = kc.getProfile().mid
#Emid = ka.getProfile().mid
admin = ["ua1cb6e845fe8f2646fe8a5c598a5c5911841fa"]
me = cl.getProfile().mid
bot1 = cl.getProfile().mid
main = cl.getProfile().mid
#kicker1 = ki.getProfile().mid
#bots = me + kicker1
protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []

admins = ["ua1cb6e845fe8f2646fe8a5c598a5c5911841fa"]
Rx5 = ["u2adff56ccc44b3c95d11e9de29ee671e"]
Rx4 = ["u4405cf1ff24a7e453def401c02d97cb2"]
Rx3 = ["u794e8ec978df6e5b39f83c42a4127458"]
Rx2 = ["uf7246b72a33cb043eec99b0c20defd2e"]
Rx1 = ["ucd8eab17148199e104a1da913bc30b51"]
Administrator = admins + Rx5 + Rx4 + Rx3 + Rx2 + Rx1
AS = Rx2 + Rx1 + Rx3 + Rx4 + Rx5
adminsA = admins + Rx3 + Rx5

omikuzi = ["大�?","中�?","小�?","?��?","大凶","??1?7"]

wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"off":False,"members":50},
    'leaveRoom':False,
    'timeline':False,
    'autoAdd':False,
    'message':"แอดมารั�?หรือแอดมารั�?ครั�?",
    "lang":"JP",
    "comment":"Auto like By.?�Ŧ�?�ℳ???��??�ាத�?ય�??�ຮี✨ ",
    "likeOn":False,
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "blacklist":{}, 
    "wblacklist":False,
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},    
    "dblacklist":False
}

wait2 = {
	'readMember':{},
	'readPoint':{},
	'ROM':{},
	'setTime':{}
    }
	
setTime = {}
setTime = wait2["setTime"]

res = {
    'num':{},
    'us':{},
    'au':{},
}

def Cmd(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = [""]
    for texX in tex:
        for command in commands:
            if string ==texX + command:
                return True
    return False
    
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
         
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    kk.cancelGroupInvitation(op.param1, matched_list)
                    ks.cancelGroupInvitation(op.param1, matched_list)
                    ka.cancelGroupInvitation(op.param1, matched_list)
                    kc.cancelGroupInvitation(op.param1, matched_list)
                      
        if op.type == 17:
            if mid in op.param3:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist user flushing is complete")

        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                        except:
                            try:
                                G = kk.getGroup(op.param1)
                            except:
                                try:
                                    G = ks.getGroup(op.param1)
                                except:
                                    try:
                                        G = ki.getGroup(op.param1)
				    except:
					try:
                                            G = kc.getGroup(op.param1)
                                        except:
                                            pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                kk.updateGroup(G)
                            except:
                                try:
                                    ks.updateGroup(G)
                                except:
                                    try:
                                        kc.updateGroup(G)
                                    except:
                                        try:
                                            ka.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in ken:
                        pass
                    else:
                        try:
                            koutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ka.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ks.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                        cl.sendText(op.param1,"Group name lock")
                                        ki.sendText(op.param1,"Haddeuh dikunci Pe'a")
                                        kk.sendText(op.param1,"Wekawekaweka ????Har Har?��")
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
		if op.type == 17:
			if mid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2])
                                        ka.kickoutFromGroup(op.param1,[op.param2])
                                        kc.kickoutFromGroup(op.param1,[op.param2])
		if op.type == 32:
			if mid in op.param3:
				wait["blacklist"][op.param2] == True
		if op.type == 32:
			if mid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2])
                                        ka.kickoutFromGroup(op.param1,[op.param2])
                                        kc.kickoutFromGroup(op.param1,[op.param2])
		if op.type == 25:
			if mid in op.param3:
				wait["blacklist"][op.param2] == True
		if op.type == 25:
			if mid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2])
                                        ka.kickoutFromGroup(op.param1,[op.param2])
                                        kc.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.param3 == "4":
            if op.param1 in protecturl:
				group = cl.getGroup(op.param1)
				if group.preventJoinByTicket == False:
					group.preventJoinByTicket = True
					cl.updateGroup(group)
					cl.sendText(op.param1,"URL can not be changed")
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2])
                                        ka.kickoutFromGroup(op.param1,[op.param2])
                                        kc.kickoutFromGroup(op.param1,[op.param2])
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
				else:
					pass                
        if op.type == 26:
            msg = op.message
            if msg.toType == 26:
                msg.to = msg.from_
                if msg.from_ == "u41d44401392c18e87311e98ee8c278a2":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            ki.acceptGroupInvitationByTicket(list_[1],list_[2])
                            kk.acceptGroupInvitationByTicket(list_[1],list_[2])
                            ka.acceptGroupInvitationByTicket(list_[1],list_[2])
                            kc.acceptGroupInvitationByTicket(list_[1],list_[2])
                            ks.acceptGroupInvita		
                            X = cl.getGroup(list_[1])
                            X = ki.getGroup(list_[1])
                            X = kk.getGroup(list_[1])
                            X = ks.getGroup(list_[1])							
                            X = ka.getGroup(list_[1])
                            X = kc.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                            ki.updateGroup(X)
                            kk.updateGroup(X)
                            ks.updateGroup(X)							
                            ka.updateGroup(X)
                            kc.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1002)                    
        if op.type == 26:
            msg = op.message
            if msg.contentType == 26:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"It's included in a blacklist already??1?7")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"I decided not to make a comment??1?7")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"It was eliminated from a blacklist??1?7")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It isn't included in a blacklist??1?7")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"It's included in a blacklist already.??1?7")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"It was added to the blacklist.??1?7")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"It was eliminated from a blacklist??1?7")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It isn't included in a blacklist??1?7")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["help","Help","HELP"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["key","Key","KEY"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage2)
                else:
                    cl.sendText(msg.to,helpt)
            elif ("Gn:"in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn:","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("ki1 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("ki1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("ki2 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("ki2 gn ","")
                    ki2.updateGroup(X)
                else:
                    ki2.sendText(msg.to,"It can't be used besides the group.")
            elif "kick:" in msg.text:
                midd = msg.text.replace("kick:","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Invite:" in msg.text:
                midd = msg.text.replace("Invite:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif "K1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
            elif "K2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                kk.sendMessage(msg)
            elif "K3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ks.sendMessage(msg)    
            elif "K4" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
            elif "K5" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                ka.sendMessage(msg)
            elif msg.text in ["Gift","แ�?�?"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["?�の?�レ?�ン??1?7","K1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["?�の?�レ?�ン??1?7","K2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                kk.sendMessage(msg)
            elif msg.text in ["?�の?�レ?�ン??1?7","K3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ks.sendMessage(msg)
            elif msg.text in ["?�の?�レ?�ン??1?7","K4 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                kc.sendMessage(msg)
            elif msg.text in ["?�の?�レ?�ン??1?7","K5 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ka.sendMessage(msg)
            elif msg.text in ["cancel","Cancel"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"There isn't an invited person??1?7")
                        else:
                            cl.sendText(msg.to,"you Sato face-like person absence??1?7")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can't be used besides the group??1?7")
                    else:
                        cl.sendText(msg.to,"Impossible use besides")

            elif msg.text in ["K1 cancel"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"There isn't an invited person??1?7")
                        else:
                            ki.sendText(msg.to,"you Sato face-like person absence??1?7")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can't be used besides the group??1?7")
                    else:
                        cl.sendText(msg.to,"Impossible use besides")
                        
            elif "Comment set:" in msg.text:
                c = msg.text.replace("Comment set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Error")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"It was changed?�\n\n" + c)
            elif msg.text in ["Comment check"]:
                cl.sendText(msg.to,"An automatic comment is established as follows at present?�\n\n" + str(wait["comment"]))
            elif msg.text in ["?�メ?��?:?�ン","Comment:on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done??1?7")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already??1?7")
            elif msg.text in ["?�メ?��?:?��?","Comment:off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done??1?7")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already??1?7")          
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Block url:on"]:
                protecturl.append(msg.to)
                cl.sendText(msg.to,"????")
            elif msg.text in ["Block url:off"]:
                if msg.from_ in Administrator:
                    protecturl.remove(msg.to)
                    cl.sendText(msg.to,"?ԼԼ????")
                else:
                    cl.sendText(msg.to,"?ԼƦ???Ƴ")
            elif msg.text in ["Urlon"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƲƦԼ ?? ?ԼƦ???Ƴ??1?7")
                    else:
                        cl.sendText(msg.to,"?ԼƦ???Ƴ ƲƦԼ??")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can't be used besides the group??")
                    else:
                        cl.sendText(msg.to,"Impossible use besides")
            elif msg.text in ["Urloff"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƲƦԼ ?Լ?Ƨ????")
                    else:
                        cl.sendText(msg.to,"?ԼƦ???Ƴ ƲƦԼ??")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can't be used besides the group??")
                    else:
                        cl.sendText(msg.to,"Impossible use besides")
            elif msg.text in ["ginfo","Ginfo"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "refusal"
                        else:
                            u = "許可"
                        cl.sendText(msg.to,"[?Ʀ?ƲƤ]\n" + str(ginfo.name) + "\n\n[???]\n" + msg.to + "\n\n[?Ʀ?ƲƤ ?Ʀ??Ƭ?Ʀ]\n" + gCreator + "\n\n[ƤƦ???Լ ?Ʀ?ƲƤ]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nM?M??Ʀ:" + str(len(ginfo.members)) + "Person\n????Ƭ?:" + sinvitee + "Person\n????Ƭ?Ƭ??? ƲƦԼ:" + u + "?Ƭ'Ƨ ƬH? ??Ƨ???.")
                    else:
                        cl.sendText(msg.to,"[?��?]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[小�??��??�者]\n" + gCreator + "\n[小�??��?]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can't be used besides the group??")
                    else:
                        cl.sendText(msg.to,"Impossible use besides")
            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif "Mid" == msg. text:
                cl.sendText(msg.to,mid)
            elif "All mid" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,kimid)
                ks.sendText(msg.to,ki2mid)      
                ka.sendText(msg.to,Cmid)
                kc.sendText(msg.to,Emid)
            elif "Wkwk" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ks.sendMessage(msg)
            elif "Sue" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "105",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ks.sendMessage(msg)
            elif "Welcome" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ks.sendMessage(msg)
            elif "TL:" in msg.text:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Name:" in msg.text:
                string = msg.text.replace("Name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"The name " + string + " I did NI change??")
            elif "Last name" in msg.text:
                string = msg.text.replace("Last name","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"The name " + string + " I did NI change??")
#---------------------------------------------------------
            elif "K1 upname:" in msg.text:
                string = msg.text.replace("K1 up name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"The name " + string + " I did NI change??")
#--------------------------------------------------------
            elif "K2 upname:" in msg.text:
                string = msg.text.replace("K2 up name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = kk.getProfile()
                    profile.displayName = string
                    kk.updateProfile(profile)
                    kk.sendText(msg.to,"The name " + string + " I did NI change??")
#--------------------------------------------------------
            elif "K3 upname:" in msg.text:
                string = msg.text.replace("K3 up name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ks.getProfile()
                    profile.displayName = string
                    ks.updateProfile(profile)
                    ks.sendText(msg.to,"The name " + string + " I did NI change??")
#--------------------------------------------------------
            elif "K1 upstatus: " in msg.text:
                string = msg.text.replace("K1 upstatus: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile_B = ki.getProfile()
                    profile_B.statusMessage = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"display message " + string + " done")
            elif "K2 upstatus: " in msg.text:
                string = msg.text.replace("K2 upstatus: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile_C = kk.getProfile()
                    profile_C.statusMessage = string
                    kk.updateProfile(profile_C)
                    kk.sendText(msg.to,"display message " + string + " done")
            elif "K3 upstatus: " in msg.text:
                string = msg.text.replace("K3 upstatus: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile_C = ks.getProfile()
                    profile_C.statusMessage = string
                    ks.updateProfile(profile_C)
                    ks.sendText(msg.to,"display message " + string + " done")
            elif "Mic:" in msg.text:
                mmid = msg.text.replace("Mic:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Contact:on"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"???Ƭ??Ƭ ?? ?ԼƦ???Ƴ??")
                    else:
                        cl.sendText(msg.to,"?ԼƦ???Ƴ ????")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"?Ƭ ??Ƨ ƬƲƦ??? ????")
                    else:
                        cl.sendText(msg.to,"ƬƲƦ??? ????")
            elif msg.text in ["Contact:off"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"???Ƭ??Ƭ ??? ?ԼƦ???Ƴ??")
                    else:
                        cl.sendText(msg.to,"?ԼƦ???Ƴ ?????")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"?Ƭ ??Ƨ ƬƲƦ??? ?????")
                    else:
                        cl.sendText(msg.to,"ƬƲƦ??? ?????")
            elif msg.text in ["Auto join:on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"???? ?? ?ԼƦ???Ƴ??")
                    else:
                        cl.sendText(msg.to,"?ԼƦ???Ƴ ????")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"?Ƭ ??Ƨ ƬƲƦ??? ????")
                    else:
                        cl.sendText(msg.to,"ƬƲƦ??? ????")
            elif msg.text in ["Auto join:off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"???? ??? ?ԼƦ???Ƴ??")
                    else:
                        cl.sendText(msg.to,"?ԼƦ???Ƴ ?????")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"?Ƭ ??Ƨ ƬƲƦ??? ?????")
                    else:
                        cl.sendText(msg.to,"ƬƲƦ??? ?????")
            elif "Cancel invite:" in msg.text:
                try:
                    strnum = msg.text.replace("Cancel invite:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refusal was turned off?�\non, please designate and send the number of people.")
                        else:
                            cl.sendText(msg.to,"number of people")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "A group below the person made sure that I'll refuse invitation automatically??")
                        else:
                            cl.sendText(msg.to,strnum + "Self- you for below shinin-like small.")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"The price is wrong??")
                    else:
                        cl.sendText(msg.to,"key is wrong??")
            elif msg.text in ["Auto leave:on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Լ???? ?? ?ԼƦ???Ƴ??")
                    else:
                        cl.sendText(msg.to,"?ԼƦ???Ƴ ????")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"?Ƭ ??Ƨ ƬƲƦ??? ????")
                    else:
                        cl.sendText(msg.to,"ƬƲƦ??? ????")
            elif msg.text in ["Auto leave:off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Լ???? ??? ?ԼƦ???Ƴ??")
                    else:
                        cl.sendText(msg.to,"?ԼƦ???Ƴ ?????")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"?Ƭ ??Ƨ ƬƲƦ??? ?????")
                    else:
                        cl.sendText(msg.to,"ƬƲƦ??? ?????")
            elif msg.text in ["?��?:?�ン","?��?：オ??","Auto share:on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"?ԼƦ???Ƴ ??")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"Already??")
            elif msg.text in ["?��?:?��?","?��?：オ??","Auto share:off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"?ԼƦ???Ƴ ???")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"Already??")                        
            elif "Set" == msg.text:
                md = ""
                if wait["contact"] == True: md+="?? Contact ?? on \n"       
                else: md+="?? Contact ?? off \n"      
                if wait["autoJoin"] == True: md+="??  Auto join ?? on \n" 
                else: md +="?? Auto join ?? off \n"
                if wait["autoCancel"]["on"] == True:md+="?? Cancel Invite ?? " + str(wait["autoCancel"]["members"]) + " \n"     
                else: md+= "?? Cancel Invite ?? off \n"  
                if wait["leaveRoom"] == True: md+="?? Auto leave ?? on \n"   
                else: md+="?? Auto leave ?? off \n"
                if wait["timeline"] == True: md+="?? Auto Share ?? on \n"  
                else:md+="?? Auto Share ?? off \n" 
                if wait["commentOn"] == True: md+="?? Comment ?? on \n"   
                else:md+="?? Comment ?? off \n"    
                if wait["autoAdd"] == True: md+="?? Auto add ?? on \n"  
                else:md+="?? Auto add ?? off \n"   
                if wait["likeOn"] == True: md+="?? Auto like ?? on \n"
                else:md+="?? Auto like ?? off \n" 
                cl.sendText(msg.to,md)
            elif msg.text in ["Group id","group id"]:
                gid = cl.getGroupIdsJoined()
                g = ""
                for i in gid:
                    g += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,g)
            elif msg.text in ["ล�?�?���?"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Completion??")
                else:
                    cl.sendText(msg.to,"key is wrong??")
            elif msg.text in ["Auto like:on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done??")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already??")
            elif msg.text in ["?��???:?��?","Auto like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done??")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already??")

            elif msg.text in ["Auto add:on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It's on already??")
                    else:
                        cl.sendText(msg.to,"on already??")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It was turned on??")
                    else:
                        cl.sendText(msg.to,"Turned on??")
            elif msg.text in ["Auto add:off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It's off already??")
                    else:
                        cl.sendText(msg.to,"off already??")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It was turned off??")
                    else:
                        cl.sendText(msg.to,"Turned off??")
            elif "Massage add:" in msg.text:
                wait["message"] = msg.text.replace("Massage add:","")
                cl.sendText(msg.to,"The message was changed??")
            elif "Auto addition??" in msg.text:
                wait["message"] = msg.text.replace("Auto addition??","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"The message was changed??")
                else:
                    cl.sendText(msg.to,"was change already??")
            elif msg.text in ["Add confirmasi","?��?追�??�候�?確�?"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,".automatic message is established as follows?�\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"One  of weeds on the surface below the self- additional breath image?�\n\n" + wait["message"])
            elif msg.text in ["CHANGE","言語�???"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"??Ʋ?ƬƦƳ Լ???Ʋ??? ?ƲƦ??? ? ?H??????")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,". The language was made English??")
            elif msg.text in ["Url"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"?Ƭ ???'Ƭ ?? ƲƧ?? ??Ƨ???Ƨ ƬH? ?Ʀ?ƲƤ.??")
                    else:
                        cl.sendText(msg.to,"?MƤ?ƧƧ??Լ? ƲƧ? ??Ƨ???Ƨ ƬH? ?Ʀ?ƲƤ. ")
            elif "gurl:" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl:","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"?Ƭ ???'Ƭ ?? ƲƧ?? ??Ƨ???Ƨ ƬH? ?Ʀ?ƲƤ??")
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = ki.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"??? ??Ƭ ?? ƲƧ?? ?ƲƬƧ??? ƬH? ?Ʀ?ƲƤ")
                    else:
                        cl.sendText(msg.to,"??Ƭ ??Ʀ ƲƧ? Լ?ƧƧ ƬH?? ?Ʀ?ƲƤ")
            elif msg.text in ["cb"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send the phone number of the person who adds it to the blacklist.")
            elif msg.text in ["cbd"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send the phone number of the person who adds it to the blacklist.")
            elif msg.text in ["cbc"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"There isn't a person made a blacklist??")
                else:
                    cl.sendText(msg.to,"Below is a blacklist??")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "??" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Clock:on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"It's on already??")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"It was turned on")
            elif msg.text in ["Clock:off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"It's off already.??")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"It was tuned off??")
            elif "Clock:" in msg.text:
                n = msg.text.replace("Clock:","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"Last name clock??")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"It was renewed\n\n" + n)
            elif msg.text in ["Up clock"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"It was renewed??")
                else:
                    cl.sendText(msg.to,"Please turn on a name clock.??")
            elif "แ�?�?" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg) 
            elif "�?���?" in msg.text:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  ks.acceptGroupInvitationByTicket(msg.to,Ti)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  ka.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
            elif msg.text in ["K1 join"]:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)                  
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["K2 join"]:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)           
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kk.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)
				  
            elif msg.text in ["K3 join"]:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  ks.acceptGroupInvitationByTicket(msg.to,Ti)           
                  G = ks.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ks.updateGroup(G)
                  Ticket = ks.reissueGroupTicket(msg.to)                           

            elif msg.text in ["Bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
					ki.leaveGroup(msg.to)
					kk.leaveGroup(msg.to)
					ks.leaveGroup(msg.to)
					kc.leaveGroup(msg.to)
					ka.leaveGroup(msg.to)
                except:
                     pass            
            elif "NK:" in msg.text:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("NK:","")
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                KAC = [ki,kk,ks,kc,ka]
                                kicker = random.choice(KAC)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg.to,"?ƦƦ?Ʀ")
#-----------------------------------------------------------                          
            elif "Kick" in msg.text:
                if msg.contentMetadata is not None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                           ki.kickoutFromGroup(msg.to,[target])
                    else:
                        pass
            elif "K1 fuck" in msg.text:
				OWN = "u406133ad4d3fbe50a2f4d51ea081d050"
				if msg.from_ in OWN:
					pass
				else:
					nk0 = msg.text.replace("K1 fuck","")
					nk1 = nk0.lstrip()
					nk2 = nk1.replace("@","")
					nk3 = nk2.rstrip()
					_name = nk3
					gs = ki.getGroup(msg.to)
					targets = []
					for h in gs.members:
						if _name in h.displayName:
							targets.append(h.mid)
					if targets == []:
						sendMessage(msg.to,"ƲƧ?Ʀ ???Ƨ ??Ƭ ?Ҳ?ƧƬ")
						pass
					else:
						for target in targets:
							try:
								if msg.from_ not in target:
									ki.kickoutFromGroup(msg.to, [target])							   
							except:
									ki.kickoutFromGroup(msg.to, [target])							   
									pass
            elif "K2 fuck" in msg.text:
				OWN = "ua51ba06b0dd18c0bfe2cc6caa3458202"
				if msg.from_ in OWN:
					pass
				else:
					nk0 = msg.text.replace("K2 fuck","")
					nk1 = nk0.lstrip()
					nk2 = nk1.replace("@","")
					nk3 = nk2.rstrip()
					_name = nk3
					gs = ki.getGroup(msg.to)
					targets = []
					for h in gs.members:
						if _name in h.displayName:
							targets.append(h.mid)
					if targets == []:
						sendMessage(msg.to,"ƲƧ?Ʀ ???Ƨ ??Ƭ ?Ҳ?ƧƬ")
						pass
					else:
						for target in targets:
							try:
								if msg.from_ not in target:
									kk.kickoutFromGroup(msg.to, [target])							   
							except:
									kk.kickoutFromGroup(msg.to, [target])							   
									pass

            elif "K3 fuck" in msg.text:
				OWN = "u34a9af3a18784280147fc413a68a77fd"
				if msg.from_ in OWN:
					pass
				else:
					nk0 = msg.text.replace("K3 fuck","")
					nk1 = nk0.lstrip()
					nk2 = nk1.replace("@","")
					nk3 = nk2.rstrip()
					_name = nk3
					gs = ki.getGroup(msg.to)
					targets = []
					for h in gs.members:
						if _name in h.displayName:
							targets.append(h.mid)
					if targets == []:
						sendMessage(msg.to,"ƲƧ?Ʀ ???Ƨ ??Ƭ ?Ҳ?ƧƬ")
						pass
					else:
						for target in targets:
							try:
								if msg.from_ not in target:
									ks.kickoutFromGroup(msg.to, [target])							   
							except:
									ks.kickoutFromGroup(msg.to, [target])							   
									pass									
            elif "Ban " in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:                                        
                       ban0 = msg.text.replace("Ban ","")
                       ban1 = ban0.lstrip()
                       ban2 = ban1.replace("@","")
                       ban3 = ban2.rstrip()
                       _name = ban3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           cl.sendText(msg.to,"ƲƧ?Ʀ ???Ƨ ??Ƭ ?Ҳ?ƧƬ")
                           pass
                       else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"??( ^?^)�? ƧƲ???ƧƧ")
                                except:
                                    cl.sendText(msg.to,"??( ^?^)�? ƧƲ???ƧƧ")
#-----------------------------------------------------------"
#--------------------
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass

#-----------------------------------------------------------
            elif "Unban " in msg.text:
               if msg.toType == 2:
                  if msg.from_ in admin:                                        
                       unb0 = msg.text.replace("Unban ","")
                       unb1 = unb0.lstrip()
                       unb2 = unb1.replace("@","")
                       unb3 = unb2.rstrip()
                       x_name = unb3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if x_name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           cl.sendText(msg.to,"ƲƧ?Ʀ ???Ƨ ??Ƭ ?Ҳ?ƧƬ")
                           pass
                       else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"??( ^?^)�? ƧƲ???ƧƧ")
                                except:
                                    cl.sendText(msg.to,"??( ^?^)�? ƧƲ???ƧƧ")
#-----------------------------------------------------------
            elif "Protect:off" == msg.text:
				if msg.to in protection:
					cl.sendText(msg.to,"?ԼƦ???Ƴ ??")
				else:
					wait["pnharfbot"][msg.to] = cl.getGroup(msg.to).name
					f=codecs.open('pnharfbot.json','w','utf-8')
					json.dump(wait["pnharfbot"], f, sort_keys=True, indent=4,ensure_ascii=False)
					protection.append(msg.to)
					cl.sendText(msg.to,"ƬƲƦ??? ??")
            elif "Protect:on" == msg.text:
				try:
					if msg.from_ in Administrator:
						protection.remove(msg.to)
						cl.sendText(msg.to,"ƬƲƦ??? ???")
					else:
						cl.sendText(msg.to,"?ԼƦ???Ƴ ???")
				except:
					pass
            elif "Namelock:on" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ƬƲƦ??? ??.")
                else:
                    cl.sendText(msg.to,"?ԼƦ???Ƴ ??")
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
            elif "Namelock:off" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ƬƲƦ? ???.")
                    del wait['pname'][msg.to]
                else:
                    cl.sendText(msg.to,"?ԼƦ???Ƴ ???")
					
            elif "Blockinvite:on" == msg.text:
				gid = msg.to
				autocancel[gid] = "poni"
				cl.sendText(msg.to,"ƤƦ?Ƭ??Ƭ ????Ƭ?Ƭ??? ??")
            elif "Blockinvite:off" == msg.text:
				try:
					del autocancel[msg.to]
					cl.sendText(msg.to,"ƤƦ?Ƭ??Ƭ ????Ƭ?Ƭ??? ???")
				except:
					pass                                 
#-----------------------------------------------------------
            elif "#END" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------
            elif "Spam @" in msg.text:
                _name = msg.text.replace("Spam @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"?Ƭ? ƧƤ?M Ƭ?Ʀ??Ƭ ??")
                       ki.sendText(g.mid,"Spam  ??")  
                       kk.sendText(g.mid,"Spam  ??")  
                       ks.sendText(g.mid,"Spam  ??")
                       kc.sendText(g.mid,"Spam  ??")
                       ka.sendText(g.mid,"Spam  ??")
                       cl.sendText(g.mid,"Spam  ??")
                       ki.sendText(g.mid,"Spam  ??")
                       kk.sendText(g.mid,"Spam  ??")
                       ks.sendText(g.mid,"Spam  ??")
                       kc.sendText(g.mid,"Spam  ??")  
                       ka.sendText(g.mid,"Spam  ??")  
                       cl.sendText(g.mid,"Spam  ??")
                       ki.sendText(g.mid,"Spam  ??")
                       kk.sendText(g.mid,"Spam  ??")
                       ks.sendText(g.mid,"Spam  ??")
                       kc.sendText(g.mid,"Spam  ??")
                       ka.sendText(g.mid,"Spam  ??")
                       cl.sendText(g.mid,"Spam  ??")
                       ki.sendText(g.mid,"Spam  ??")  
                       kk.sendText(g.mid,"Spam  ??")  
                       ks.sendText(g.mid,"Spam  ??")
                       kc.sendText(g.mid,"Spam  ??")
                       ka.sendText(g.mid,"Spam  ??")
                       cl.sendText(g.mid,"Spam  ??")
                       ki.sendText(g.mid,"Spam  ??")
                       kk.sendText(g.mid,"Spam  ??")
                       ks.sendText(g.mid,"Spam  ??")
                       kc.sendText(g.mid,"Spam  ??")  
                       ka.sendText(g.mid,"Spam  ??")  
                       cl.sendText(g.mid,"Spam  ??")
                       ki.sendText(g.mid,"Spam  ??")
                       kk.sendText(g.mid,"Spam  ??")
                       ks.sendText(g.mid,"Spam  ??")
                       kc.sendText(g.mid,"H?H?H? ?? ƧƤ?M  ??")
                       ka.sendText(g.mid,"H?H?H? ?? ƧƤ?M  ??")
                       ks.sendText(g.mid,"H?H?H? ?? ƧƤ?M  ??")
                       cl.sendText(msg.to, "???? ƧƤ?M  ??")
                       print "Done spam" 
#-----------------------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
                ki.sendText(msg.to,"Ƥ??? ???��double thumbs up?��????Har Har?��")
                kk.sendText(msg.to,"Ƥ??? ???��double thumbs up?��????Har Har?��")
                ks.sendText(msg.to,"Ƥ??? ???��double thumbs up?��????Har Har?��")
                kc.sendText(msg.to,"Ƥ??? ???��double thumbs up��?1?7???Har Har�?1?7")
                ka.sendText(msg.to,"Ƥ??? ???��double thumbs up��?1?7???Har Har�?1?7")
#----------------------------------------------------------
            elif msg.text in ["Respon","respon","responsename"]:
                cl.sendText(msg.to,"???Ƭ?Ʀ ??Ʋ? ??Ƭ Լ??? ?.2 ????")
                ki.sendText(msg.to,"??Ƭ Լ??? 1")
                kk.sendText(msg.to,"??Ƭ Լ??? 2")
                ks.sendText(msg.to,"??Ƭ Լ??? 3")	
                kc.sendText(msg.to,"??Ƭ Լ??? 4")
                ka.sendText(msg.to,"??Ƭ Լ??? 5")
#----------------------------------------------------------
            elif msg.text == "มอ�?1?7":
              if msg.from_ in admin:
                cl.sendText(msg.to, "Ƨ?Ƭ ƬH? Լ?ƧƬƧ???Ƨ' Ƥ???Ƭ(�?1?7?�ω・´)")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
	            pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                wait2['ROM'][msg.to] = {}
                print wait2
            elif msg.text == "�?1?7ห�?�?1?7":
              if msg.from_ in admin:
		  if msg.to in wait2['readPoint']:
	            if wait2["ROM"][msg.to].items() == []:
	              chiya = ""
	            else:
	              chiya = ""
	              for rom in wait2["ROM"][msg.to].items():
	                print rom
	                chiya += rom[1] + "\n"

	            cl.sendText(msg.to, " %s\n\n\nPeople who have ignored reads\n(�?1?7?�ω・´)\n%s\n\nThese anu anu uesrs have seen at the lastseen point(�?1?7?�ω・´)\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
	          else:
	            cl.sendText(msg.to, "Sider ga bisa di read cek setpoint dulu bego tinggal ketik\nSetlastpoint\nkalo mau liat sider ketik\nViewlastseen")
#-----------------------------------------------------------speed
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"ƤԼ??Ƨ? Ƨ??? ƬH? ????Ʋ?Ƭ Ʀ???ƧƬ?Ʀ?? ??ƬH ? ?Լ???Լ?ƧƬ??1?7")
            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"ƤԼ??Ƨ? Ƨ??? ƬH? ????Ʋ?Ƭ Ʀ???ƧƬ?Ʀ?? ??ƬH ? ?Լ???Լ?ƧƬ??1?7")
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"ƬH?Ʀ? ?Ƨ?'Ƭ ? Ƥ?ƦƧ?? M??? ? ?Լ???Լ?ƧƬ.??1?7")
                else:
                    cl.sendText(msg.to,"??Լ?? ?Ƨ ? ?Լ???Լ?ƧƬ??1?7")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "??1?7" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Blist"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "??1?7" +cl.getContact(mm).displayName + "\n"
                    cl.sendText(msg.to,cocoa + "But it's a blacklist.??1?7")
            elif msg.text in ["Kill ban"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"There wasn't a blacklist user??1?7")
                        return
                    for jj in matched_list:
                        try:
                            klist=[cl,ki,kk,ks,kc,ka]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass							
            elif msg.text in ["single"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I have feigned and have canceled it??1?7")
            elif "random:" in msg.text:
                if msg.toType == 2:
                    strnum = msg.text.replace("random:","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"?ƦƦ?Ʀ")
            elif "Album making" in msg.text:
                try:
                    albumtags = msg.text.replace("Album making","")
                    gid = albumtags[:33]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "An album was made??1?7")
                except:
                    cl.sendText(msg.to,"?ƦƦ?Ʀ")
            elif "fakec??1?7" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    amid = msg.text.replace("fakec??1?7","")
                    cl.sendText(msg.to,str(cl.channel.createAlbumF(msg.to,name,amid)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass                
#-----------------------------------------------
            elif "Say " in msg.text:
                string = msg.text.replace("Say ","")
                if len(string.decode('utf-8')) <= 50:
                    ki.sendText(msg.to," " + string + " ")
                    kk.sendText(msg.to," " + string + " ")
                    ks.sendText(msg.to," " + string + " ")
                    kc.sendText(msg.to," " + string + " ")
                    ka.sendText(msg.to," " + string + " ")
#-----------------------------------------------
            elif "#test" in msg.text:
                ks.sendText(msg.to,"ok")
#-----------------------------------------------
            elif "Speed" in msg.text:
                start = time.time()
                cl.sendText(msg.to, "????ƧƧ ƧƤ??? ???Ƭ???")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))    
#-----------------------------------------------             
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)                        
                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = False

                elif op.param3 in op.param3:
                    if op.param1 in protection:
                        OWN = "u41d44401392c18e87311e98ee8c278a2","u2adff56ccc44b3c95d11e9de29ee671e","u4405cf1ff24a7e453def401c02d97cb2","u794e8ec978df6e5b39f83c42a4127458","uf7246b72a33cb043eec99b0c20defd2e","ucd8eab17148199e104a1da913bc30b51"
                    if op.param2 in OWN:
                        kicker1 = [cl,ki,kk,ks,kc,ka,km,kn,ko]
                        G = random.choice(kicker1).getGroup(op.param1)
                        G.preventJoinByTicket = False
                        random.choice(kicker1).updateGroup(G)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(kicker1).updateGroup(G)
                    else:
                        G = random.choice(kicker1).getGroup(op.param1)

                        random.choice(kicker1).kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        random.choice(kicker1).updateGroup(G)
                        Ticket = random.choice(kicker1).reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(kicker1).updateGroup(G)

                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        
                elif op.param3 in Amid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        cl.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)            
            except:
                pass

        if op.type == 19:
            try:
                if op.param3 in Amid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        cl.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)


                elif op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)            
            except:
                pass
                
        if op.type == 19:
            try:
                if op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ks.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)
                    else:
                        G = ks.getGroup(op.param1)

                        
                        ks.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)

                        
                elif op.param3 in Amid:
                    if op.param2 in kimid:
                        G = kk.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)

                        kk.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)            
            except:
                pass
                
        if op.type == 19:
            try:
                if op.param3 in ki2mid:
                    if op.param2 in kimid:
                        if op.param4 in Cmid:
                            if op.param5 in Emid:
                                G = kk.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)

                        
                        kk.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)


                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ks.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)
                    else:
                        G = ks.getGroup(op.param1)

                        
                        ks.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)            
            except:
                pass
                
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in ki2mid:
                        G = ks.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)
                    else:
                        G = ks.getGroup(op.param1)

                        
                        ks.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)

                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        
                elif op.param3 in ki2mid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        cl.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)            
            except:
                pass
             
        if op.param3 == "1":
            if op.param1 in protectname:
                group = cl.getGroup(op.param1)
                try:
					group.name = wait["pro_name"][op.param1]
					cl.updateGroup(group)
					cl.sendText(op.param1, "Groupname protect now")
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except Exception as e:
                    print e
                    pass
                    
        if op.param1 in autocancel:
			OWN = "ua7fc5964d31f45ac75128fc2b8deb842","u406133ad4d3fbe50a2f4d51ea081d050","ua51ba06b0dd18c0bfe2cc6caa3458202","uc7f32bb28dc009916d40af87c9910ddc"
			if op.param2 in OWN:
				pass
			else:
				Inviter = op.param3.replace("",',')
				InviterX = Inviter.split(",")
				contact = cl.getContact(op.param2)
				cl.cancelGroupInvitation(op.param1,InviterX)
				ki.cancelGroupInvitation(op.param1,InviterX)
				kk.cancelGroupInvitation(op.param1,InviterX)
				ks.cancelGroupInvitation(op.param1,InviterX)
				kc.cancelGroupInvitation(op.param1,InviterX)
				ka.cancelGroupInvitation(op.param1,InviterX)
				cl.kickoutFromGroup(op.param1,[op.param2])
				ki.kickoutFromGroup(op.param1,[op.param2])
				kk.kickoutFromGroup(op.param1,[op.param2])
				ks.kickoutFromGroup(op.param1,[op.param2])
				kc.kickoutFromGroup(op.param1,[op.param2])
				ka.kickoutFromGroup(op.param1,[op.param2])
				wait["blacklist"][op.param2] = True
				f=codecs.open('st2__b.json','w','utf-8')
				json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#------------------------------------------------------------------------------------
        if op.type == 32:
			OWN = "ua7fc5964d31f45ac75128fc2b8deb842","u406133ad4d3fbe50a2f4d51ea081d050","ua51ba06b0dd18c0bfe2cc6caa3458202","uc7f32bb28dc009916d40af87c9910ddc"
			if op.param2 in OWN:
				pass
			else:
				Inviter = op.param3.replace("",',')
				InviterX = Inviter.split(",")
				contact = cl.getContact(op.param2)
				ki.kickoutFromGroup(op.param1,[op.param2])
				kk.kickoutFromGroup(op.param1,[op.param2])
				ks.kickoutFromGroup(op.param1,[op.param2])
				kc.kickoutFromGroup(op.param1,[op.param2])
				ka.kickoutFromGroup(op.param1,[op.param2])
				wait["blacklist"][op.param2] = True
				f=codecs.open('st2__b.json','w','utf-8')
				json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#------------------------------------------------------------------------------------
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n??" + Name
                        wait2['ROM'][op.param1][op.param2] = "??" + Name
                else:
                    cl.sendText
            except:
                  pass
                  
#-----------------------------------------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def autoSta():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
#----------------------------------------

#-------------------------------
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
