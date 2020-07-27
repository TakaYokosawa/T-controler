if not "%~0"=="%~dp0.\%~nx0" (
    start /min cmd /c,"%~dp0.\%~nx0" %*
    exit
)

cd C:\Users\User\Tcontroller
call .\.tcontroller\Scripts\activate
python Omron_temperature_controller.py