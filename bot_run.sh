#!/bin/bash

~/orphan/to_delete_orphan.py;
python ~/orphan/bot_process.py;
mv result.json public/result.json
