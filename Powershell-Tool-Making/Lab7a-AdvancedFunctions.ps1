# Lab 7a - Advanced Functions

function Get-SystemInfo {
    [CmdletBinding()]
    param (
        [string[]]$ComputerName
    )
    BEGIN {}
    PROCESS {
        foreach ($Computer in $ComputerName){
            $os = Get-WmiObject -class Win32_OperatingSystem -ComputerName $Computer
            $comp = Get-WmiObject -class Win32_ComputerSystem -ComputerName $Computer
            $bios = Get-WmiObject -class Win32_BIOS -ComputerName $Computer

            # Check the return value of AdminPassStatus, Change value to string
            if ($comp.AdminPasswordStatus -eq 1) {
                $AdminPass = 'Disabled'
            }elseif ($comp.AdminPasswordStatus -eq 2) {
                $AdminPass = 'Enabled'
            }elseif ($comp.AdminPasswordStatus -eq 3) {
                $AdminPass = 'NA'
            }elseif ($comp.AdminPasswordStatus -eq 4) {
               $AdminPass = 'Unknown' 
            }
            
            $props = @{'ComputerName'=$computer;
                       'WorkGroup'=$os.workgroup;
                       'AdminPasswordStatus'=$AdminPass; # Call the stringvalue
                       'Model'=$comp.model;
                       'Manufacture'=$comp.manufacturer;
                       'SerialNumber'=$os.serialnumber;
                       'OSVersion'=$os.version;
                       'SPVersion'=$os.servicepackmajorversion}
            $obj = New-Object -TypeName PSObject -Property $props
            Write-Output $obj
        }
    }
    END {}
}

Get-SystemInfo -ComputerName localhost,localhost