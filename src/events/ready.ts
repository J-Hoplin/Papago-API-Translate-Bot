import { DiscordCustomClient } from "../classes"
import logger from "../log/index"


function ready(client: DiscordCustomClient){
    logger.info(`${client.user?.username} is online`)
}

export default ready