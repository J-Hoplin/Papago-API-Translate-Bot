import {
  CommandInteraction,
  PermissionFlagsBits,
  SlashCommandBuilder,
  SlashCommandStringOption,
} from "discord.js";
import { DiscordCustomClient } from "../classes";
import { Command, SlashCommandChoice, PapagoLanguageSet } from "../types";
import { papagoRequest } from "../app/";
import {
  translateResultFailEmbed,
  translateResultSuccessEmbed,
} from "../embeds";
import logger from "../log/index";
import { mapper } from "./papago-language-mapper";

const supportedLanguages: PapagoLanguageSet[] = [
  ...Object.keys(mapper).map((x: string): PapagoLanguageSet => {
    return {
      key: x,
      name: mapper[x],
    };
  }),
];

export const papagoTranslate: Command = {
  data: new SlashCommandBuilder()
    .setName("translate")
    .setDescription("Translate your sentence using papago!")
    .addStringOption((option): SlashCommandStringOption => {
      return option
        .setName("from")
        .setDescription("Translate from")
        .setRequired(true)
        .addChoices(
          ...supportedLanguages.reduce(
            (acc: SlashCommandChoice[], cur: PapagoLanguageSet, idx, src) => {
              acc.push({
                name: cur.name,
                value: cur.key,
              });
              return acc;
            },
            []
          )
        );
    })
    .addStringOption((option): SlashCommandStringOption => {
      return option
        .setName("to")
        .setDescription("Translate to")
        .setRequired(true)
        .addChoices(
          ...supportedLanguages.reduce(
            (acc: SlashCommandChoice[], cur, idx, src) => {
              acc.push({
                name: cur.name,
                value: cur.key,
              });
              return acc;
            },
            []
          )
        );
    })
    .addStringOption((option): SlashCommandStringOption => {
      return option
        .setName("content")
        .setDescription("Content you want to translate")
        .setRequired(true);
    })
    .addStringOption((option): SlashCommandStringOption => {
      return option
        .setName("private")
        .setDescription(
          "Yes if you want to make question and response as public. Default is No"
        )
        .setRequired(false)
        .addChoices({ name: "Yes", value: "Yes" }, { name: "No", value: "No" });
    }),
  run: async (client: DiscordCustomClient, interaction: CommandInteraction) => {
    const requestUserName = interaction.user.username;
    const from = interaction.options.get("from")?.value;
    const to = interaction.options.get("to")?.value;

    const fromName = mapper[from as string];
    const toName = mapper[to as string];
    const content = interaction.options.get("content")!.value as string;
    const ephemeral =
      interaction.options.get("private")?.value === undefined ? true : false;

    logger.info(
      `Translation Request(${requestUserName}) - ${from} → ${to} - Content : ${content}`
    );
    const result = await papagoRequest(from as string, to as string, content);
    try {
      if (result.type === "success") {
        await interaction.reply({
          embeds: [
            await translateResultSuccessEmbed(
              fromName as string,
              toName as string,
              content,
              result.result
            ),
          ],
          ephemeral,
        });
      } else {
        await interaction.editReply({
          embeds: [await translateResultFailEmbed(result.errormessage)],
        });
      }
    } catch (err) {
      logger.error("Fail to embed - Too many contents");
      await interaction.reply({
        embeds: [
          await translateResultFailEmbed(
            "😓 Content should be less than 1024 characters!"
          ),
        ],
        ephemeral,
      });
    }
  },
};
