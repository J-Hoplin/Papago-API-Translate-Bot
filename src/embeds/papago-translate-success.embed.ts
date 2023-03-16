import { EmbedBuilder } from "@discordjs/builders";

export const translateResultSuccessEmbed = async (from: string, to: string, content: string, result: string) => {
    return new EmbedBuilder()
        .setColor(0x29cdff)
        .setTitle(`Translate | ${from} → ${to}`)
        .setThumbnail("https://papago.naver.com/static/img/papago_og.png")
        .addFields(
            {
                name: 'Content you want to translate',
                value: content
            },
            {
                name: 'Translation result',
                value: result
            }
        )
        .setTimestamp()
        .setFooter({
            text: 'Service provided by Hoplin',
            iconURL: 'https://avatars.githubusercontent.com/u/45956041?v=4'
        })
}



