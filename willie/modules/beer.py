from willie import module



@module.commands('beer')
def beer(bot, trigger):
    bot.action('Gives a beer to ' + trigger.nick)
