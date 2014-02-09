#!/bin/sh
awk '{print $c}' c=${1:-1}
