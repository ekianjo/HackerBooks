#!/bin/sh
echo -n 'what is the value? '
read value
sed  's/XXX/'$value'/' <<EOF
The value is XXX
EOF

