@REM args(
@REM name: "ABC*",
@REM number: "*",
@REM )
@echo off

setlocal enabledelayedexpansion

set name=a b c d e f g h i j k l m n o p q r s t u v w x y z
set num=0

echo %~dp0..\%1\test

mkdir %~dp0..\%1\test

for %%a in (%name%) do (
  set /a num=num+1
  if !num! leq %2 (
    mkdir %~dp0..\%1\test\%%a\in
    mkdir %~dp0..\%1\test\%%a\out
    mkdir %~dp0..\%1\test\%%a\ans
  )
)