import disnake
import json

from disnake.ext import commands
from config import TOKEN, COGS_LIST, DEVS_ID
from disnake import TextInputStyle
from disnake import Button, ButtonStyle

# С ЛЮБОВЬЮ ОТ trigand

bot = commands.Bot(
    command_prefix="#",
    intents=disnake.Intents.all(),
    status=disnake.Status.dnd,
    activity=disnake.Game(name="🖤")
)
bot.remove_command('help')
    

    
@bot.event
async def on_ready():
    print(f"[Bot] Бот {bot.user.name} в сети!")

@bot.slash_command(description="Загрузка кога.")
async def load(inter: disnake.CommandInteraction, cog: str):
    if inter.author.id in DEVS_ID:
        try:
            bot.load_extension(f"cogs.{cog}")
            await inter.response.send_message(f'Ког {cog} успешно загружен')
        except commands.ExtensionNotFound:
            await inter.response.send_message(f'Ког {cog} не найден')
        except commands.ExtensionAlreadyLoaded:
            await inter.response.send_message(f'Ког {cog} уже загружен')
    else:
        await inter.response.send_message(content="У вас нет права использовать эту команду.")

@bot.slash_command(description="Перезагрузка кога.")
async def reload(inter: disnake.CommandInteraction, cog: str):
    if inter.author.id in DEVS_ID:
        try:
            bot.reload_extension(f"cogs.{cog}")
            await inter.response.send_message(content=f"Ког {cog} успешно перезагружен.")
        except commands.ExtensionNotFound:
            await inter.response.send_message(content=f"Ког {cog} не найден.")
        except commands.ExtensionNotLoaded:
            await inter.response.send_message(content=f"Ког {cog} не был загружен.")
    else:
        await inter.response.send_message(content="У вас нет права использовать эту команду.")

@bot.slash_command(description="Отгрузка кога.")
async def unload(inter: disnake.CommandInteraction, cog: str):
    if inter.author.id in DEVS_ID:
        try:
            bot.unload_extension(f"cogs.{cog}")
            await inter.response.send_message(f'Ког {cog} успешно выгружен')
        except commands.ExtensionNotFound:
            await inter.response.send_message(f'Ког {cog} не найден')
        except commands.ExtensionNotLoaded:
            await inter.response.send_message(f'Ког {cog} не был загружен')
    else:
        await inter.response.send_message(content="У вас нет права использовать эту команду.")



@bot.slash_command()
async def test(interaction: disnake.AppCmdInter):
    await interaction.send("Свой текст")






        
for cog in COGS_LIST:
    try:
        bot.load_extension(f'cogs.{cog}')
        print(f"[Cogs] Ког {cog} загружен!")
    except commands.ExtensionNotFound:
        print(f'[Cogs] Ког {cog} не найден')
        

bot.run(TOKEN)