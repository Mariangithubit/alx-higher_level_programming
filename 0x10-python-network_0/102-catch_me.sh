#!/bin/bash
# script makes request to 0.0.0.0:5000/catch_me causes server to respond message
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
