import xbmcaddon
import xbmcgui
import urllib2
import base64
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

myurl = addon.getSetting('hostname') 
if myurl == "" :
      keyboard = xbmc.Keyboard("","HostName")
      keyboard.doModal()
      if (keyboard.isConfirmed()):
         myurl = keyboard.getText()
         addon.setSetting("hostname", myurl)

username = addon.getSetting('username') 
if username == "" :
      keyboard = xbmc.Keyboard("","Username")
      keyboard.doModal()
      if (keyboard.isConfirmed()):
         username = keyboard.getText()
         addon.setSetting("username", username)
         
password =  addon.getSetting('password') 
if password == "" :
      keyboard = xbmc.Keyboard("","Password")
      keyboard.setHiddenInput(True)
      keyboard.doModal()
      if (keyboard.isConfirmed()):
         password = keyboard.getText()
         addon.setSetting("password", password)

web_page = urllib2.urlopen("http://iptools.bizhat.com/ipv4.php")
myip = web_page.read()
#toshow = "IP actual : " + myip + "\n"

update_url = "https://dynupdate.no-ip.com/nic/update?hostname=" + myurl + "&myip=" + myip

req = urllib2.Request(update_url)
req.add_header('Authorization', 'Basic '+base64.encodestring(username+":"+password).replace("\n",""))
resp = urllib2.urlopen(req)
content = resp.read()
#xbmcgui.Dialog().ok(addonname,toshow+" Respuesta de no-ip: "+content) 

time = 5000 #in miliseconds
__icon__ = addon.getAddonInfo('icon')
xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(addonname," "+content, time, __icon__))
