#!/usr/bin/env bash

SRC_ODBC=/usr/local/Cellar/unixodbc/2.3.2_1/include
export C_INCLUDE_PATH=$C_INCLUDE_PATH:$SRC_ODBC
export CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:$SRC_ODBC
npm install odbc
