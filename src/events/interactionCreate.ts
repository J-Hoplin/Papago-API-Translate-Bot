import { Interaction } from "discord.js";
import { DiscordCustomClient } from "../classes";

function interactionCreate(client: DiscordCustomClient, interaction: Interaction) {
    if (interaction.isCommand()) {
        const command = client.commands.get(interaction.commandName)

        // If command not found
        if (!command) return
        try {
            command.run(client, interaction)
        } catch (err) {
            if (interaction.replied) {
                interaction.followUp("Error occured while processing commands")
            }
            else {
                interaction.reply("Error occured while processing commands")
            }
        }
    }
}

export default interactionCreate