import discord, pymysql, json
from discord import ui, Interaction
from discord.ui import Button, View

with open("config.json", 'r', encoding='utf-8') as Database:
    SihwanOs = json.load(Database)

Table_name = SihwanOs['sql']['Table_name']

def check():
        SQL = pymysql.connect(host = SihwanOs['sql']['host'], user = SihwanOs['sql']['user'], password = SihwanOs['sql']['password'], db = SihwanOs['sql']['db_name'], charset = 'utf8')
        Database = SQL.cursor()
        return SQL, Database

class MainModal(ui.Modal, title="뉴비인증"):
    nowbie_code = ui.TextInput(
        label = '인증번호',
        style = discord.TextStyle.short,
        placeholder='인증번호를 입력해주세요. (ex.829562)',
        required = True, 
        max_length = 6
    )

    async def on_submit(self, interaction: Interaction):
        Database, SQL = check()
        if SQL == False: 
            return await interaction.response.send_message('데이터베이스 연결이 불가능 합니다.', ephemeral=True)
        nowbie_codes = self.nowbie_code
        SQL.execute(f'select code from {Table_name} where code = "{nowbie_codes}"')
        SihwanO_check = SQL.fetchone()
        if SihwanO_check is None:
            return await interaction.response.send_message('`고유번호와 일치하지 않는 인증코드 입니다`\n> 다시 확인 후 인증해주세요', ephemeral=True)
        else:
            SQL.execute(f'select * from {Table_name} where state = "0" and code = "{nowbie_codes}"')
            SihwanO_check1 = SQL.fetchone()
            SQL.execute(f'select * from {Table_name} where code = "{nowbie_codes}"')
            SihwanO_check2 = SQL.fetchone()

            if SihwanO_check1 is not None:
                SQL.execute(f'update {Table_name} set state = "1" where code = "{nowbie_codes}"')
                Database.commit()
                await interaction.response.send_message('인증이 정상적으로 완료 되었습니다', ephemeral=True)
                return await interaction.user.add_roles(interaction.guild.get_role(int(SihwanOs['SihwanO']['role'])))
            
            elif SihwanO_check2[2] >= 1:
                return await interaction.response.send_message('입력하신 코드는 이미 인증된 코드 입니다.', ephemeral=True)
