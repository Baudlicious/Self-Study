function Get-DiskInfo {
    [CmdletBinding()]
    param(
        [string[]]$ComputerName
    )
    BEGIN {}
    PROCESS {
        foreach ($Computer in $ComputerName){ # Enumerate the computers provided by the call
            
            $disk = Get-WmiObject -class Win32_Volume 
                foreach ($drive in $disk){ # Go through the computer volumes
                $disk_size = $drive.capacity/1024/1024/1024; # Math to GB
                $free = $drive.freespace/1024/1024/1024;
                $props = @{'ComputerName'=$ComputerName;
                        'VolumeName'=$drive.name;
                        'VolumeSize(GB)'=[math]::Round($disk_size,2); #round to 2 places
                        'FreeSpace(GB)'=[math]::Round($free,2); 
                        #'DiskUtilization'=$per_free
                }
                $obj = New-Object -TypeName PSObject -Property $props
                Write-Output $obj
            }
            
        }
    }
    END {}
}

Get-DiskInfo -ComputerName  DevBox