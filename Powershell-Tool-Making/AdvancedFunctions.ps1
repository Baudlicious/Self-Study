function Get-RemoteSystemInfo {
    [CmdletBinding()]
    param(
        [string[]]$ComputerName,

        [string]$ErrorLog
    )
    BEGIN {
        # Better way to do this, learned in later chapters
        Write-Output "Log name is $ErrorLog"
    }
    PROCESS {
        foreach ($Computer in $ComputerName) {
           $os = Get-WmiObject -class Win32_OperatingSystem -ComputerName $Computer 
           $comp = Get-WmiObject -class Win32_ComputerSystem -ComputerName $Computer 
           $bios = Get-WmiObject -class Win32_BIOS -ComputerName $computer

           $props = @{'ComputerName'=$computer;
                      'OSVersion'=$os.version;
                      'SPVersion'=$os.servicepackmajorversion;
                      'BIOSSerial'=$bios.serialnumber;
                      'Manufacturer'=$comp.manufacturer;
                      'Model'=$comp.model}
            $obj = New-Object -TypeName PSObject -Property $props
           Write-Output $obj 
        }
    }
    END {}
}

Get-RemoteSystemInfo -ErrorLog x.txt -ComputerName localhost,localhost 