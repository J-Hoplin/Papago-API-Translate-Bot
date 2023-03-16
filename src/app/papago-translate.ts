import axios, { AxiosError } from "axios";
import qs from 'querystring'
import { PapagoErrorMessage, PapagoResult } from '../types'
import logger from "../log/index";

export const papagoRequest = async (from: string, to: string, content: string) => {
    try {
        const queryString = qs.stringify({
            source: from,
            target: to,
            text: content
        })
        const { data } = await axios.post(
            'https://openapi.naver.com/v1/papago/n2mt',
            queryString,
            {
                headers: {
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'X-Naver-Client-Id': process.env.X_Naver_Client_Id as string,
                    'X-Naver-Client-Secret': process.env.X_Naver_Client_Secret as string
                }
            }
        )
        const translatedText = data?.message?.result?.translatedText
        return {
            type: 'success',
            result: translatedText
        } as PapagoResult
    } catch (err) {
        const error = err as AxiosError;
        const data = error.response?.data;
        let errorMessage = ""
        if (data) {
            const errInfo = data as PapagoErrorMessage;
            errorMessage = errInfo.errorMessage
            logger.error(`Error while processing request - ${errInfo.errorCode} : ${errorMessage}`)
        } else {
            errorMessage = "Error while request to API!"
            logger.error(`Error while processing request - ${errorMessage}`)
        }
        return {
            type: 'fail',
            errormessage: errorMessage
        } as PapagoResult
    }
}

// papagoRequest('ko', 'en', '안녕!')
