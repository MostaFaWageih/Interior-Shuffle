const express = require('express');
const uploadRoutes = require('./scripts/upload');
const redesignRoutes = require('./scripts/redesign');

const app = express();
app.use('/upload', uploadRoutes);
app.use('/redesign', redesignRoutes);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

