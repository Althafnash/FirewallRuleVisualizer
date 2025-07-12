Get-NetFirewallRule | 
    Select-Object Name, DisplayName, Description | 
    Export-Csv -Path "./firewall_rules_with_desc.csv" -NoTypeInformation
