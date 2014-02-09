#!/bin/sh
awk '{print $'${1:-1}'}'
