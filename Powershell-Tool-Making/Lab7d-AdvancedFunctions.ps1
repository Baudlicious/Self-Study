function Get-SystemInfo {
    [CmdletBinding()]
    param (
        [string[]]$ComputerName
    )
    BEGIN {}
    PROCESS {
        foreach ($Computer in ComputerName) {
            $os = Get-WmiObect -class Win32_OperatingSystem -ComputerName $computer
            $comp = Get-WmiObect -class Win32_ComputerSystem -ComputerName $computer

            $props = @{'LastBootTime'=$os.;                 #boottime ConvertToDateTime()
                       'ComputerName'=$os.name;             #computer name
                       'OSVersion'=$os.version;             #Os version
                       'Manufacturer'=$comp.manufacturer;   #manufacture
            #model 
            }
        }
    }
    END {}
}