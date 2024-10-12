#!/bin/bash
export $(grep -v '^#' ./.env | xargs)
python server.py