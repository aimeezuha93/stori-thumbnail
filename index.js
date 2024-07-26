const AWS = require('aws-sdk');
AWS.config = new AWS.Config();
AWS.config.accessKeyId = process.env.accessKey;
AWS.config.secretAccessKey = process.env.secretKey;
AWS.config.region = "us-east-1";

const s3 = new AWS.S3();

document.getElementById('imageForm').addEventListener('submit', (event) => {
    event.preventDefault();

    const fileInput = document.getElementById('imageInput');
    const file = fileInput.files[0];
    if (!file) {
        alert('Please select a file to upload.');
        return;
    }

    const key = `images/${file.name}`;
    const params = {
        Bucket: 'stori-data-services-in-prod',
        Key: key,
        Body: file
    };

    s3.putObject(params, (err, data) => {
        if (err) {
            console.error('Error uploading file:', err);
            alert('An error occurred while uploading the file.');
        } else {
            console.log('File uploaded successfully:', data);
            alert('File uploaded successfully!');
        }
    });
});