const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lineas = data.trim().split('\n');

    let totalStudents = 0;
    const fields = {};

    for (let i = 0; i < lineas.length; i += 1) {
      const linea = lineas[i].trim();

      if (i === 0) {

      } else if (linea.length >= 4) {
        const parts = linea.split(',');
        const firstname = parts[0];
        const field = parts[3];

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
        totalStudents += 1;
      }
    }

    console.log(`Number of students: ${totalStudents}`);
    for (const field in fields) {
      const list = fields[field].join(', ');
      console.log(`Number of students in ${field}: ${fields[field].length}. List: ${list}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
