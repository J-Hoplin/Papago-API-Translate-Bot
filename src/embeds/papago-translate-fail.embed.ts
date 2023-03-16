import { EmbedBuilder } from "@discordjs/builders"

export const translateResultFailEmbed = async (errorMessage: string) => {
    return new EmbedBuilder()
        .setColor(0x29cdff)
        .setTitle(`Sorry😓 fail to translate`)
        .setDescription('Please request this issue to guild\'s master!')
        .setThumbnail("https://papago.naver.com/static/img/papago_og.png")
        .addFields(
            {
                name: 'Error Message',
                value: errorMessage
            },
        )
        .setTimestamp()
        .setFooter({
            text: 'Service provided by Hoplin',
            iconURL: 'https://avatars.githubusercontent.com/u/45956041?v=4'
        })
}