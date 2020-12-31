import { NowRequest, NowResponse } from '@vercel/node'

export default function (req: NowRequest, res: NowResponse) {
    const { name = 'NULL' } = req.query
    res.send(`Typescript: Hello ${name}!`)
}