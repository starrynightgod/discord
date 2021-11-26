from discord.ext import commands
from core.classes import Cog_Extension
import requests
import json
from opencc import OpenCC

cc = OpenCC('s2twp') #簡體中文 -> 繁體中文 (台灣, 包含慣用詞轉換)

rawDict = requests.get("https://raw.githubusercontent.com/lonnstyle/riven-mirror/dev/src/i18n/lang/zh-Hant.json")
Dict = json.loads(rawDict.text)
Dict = Dict['messages']

class baroManual(Cog_Extension):
  @commands.command(name='baro',aliases=['奸商' , '虛空商人' , 'Baro'], brief="warframe", description="此功能可以查詢虛空商人的商品或抵達前剩餘時間")
  async def baroManual(self,ctx):
    url = requests.get("https://api.warframestat.us/pc/tc/voidTrader",headers={'Accept-Language':'zh','Cache-Control': 'no-cache'})
    html = json.loads(url.text)
    if html['active'] == True:
      message = "```"
      location = html['location']
      location = cc.convert(location)
      stay = html['endString']
      stay = stay.replace("d","天")
      stay = stay.replace("h","小時")
      stay = stay.replace("m","分鐘")
      stay = stay.replace("s","秒")
      await ctx.send(f"Baro Ki'Teer 已經到達{location},停留時間為{stay}\t帶來的商品如下:")
      for items in html['inventory']:
        item = items['item']
        item = item.lower()
        item = item.replace("\'","")
        count = 0
        name = ''
        for words in item.split():
          if count != 0:
            word = words.capitalize()
            name += word
          elif count == 0:
            name += words
          count += 1
        name = Dict.get(name,name)
        ducats = items['ducats']
        credits = items['credits']
        message += f"物品:{name}\n杜卡德金幣:{ducats}\t現金:{credits}\n"
      message += "```"
      await ctx.send(message)
    if html['active'] == False:
      location = html['location']
      location = cc.convert(location)
      arrive = html['startString']
      arrive = arrive.replace("d","天")
      arrive = arrive.replace("h","小時")
      arrive = arrive.replace("m","分鐘")
      arrive = arrive.replace("s","秒")
      await ctx.send(f"Baro Ki' Teer會在{arrive}後抵達{location}") 


def setup(bot):
    bot.add_cog(baroManual(bot))