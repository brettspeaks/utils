#!/usr/bin/env bash

# this is a script which manually sets up the paths so that you can install node odbc.
# unixodbc should should be installed first from homebrew.

SRC_ODBC=/usr/local/Cellar/unixodbc/2.3.4/include
export C_INCLUDE_PATH=$C_INCLUDE_PATH:$SRC_ODBC
export CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:$SRC_ODBC
npm install odbc
