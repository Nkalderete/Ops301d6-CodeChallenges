# variables---user info

$firstname = "Franz"
$lastname = "Ferdinand"
$displayname = "Franz Ferdinand"
$username = "Franz"
$email = "ferdi@globexpower.com"
$office = "Springfield, OR"
$company = "Globex USA"
$department = "TPS"
$jobtitle = "TPS Reporting Lead"
$password = "Nikoda125"


# Create new AD user

New-ADUser -GivenName $firstname -Surname $lastname -DisplayName $displayname `
    -Title $jobtitle -Office $office -Department $department `
    -Email $email -AccountPassword (ConvertTo-SecureString -AsPlainText $password -Force) `
    -Enabled $true -ChangePasswordAtLogon $false -Name $username

