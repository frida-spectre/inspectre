@ECHO off
RD /S /Q .\dist

pyinstaller build.spec

COPY /V /Y .\src\inspectre.json .\dist\