import Discord, { ClientOptions, Collection } from 'discord.js'
import { Command, DiscordAssets } from '../types';
/**
 * Deploy require $PATH variable.
 * 
 * In this project, use 'dotenv' for ENV variable. require to dotenv configuration before
 */
import { deploy } from '../deploy'

class DiscordCustomClient extends Discord.Client {
    public commands: Collection<string, Command> = new Collection();
    constructor(options: ClientOptions, assets?: DiscordAssets) {
        super(options)

        //If assets is not null
        if (assets) {
            const { commands } = assets
            // Enroll Commands
            commands.map((x: Command) => {
                this.commands.set(x.data.name, x);
            })
        };
        // Deploy command route
        (async () => await deploy(this))()

    }
}

export default DiscordCustomClient