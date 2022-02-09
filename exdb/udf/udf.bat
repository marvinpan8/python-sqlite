@echo off
set SAVE_MCO_ROOT=%MCO_ROOT%
set MCO_ROOT=%CD%\..\..\..
%MCO_ROOT%\target\bin\xsql -b -f udf.sql
set MCO_ROOT=%SAVE_MCO_ROOT%
