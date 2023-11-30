import { config } from "dotenv";
import path from "path";
config({
  path: path.join(__dirname, "../.env"),
});

/**
 * Import Here
 *
 */

import { Events, GatewayIntentBits } from "discord.js";
import * as Discord from "./classes";
import { papagoTranslate, pingcommand } from "./commands";
import { interactionCreate, ready } from "./events";
import logger from "./log";

const client: Discord.DiscordCustomClient = new Discord.DiscordCustomClient(
  {
    intents: [
      GatewayIntentBits.Guilds,
      GatewayIntentBits.GuildMembers,
      GatewayIntentBits.MessageContent,
      GatewayIntentBits.GuildMessages,
    ],
  },
  {
    commands: [papagoTranslate, pingcommand],
  }
);

client.once(Events.ClientReady, (info) => {
  logger.info(`I'm ready! Logged in as ${info.user.tag}`);
});

/**
 * Event Emitter
 */
client.on(Events.ClientReady, () => {
  ready(client);
  client.user?.setStatus("online");
  client.user?.setPresence({
    status: "online",
    activities: [
      {
        name: "Use /translate to translate!",
      },
    ],
  });
});

// Slash Command is interaction. Add interaction event listener
client.on(Events.InteractionCreate, (interaction) => {
  interactionCreate(client, interaction);
});

client.login(process.env.DISCORD_API);
