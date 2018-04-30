# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from threading import Thread
from googletrans import Translator


cl =LINETCR.LINE()
#cl.login(qr=True)
cl.login(token='Es8YO9N0su305mQPj0N9.KbMq4fWrhftskN0ZQrMcwq.SiA3gKB5duQ8Uehc9l+N66zU9CnsvfegjjxZ8gMXoLU=')
cl.loginResult()


print u"login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" 
/Y (ชื่อเพลง)
/sp
/ifconfig
/system
/cpu
/kernel
/พูด
/แปลงร่าง @
/กลับ
/แทค
"""

helo=""

KAC=[cl]
mid = cl.getProfile().mid
bot1 = cl.getProfile().mid
Bots = [mid]
admsa = "uca51afa767df87ba3705494b97c3355c"
admin = "uca51afa767df87ba3705494b97c3355c"

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False
	
            elif "/แทค" in msg.text:
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
					
                    except:
                        pass
						
            elif '/Y ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('/Y ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")
					
                    except:
                        pass
					
            elif msg.text in ["/Sp","/sp","/Speed"]:
                cl.sendText(msg.to, "Progress.......")
                start = time.time()
                time.sleep(0.001)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))    
                print "[Command]Speed palsu executed"
					
                    except:
                        pass
						
            elif msg.text.lower() == '/ifconfig':
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == '/system':
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == '/kernel':
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == '/cpu':
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
					
                    except:
                        pass

            elif "/พูด " in msg.text.lower():
                    query = msg.text.lower().replace("พูด ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'th', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithUrl(msg.to, mp3)

                    except:
                        pass						

            elif "/แปลงร่าง @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("/แปลงร่าง @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               cl.CloneContactProfile(target)
                               cl.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e
													
                    except:
                        pass
						
            elif msg.text in ["/กลับ"]:
                try:
                    cl.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    cl.sendText(msg.to, "Refreshed.")
                except Exception as e:
                    cl.sendText(msg.to, str(e))
            elif msg.text.lower()  == 'help':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)
    except Exception as error:
        print error
		
while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev,  5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
						