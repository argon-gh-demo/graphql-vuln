const mysql = require('mysql');
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'users'
});

const userId = req.query.id; // Assuming this is user input

const query = `SELECT * FROM users WHERE id = ${userId}`;
connection.query(query, (error, results) => {
  if (error) throw error;
  console.log(results);
});
