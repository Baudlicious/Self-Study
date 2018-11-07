Param (
    [string]$computer_name = 'localhost'

)

Get-CimInstance -ClassName Win32_OperatingSystem -ComputerName $computer_name
