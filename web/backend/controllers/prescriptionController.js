const { spawn } = require('child_process');
const path = require('path');

exports.processPrescription = (req, res) => {
  const imagePath = req.body.imagePath;

  // Path to the Python script
  const scriptPath = path.join(__dirname, '..', '..', 'main.py');

  // Run the Python script
  const pythonProcess = spawn('python', [scriptPath, imagePath]);

  let responseData = '';

  pythonProcess.stdout.on('data', (data) => {
    responseData += data.toString();
  });

  pythonProcess.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
    if (!res.headersSent) {
      res.status(500).send(data.toString());
    }
  });

  pythonProcess.on('close', (code) => {
    if (!res.headersSent) {
      if (code === 0) {
        res.status(200).send(responseData);
      } else {
        res.status(500).send(`Python script exited with code ${code}`);
      }
    }
  });
};
