import path from 'path'
import { config } from 'dotenv'
config({
    path: path.join(__dirname, "../.env")
})

/**
 * Import Here
 * 
 */
import * as Discord from './classes'
import { Events, GatewayIntentBits, Collection, CommandInteraction, Interaction, ActivityType } from 'discord.js'
import { ready, interactionCreate } from "./events"
import logger from './log'
import { papagoTranslate, pingcommand } from './commands'

const client: Discord.DiscordCustomClient = new Discord.DiscordCustomClient({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMembers,
        GatewayIntentBits.MessageContent,
        GatewayIntentBits.GuildMessages
    ]
}, {
    commands: [
        papagoTranslate,
        pingcommand
    ]
});

client.once(Events.ClientReady, info => {
    logger.info(`I'm ready! Logged in as ${info.user.tag}`)
})

/**
 * Event Emitter
 */
client.on(Events.ClientReady, () => {
    ready(client)
    client.user?.setStatus('online')
    client.user?.setPresence({
        status: 'online',
        activities: [{
            name: 'Discord Bot Boiler Plate!',
        }]
    })
})

// Slash Command is interaction. Add interaction event listener
client.on(Events.InteractionCreate, (interaction) => {
    interactionCreate(client, interaction)
})

client.login(process.env.DISCORD_API);