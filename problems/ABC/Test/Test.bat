@echo off
source C:/Users/Shima_Yuu/.virtualenvs/AtCoder-3VgDB5mr/Scripts/activate
echo %1/%2.py
if "%3"=="" (
  echo %3
) else (
  python ../%1/test/%2.py
)

for %%f in (../%1/test/%2/in/*.txt) do (
  echo %%f
  echo ===============input===============
  cat ../%1/test/%2/in/%%f
  echo ===================================

  echo ===============output==============
  cat ../%1/test/%2/in/%%f | python ../%1/%2.py
  echo ===================================
  @REM cat ../%1/test/%2/in/%%f | python ../%1/%2.py > ../%1/test/%2/out/%%f

  ls -l ../%1/test/%2/out/

  fc ../%1/test/%2/out/%%f ../%1/test/%2/ans/%%f
  if %errorlevel% == 0 (
    echo OK
  ) else (
    echo NG
  )

  echo;
)
