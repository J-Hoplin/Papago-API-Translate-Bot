import {REST,Routes} from 'discord.js'
import { DiscordCustomClient } from '../classes'
import logger from '../log/index'

const deploy = async (client: DiscordCustomClient) => {
    const commands = client.commands.map(command => {
        return command.data.toJSON()
    })

    const rest = new REST({version:'10'}).setToken(process.env.DISCORD_API as string)
    const datas = await rest.put(
        Routes.applicationGuildCommands(process.env.APPLICATION_ID as string, process.env.GUILD_ID as string),
        {body: commands}
    )
    logger.info(`Total enrolled command : ${(datas as any[]).length} command(s)`)
}

export default deploy