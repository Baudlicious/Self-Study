function Get-OSInfo {
    param(
        [string]$computer_name = 'localhost'
    )
    Get-CimInstance -ClassName Win32_OperatingSystem -ComputerName $computer_name
}

Get-OSInfo -computerName localhost