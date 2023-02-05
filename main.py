import discord, pytz, os
from discord import ui, app_commands, Interaction, ButtonStyle
from discord.ui import Button, View
from datetime import datetime
from config import config
from SihwanO_modals import MainModal

class MyClient(discord.Client):
    async def on_ready(self):
        await tree.sync(guild= discord.Object(id=config.config('guild')))
        os.system('cls')
        print("Newbie Bot - SihwanO")
        print("Github - https://github.com/SihwanO")

client = MyClient(intents = discord.Intents.all())
tree = app_commands.CommandTree(client)

@tree.command(guild=discord.Object(id=config.config('guild')), name="인증", description="모달 인증기능을 업로드합니다.")
async def mkbutton(interaction: Interaction):
    channel = client.get_channel(config.config('nowbie_channel'))
    embed = discord.Embed(timestamp=datetime.now(pytz.timezone('UTC')), title='뉴비인증', description='버튼을 눌러 뉴비인증을 완료하세요.', color=0xff9d9d)
    button = ui.Button(style=ButtonStyle.green, label='인증하기')
    view = ui.View(timeout=None)
    view.add_item(button)
    async def button_callback(interaction:Interaction):
        await interaction.response.send_modal(MainModal())
    button.callback = button_callback
    await interaction.response.send_message('업로드 완료')
    await channel.send(embed=embed, view=view)

client.run(config.config('token'))