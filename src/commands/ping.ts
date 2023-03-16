import { CommandInteraction, PermissionFlagsBits, SlashCommandBuilder, SlashCommandStringOption } from "discord.js";
import { DiscordCustomClient } from "../classes";
import { Command } from "../types";
import logger from "../log/index";

export const pingcommand: Command = {
    data: new SlashCommandBuilder()
        .setName('ping')
        .setDescription("Check command's ping status!")
        .addStringOption((option): SlashCommandStringOption => {
            return option
                .setName("ispublic")
                .setDescription("Yes if you want to make question and response as public. Default is No")
                .setRequired(false)
                .addChoices(
                    { name: 'Yes', value: 'Yes' },
                    { name: 'No', value: 'No' }
                )
        }),
    run: async (client: DiscordCustomClient, interaction: CommandInteraction) => {
        const ephemeral = interaction.options.get('ispublic')?.value === 'Yes' ? false : true
        await interaction.reply({
            content: `🏓 Pong! My latency status is ${client.ws.ping}ms!`,
            ephemeral
        })
        logger.info(`User : ${interaction.user.username} / Request Ping!`)
    }
}

export default pingcommand