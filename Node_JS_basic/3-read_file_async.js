const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lineas = data.trim().split('\n');
    const fields = {};
    let totalStudents = 0;

    for (let i = 1; i < lineas.length; i += 1) {
      const linea = lineas[i].trim();
      if (linea) {
        const parts = linea.split(',');
        if (parts.length >= 4) {
          const firstname = parts[0];
          const field = parts[3];

          if (!fields[field]) {
            fields[field] = [];
          }
          fields[field].push(firstname);
          totalStudents += 1;
        }
      }
    }

    console.log(`Number of students: ${totalStudents}`);

    for (const field in fields) {
      if (Object.prototype.hasOwnProperty.call(fields, field)) {
        const list = fields[field].join(', ');
        console.log(`Number of students in ${field}: ${fields[field].length}. List: ${list}`);
      }
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
