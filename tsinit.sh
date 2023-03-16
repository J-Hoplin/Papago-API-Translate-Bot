#!/bin/zsh

# Require init directory

function help(){
    echo "- \$1 : Require project init directory."
}

# Check if parameter given
if [ -z $1 ]
then
    help
    exit 1
fi

# Check if directory exist. If not exist, make directory and initiate
if [ ! -d $1 ]
then
    mkdir $1
fi

# Move directory
cd $1
mkdir src
# Install typescript init 
npm i -D typescript tslint @types/node
# tslint.json config
./node_modules/.bin/tslint --init
# tsconfig.json
cat >> tsconfig.json <<EOF
{
    "compilerOptions": {
        "lib": [
            "ES2020"
        ],
        "module": "CommonJS",
        "outDir": "dist",
        "sourceMap": true,
        "strict": true,
        "target": "ES2020",
    },
    "include": [
        "src"
    ]
}
EOF