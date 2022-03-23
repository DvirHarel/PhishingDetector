
const express = require('express')
const app = express()
const port = 3000
const exec = require("child_process").execSync;
const myArgs = process.argv.slice(2);

app.get('/', (req, res) => {
    const url = req.url.substring(req.url.indexOf("=")+1)
    var result = exec(`${myArgs[0]}/venv/bin/python ${myArgs[0]}/Main.py ${url}`);
    console.log(result.toString())
    res.send(result.toString())
})

app.listen(port, () => {
  console.log(`listening at http://localhost:${port}`)
})
console.log("start server")
