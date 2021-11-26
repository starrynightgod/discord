from discord.ext import commands
from core.classes import Cog_Extension
from core.time import time_info
from datetime import datetime,timedelta
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

onMessageUser = int()
def chonMessageUser(a):
    global onMessageUser
    onMessageUser = a

class event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self,msg):
        for attachment in msg.attachments:
            att_url = attachment.url
            att_size = attachment.size
        if self.bot.user in msg.mentions:
            await msg.add_reaction(self.bot.get_emoji(int(710157217948631085)))
        if '-setuserid' in msg.content:
            return
        #不是OWNER本人發送私人訊息的紀錄
        if str(msg.channel.type) == 'private' and msg.author != self.bot.user and msg.author.id != jdata['owner']:
            own = self.bot.get_user(jdata['owner'])
            try:
              print(time_info.UTC_8_CH() + str(msg.author) + '說：' + msg.content + att_url)
            except:
              print(time_info.UTC_8_CH() + str(msg.author) + '說：' + msg.content)
              print(time_info.UTC_8_CH() + str(msg.author) + '說：' + msg.content)
            if msg.author.id == onMessageUser:
                try:
                  if att_url.endswith(".jpg") or att_url.endswith(".jpeg") or att_url.endswith(".png") or att_url.endswith(".gif"):
                    await own.send(str(msg.content) + att_url)
                  else:
                    if att_size <= 1048576:
                      await own.send(str(msg.content) + att_url + '\n檔案大小：%.2f KB' % int(att_size/1024))
                    else:
                      await own.send(str(msg.content) + att_url + '\n檔案大小：%.2f MB' % int(att_size/1024/1024))
                except:
                    await own.send(str(msg.content))
                fp = open('./log/' + 'Private.log', 'a',encoding='utf8')
                try:
                  fp.write(time_info.UTC_8() + str(msg.author) + '說:' + msg.content + att_url +'\n')
                except:
                  fp.write(time_info.UTC_8() + str(msg.author) + '說:' + msg.content + '\n')
                fp.close()
            else:
                try:
                  if att_url.endswith(".jpg") or att_url.endswith(".jpeg") or att_url.endswith(".png") or att_url.endswith(".gif"):
                    await own.send(time_info.UTC_8_CH() + '［ID：'+str(msg.author.id)+'］' + str(msg.author) + '說：\n' + str(msg.content) + att_url)
                  else:
                    if att_size <= 1048576:
                      await own.send(time_info.UTC_8_CH() + '［ID：'+str(msg.author.id)+'］' + str(msg.author) + '說：\n' + str(msg.content) + att_url + '\n檔案大小：%.2f KB' % int(att_size/1024))
                    else:
                      await own.send(time_info.UTC_8_CH() + '［ID：'+str(msg.author.id)+'］' + str(msg.author) + '說：\n' + str(msg.content) + att_url + '\n檔案大小：%.2f MB' % int(att_size/1024/1024))
                    
                except:
                  await own.send(time_info.UTC_8_CH() + '［ID：'+str(msg.author.id)+'］' + str(msg.author) + '說：\n' + str(msg.content))
                chonMessageUser(msg.author.id)
                fp = open('./log/' + 'Private.log', 'a',encoding='utf8')
                try:
                  fp.write(time_info.UTC_8() + str(msg.author) + '說:' + msg.content + att_url + '\n')
                except:
                  fp.write(time_info.UTC_8() + str(msg.author) + '說:' + msg.content +'\n')
                fp.close()
        #DISCORD群內發訊息紀錄
        else:
            if str(msg.channel.type) == 'text' and msg.author != self.bot.user:
                try:
                  print(time_info.UTC_8_CH() + str(msg.author) + '說：' + msg.content  + att_url)
                except:
                  print(time_info.UTC_8_CH() + str(msg.author) + '說：' + msg.content)
                a = str(msg.guild)
                b = str(msg.channel)
                fp = open('./log/' + a + '-' + b + '.log', 'a',encoding='utf8')
                try:
                  fp.write(time_info.UTC_8() + str(msg.author) + '說:' + msg.content + att_url + '\n')
                except:
                  fp.write(time_info.UTC_8() + str(msg.author) + '說:' + msg.content + '\n')
                fp.close()
        #不是OWNER本人發送私人訊息的紀錄
        if str(msg.channel.type) == 'private' and msg.author != self.bot.user and msg.author.id == jdata['owner']:
            try:
              print(time_info.UTC_8_CH() + str(msg.author) + '說：' + msg.content + att_url)
            except:
              print(time_info.UTC_8_CH() + str(msg.author) + '說：' + msg.content)
            user = self.bot.get_user(int(onMessageUser))
            try:
              if att_url.endswith(".jpg") or att_url.endswith(".jpeg") or att_url.endswith(".png") or att_url.endswith(".gif"):
                    await user.send(msg.content + att_url)
              else:
                    if att_size <= 1048576:
                      await user.send(msg.content + att_url + '\n檔案大小：%.2f KB' % int(att_size/1024))
                    else:
                      await user.send(msg.content + att_url + '\n檔案大小：%.2f MB' % int(att_size/1024/1024))
            except:
              try:
                await user.send(msg.content)
              except:
                pass
            fp = open('./log/' + 'Private.log', 'a',encoding='utf8')
            try:
              fp.write(time_info.UTC_8() + str(msg.author) + '說:' + msg.content + att_url + '\n')
            except:
              fp.write(time_info.UTC_8() + str(msg.author) + '說:' + msg.content + '\n')
            fp.close()
        pass

    #設定要跟誰做聊天對象
    @commands.command(name='setuserid', aliases=['重設ID' , '重設用戶ID'], brief="admin", description=f"可以給自己設定id透過機器人直接與對方聊天(前提是機器人也要在同群組)\n使用方法：{jdata['command_prefix']}setuserid [用戶ID]")
    async def setuserid(self,ctx,userid:int=0):
        if ctx.author.id == int(jdata['owner']):
            if userid != 0 and len(str(userid)) == 18:
                await ctx.send('指定：<@' + str(userid) + '> 為聊天對象')
                user = self.bot.get_user(userid)
                if user != None:
                    chonMessageUser(int(userid))
            else:
              chonMessageUser(int(userid))
              await ctx.send("已重置")

def setup(bot):
    bot.add_cog(event(bot))