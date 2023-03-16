import { ApplicationCommandOption, SlashCommandBuilder, SlashCommandStringOption } from 'discord.js' 

interface Command{
    data: Omit<SlashCommandBuilder, "addSubcommand" | "addSubcommandGroup"> ,
    permission?: string[],
    run(...args:any[]):Promise<any>
}

export default Command