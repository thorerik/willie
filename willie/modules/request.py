# coding=utf8

from __future__ import unicode_literals
from willie.module import commands
import urllib
import urllib2

@commands('request')
def request(bot, trigger):
    """Request Bot"""
#    bot.say('debug: ' + trigger.group(2))
    song = urllib.urlencode({'name': 'IRC User: ' + trigger.nick, 'type': 'Song Request', 'request': trigger.group(2).encode('utf-8'), 'submit': 'Request'})
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    request = urllib2.Request('http://djweb.eurotruckradio.com/request.php', data=song)
    request.add_header('Application', 'x-www-form-urlencoded')
    request.get_method = lambda: 'POST'
    url = opener.open(request)
    bot.say('Thank you ' + trigger.nick + '! I got your request for ' + (trigger.group(2) + '.'))
