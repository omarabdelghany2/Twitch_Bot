
from twitchio.ext import commands

class Bot(commands.Bot):
    def __init__(self,window):
        self.ArrayOfPeopleNames = [""]
        super().__init__(token='oauth:qnqc84df3gr97wu86n4j3kq47hhwmi', prefix='!', initial_channels=['omar_abdelghany2000'])
        self.window=window

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')





   
        

    @commands.command()
    async def test(self, ctx: commands.Context):
        await ctx.send("test passed")

    async def closee(self):
        await super().close()  # Terminate the bot


    async def event_message(self,ctx):
        # make sure the bot ignores itself and the streamer
        if(ctx.content=="cheer100 yay"):
            self.window.increase_loading_bar.emit()
            return 
        if(ctx.content=="cheer100 boo"):
            self.window.decrease_loading_bar.emit()
            return
        if(ctx.content=="!thumbsup"):
            for item in self.ArrayOfPeopleNames :
                if(ctx.author.name.lower()==item):
                    return
            self.window.increase_loading_bar.emit()
            self.ArrayOfPeopleNames.append (ctx.author.name.lower())


        if(ctx.content=="!thumbsdown"):

            for item in self.ArrayOfPeopleNames :
                if(ctx.author.name.lower()==item):
                    return
            self.window.decrease_loading_bar.emit()
            self.ArrayOfPeopleNames.append (ctx.author.name.lower())  

         ##lets start commands of the subscriber---------------->>>>>>>>
        if(ctx.content=="!sickjam"):

           if ctx.author.is_subscriber:
                for item in self.ArrayOfPeopleNames :
                    if(ctx.author.name.lower()==item):
                        return
                self.window.increase_loading_bar.emit()
                self.ArrayOfPeopleNames.append (ctx.author.name.lower())  


        if(ctx.content=="!kewlbeanz"):

           if ctx.author.is_subscriber:
                for item in self.ArrayOfPeopleNames :
                    if(ctx.author.name.lower()==item):
                        return
                self.window.decrease_loading_bar.emit()
                self.ArrayOfPeopleNames.append(ctx.author.name.lower())

        if(ctx.content=="!frontbutt"):

            if ctx.author.is_subscriber:
                    for item in self.ArrayOfPeopleNames :
                        if(ctx.author.name.lower()==item):
                            return
                    self.window.increase_loading_bar.emit()
                    self.ArrayOfPeopleNames.append (ctx.author.name.lower())           
        if(ctx.content=="!hype"):

            if ctx.author.is_subscriber:
                    for item in self.ArrayOfPeopleNames :
                        if(ctx.author.name.lower()==item):
                            return
                    self.window.increase_loading_bar.emit()
                    self.ArrayOfPeopleNames.append (ctx.author.name.lower()) 
        if(ctx.content=="!rude"):

           if ctx.author.is_subscriber:
                for item in self.ArrayOfPeopleNames :
                    if(ctx.author.name.lower()==item):
                        return
                self.window.decrease_loading_bar.emit()
                self.ArrayOfPeopleNames.append(ctx.author.name.lower())
        if(ctx.content=="!uncoolbeans"):

           if ctx.author.is_subscriber:
                for item in self.ArrayOfPeopleNames :
                    if(ctx.author.name.lower()==item):
                        return
                self.window.decrease_loading_bar.emit()
                self.ArrayOfPeopleNames.append(ctx.author.name.lower()) 
        if(ctx.content=="!canceled"):

           if ctx.author.is_subscriber:
                for item in self.ArrayOfPeopleNames :
                    if(ctx.author.name.lower()==item):
                        return
                self.window.decrease_loading_bar.emit()
                self.ArrayOfPeopleNames.append(ctx.author.name.lower())
        if(ctx.content=="!unhype"):

           if ctx.author.is_subscriber:
                for item in self.ArrayOfPeopleNames :
                    if(ctx.author.name.lower()==item):
                        return
                self.window.decrease_loading_bar.emit()
                self.ArrayOfPeopleNames.append(ctx.author.name.lower())                                                                                                                                