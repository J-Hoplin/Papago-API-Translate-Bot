import { config } from 'winston'

interface CustomOption {
    levels: config.AbstractConfigSetLevels,
    colors: config.AbstractConfigSetColors
}

export default CustomOption