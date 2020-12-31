module.exports = (req, res) => {
    const { name = 'World' } = req.query
    res.send(`JavaScript: Hello ${name}!`)
}