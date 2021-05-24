@ECHO OFF

:: ===================================================================================
:: Changes the page encoding so that special characters are recognized
:: ===================================================================================
CHCP 65001 > NUL


:: ===================================================================================
:: Changes the color of the command prompt to look like the game's theme
:: ===================================================================================
COLOR 0A


:: ===================================================================================
:: Requests the game directory
:: ===================================================================================
SET /p GameDirectory="Informe o diretório onde está localizado o executável do jogo (AI.exe): "


:: ===================================================================================
:: Checks if the game directory exists
:: ===================================================================================
:CHECK_IF_GAME_DIRECTORY_EXISTS
	
	IF NOT EXIST %GameDirectory% (

		ECHO "O diretório %GameDirectory% não existe, verifique se digitou corretamente."
		ECHO.

		SET /p GameDirectory="Informe o diretório onde está localizado o executável do jogo (AI.exe): "

		GOTO :CHECK_IF_GAME_DIRECTORY_EXISTS
	)


:: ===================================================================================
:: Navigates to game's directory
:: ===================================================================================
CD %GameDirectory%


:: ===================================================================================
:: Replaces the original game files for modded game files
:: ===================================================================================
ECHO.

COPY %~dp0\src\content\audio\sample.wav %GameDirectory%\DATA\AUDIO /y
COPY %~dp0\src\content\legend\sample.txt %GameDirectory%\DATA\TEXT /y
COPY %~dp0\src\content\texture\sample.gif %GameDirectory%\DATA\UI /y


:: ===================================================================================
:: Clears the command prompt
:: ===================================================================================
CLS


:: ===================================================================================
:: Sucess message
:: ===================================================================================
ECHO O mod foi instalado com sucesso!
ECHO.


:: ===================================================================================
:: Failed message
:: ===================================================================================
ECHO Não foi possível instalar o mod porque {}...
ECHO.


PAUSE
