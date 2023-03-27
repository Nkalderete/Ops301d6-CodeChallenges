

# Need to have psutil installed
# pip install psutil 

import psutil

# Get system CPU times
cpu_times = psutil.cpu_times()

# Extract required information
user_time = cpu_times.user
system_time = cpu_times.system
idle_time = cpu_times.idle
priority_user_time = cpu_times.nice
io_wait_time = cpu_times.iowait
irq_time = cpu_times.irq
soft_irq_time = cpu_times.softirq
guest_time = cpu_times.guest
guest_nice_time = cpu_times.guest_nice

# Save information to text file
file_name = "sys_time_info.txt" 
with open(file_name, 'w') as file:
    file.write(f'Time spent by normal processes executing in user mode: {user_time}\n')
    file.write('\n')
    file.write(f'Time spent by processes executing in kernel mode: {system_time}\n')
    file.write('\n')
    file.write(f'Time when system was idle: {idle_time}\n')
    file.write('\n')
    file.write(f'Time spent by priority processes executing in user mode: {priority_user_time}\n')
    file.write('\n')
    file.write(f'Time spent waiting for I/O to complete: {io_wait_time}\n')
    file.write('\n')
    file.write(f'Time spent for servicing hardware interrupts: {irq_time}\n')
    file.write('\n')
    file.write(f'Time spent for servicing software interrupts: {soft_irq_time}\n')
    file.write('\n')
    file.write(f'Time spent by other operating systems running in a virtualized environment: {guest_time}\n')
    file.write('\n')
    file.write(f'Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel: {guest_nice_time}\n')

print('System information saved to', file_name)
