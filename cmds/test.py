import discord
from discord.ext import commands
from core.classes import Cog_Extension
import os
import requests
import json



class test(Cog_Extension):
    #清除訊息
    @commands.command(name='test', aliases=['機器人測試', '測試'])
    async def t(self,ctx):
      await ctx.send("測試~~")
      print("測試~")
      for command in self.bot.commands:
        print(command.name)
      
  
def setup(bot):
    bot.add_cog(test(bot))