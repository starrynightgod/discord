from discord.ext import commands
from core.classes import Cog_Extension
from threading import Timer

a=0
def time(tim):
    global a
    a+=1
    t=Timer(tim,time,args=(tim,))
    t.start()
#===================================================================================
class main(Cog_Extension):
    @commands.command(name= 'ping', aliases=['延遲' , '機器人延遲' , 'delay'])
    async def ping(self,ctx):
        global a
        await ctx.send(f'延遲：{round(self.bot.latency*1000)} 毫秒 (ms)\n 機器人維持 {a} 秒')
        
#==================================================================================
    @commands.command()
    async def avatar(self,ctx,userid:str='0'):
        user = self.bot.get_user(int(userid))
        asset = user.avatar_url
        await ctx.send(str(asset))


def setup(bot):
    bot.add_cog(main(bot))
    time(int(1))