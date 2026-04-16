require('dotenv').config();
const express = require('express');
const app = express();
const mysql = require('mysql2');
app.use(express.json()); // Support JSON bodies

const con = mysql.createConnection({
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME,
    port: process.env.DB_PORT,
});


con.connect(err => {
    if (err) {
        console.error('Erro ao conectar na Aiven:', err);
        return;
    }
    console.log('✅ Conectado ao MySQL da Aiven!');
});



app.get('/Authors', (req, res) =>{
    const sql = "SELECT Nome_Autor FROM Message";
    con.query(sql, (err, result) => {
        if (err) return res.status(500).json(err);
        res.json(result);
    });
})

app.get('/Message', (req, res) =>{
    const sql = "SELECT * FROM Message";
    con.query(sql, (err, result) => {
        if (err) return res.status(500).json(err);
        res.json(result);
    });
})


app.post("/sendMessage", (req, res)=>{
    const { mensagem, Nome_Autor } = req.body;
    const sql = "INSERT INTO message (mensagem, Nome_Autor) VALUES (?,?)";
    
    con.query(sql, [mensagem, Nome_Autor], (err, result) => {
        if (err) return res.status(500).json(err);
        res.json({ message: "Mensagem Enviada", affectedRows: result.affectedRows });
    });
});


app.listen(process.env.PORT)


