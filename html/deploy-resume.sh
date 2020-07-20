#!/bin/bash 
# Upload static website

BUCKET="resume.hobbitcakes.com"

gsutil rsync -R ./resume.hobbitcakes.com gs://$BUCKET/
