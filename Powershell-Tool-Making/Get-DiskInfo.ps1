Function Get-DiskInfo {
    Param (
        [string]$computer_name = 'localhost',
        [int]$minimum_free_precent = 10
    )
    $disks = Get-WmiObject -Class Win32_Logicaldisk -Filter "DriveType=3"

    foreach ($disk in $disks) {
        $per_free = ($disk.FreeSpace/$disk.Size)*100;
        if ($per_free -ge $minimum_free_precent){
            $OK = $True
        } else {
            $OK = $False
        }
        $disk|Select DeviceID, VolumeName, Size, FreeSpace, @{Name="OK";Expression={$OK}}
    }
}

Get-DiskInfo