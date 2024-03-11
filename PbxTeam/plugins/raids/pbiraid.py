from ... import *
from ...modules.mongo.raidzone import *


@app.on_message(cdx(["pbr", "pbireplyraid"]))
@sudo_users_only
async def add_pbi_raid(client, message):
    try:
        aux = await eor(message, "**🔄 Processing ...**")
        if not message.reply_to_message:
            if len(message.command) != 2:
                return await aux.edit(
                    "**🤖 Reply to a user's message or give username/user_id.**"
                )
            user = message.text.split(None, 1)[1]
            if "@" in user:
                user = user.replace("@", "")
            fulluser = await app.get_users(user)
            user_id = fulluser.id
        else:
            user_id = message.reply_to_message.from_user.id

        if user_id == message.from_user.id:
            return await aux.edit(
                "**🤣 How Fool, You Want To Activate Pbx Raid On Your Own ID❓**"
            )
        
        praid = await add_pbiraid_user(user_id)
        if praid:
            return await aux.edit(
                "**🤖 Successfully Added Pbx Raid On This User.**"
            )
        return await aux.edit(
            "**🤖 Hey, Pbx Raid Already Active On This User❗**"
        )
    except Exception as e:
        print("Error: `{e}`")
        return




@app.on_message(cdx(["dpbr", "dpbireplyriad"]))
@sudo_users_only
async def del_pbi_raid(client, message):
    try:
        aux = await eor(message, "**🔄 Processing ...**")
        if not message.reply_to_message:
            if len(message.command) != 2:
                return await aux.edit(
                    "**🤖 Reply to a user's message or give username/user_id.**"
                )
            user = message.text.split(None, 1)[1]
            if "@" in user:
                user = user.replace("@", "")
            fulluser = await app.get_users(user)
            user_id = fulluser.id
        else:
            user_id = message.reply_to_message.from_user.id
        
        if user_id == message.from_user.id:
            return await aux.edit(
                "**🤣 How Fool, When I Activate Pbx Raid On Your ID❓**"
            )
        
        lraid = await del_pbiraid_user(user_id)
        if lraid:
            return await aux.edit(
                "**🤖 Successfully Removed Pbx Raid From This User.**"
            )
        return await aux.edit(
            "**🤖 Hey, Pbx Raid Not Active On This User❗**"
        )
    except Exception as e:
        print("Error: `{e}`")
        return
