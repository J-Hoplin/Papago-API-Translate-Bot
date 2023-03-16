import { TransformableInfo } from 'logform'
import { config, createLogger, format, transports } from 'winston'
import winston = require('winston')
import path = require('path')
import { CustomOption } from '../types'

const options: CustomOption = {
    levels: {
        error: 0,
        warn: 1,
        info: 2,
        debug: 3,
        other: 4
    },
    colors: {
        error: 'red',
        warn: 'yellow',
        info: 'green',
        debug: 'magenta',
        other: 'white'
    }
}


winston.addColors(options.colors)

interface Levels extends winston.Logger {
    error: winston.LeveledLogMethod;
    warn: winston.LeveledLogMethod;
    info: winston.LeveledLogMethod;
    debug: winston.LeveledLogMethod;
    other: winston.LeveledLogMethod;
}


const logger: Levels = <Levels>createLogger({
    levels: options.levels,
    format: format.combine(
        format.label({
            label: '[Papago Translation Command]'
        }),
        format.timestamp({
            format: 'YYYY-MM-DD HH:mm:ss'
        }),
        format.colorize(),
        format.printf((info: TransformableInfo) => {
            return `${info.timestamp} - ${info.level} : ${info.label} ${info.message}`
        })
    ),
    transports: [
        new transports.Console({
            level: 'other'
        }),
        new transports.File({
            filename: path.join(__dirname, "../../logfile/common.log")
        }),
        new transports.File({
            filename: path.join(__dirname, "../../logfile/error.log"),
            level: 'error'
        }),
        new transports.File({
            filename: path.join(__dirname, "../../logfile/debug.log"),
            level: 'debug'
        })
    ]
})

export default logger