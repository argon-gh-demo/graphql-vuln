const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql');

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));

// Database configuration (replace with your actual database credentials)
const dbConfig = {
  host: 'localhost',
  user: 'username',
  password: 'password',
  database: 'mydb'
};

// Establish a database connection
const connection = mysql.createConnection(dbConfig);

connection.connect(error => {
  if (error) throw error;
  console.log('Connected to the database');
});

// Route to fetch user by username securely
app.get('/users/:username', (req, res) => {
  const username = req.params.username; // non-escaped user input

  const query = `SELECT * FROM users WHERE username = ${username}`;

  connection.query(query, (error, results) => {
    if (error) throw error;
    res.json(results);
  });
});

app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});

