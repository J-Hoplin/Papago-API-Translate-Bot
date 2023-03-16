import { SlashCommandBuilder } from "discord.js";
import SlashCommandExecute from "./SlashCommandExecute";

interface SlashCommandItf{
    slash: SlashCommandBuilder,
    execute: ({ interaction }:SlashCommandExecute) => Promise<void>
}

export default SlashCommandItf