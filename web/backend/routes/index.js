const express = require('express');
const router = express.Router();
const prescriptionController = require('../controllers/prescriptionController');

// Define routes
router.post('/process-prescription', prescriptionController.processPrescription);

module.exports = router;
