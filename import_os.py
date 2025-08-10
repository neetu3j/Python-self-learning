import os


def run_command(command):
    return os.system(command)


run_command("date") # Display current date and time

run_command("df -h") # Display disk space usage

run_command("date +%Y-%m-%d") # Display current date in YYYY-MM-DD format

run_command("ls -l") # List files in the current directory with details

run_command("echo 'Hello, World!'")    # Print a simple message

run_command("uname -a") # Display system information

run_command("whoami")  # Display current user

run_command("pwd") # Print working directory

run_command("cat /etc/os-release") # Display OS release information

run_command("top -b -n 1") # Display system processes in batch mode

run_command("free -h") # Display memory usage in human-readable format

run_command("ps aux") # Display all running processes

run_command("ifconfig") # Display network interfaces and their configurations

run_command("ip addr show") # Display network interfaces and their configurations (alternative)

run_command("netstat -tuln") # Display listening ports and their status

run_command("ping -c 4 google.com") # Ping Google to check connectivity

run_command("traceroute google.com") # Trace the route to Google

run_command("curl -I https://www.google.com")   # Fetch HTTP headers from Google

run_command("wget --version") # Display wget version

run_command("git --version") # Display git version

run_command("python3 --version")    # Display Python version

run_command("java -version")    # Display Java version

run_command("node -v") # Display Node.js version

run_command("npm -v") # Display npm version

run_command("docker --version") # Display Docker version

run_command("kubectl version --client") # Display kubectl version

run_command("systemctl status") # Display systemd status

run_command("journalctl -xe") # Display system logs

run_command("df -i") # Display inode usage

run_command("mount") # Display mounted filesystems
run_command("lsblk") # Display block devices
run_command("lscpu") # Display CPU architecture information
run_command("lspci") # Display PCI devices
run_command("lsusb") # Display USB devices
run_command("dmesg | tail") # Display kernel ring buffer messages
run_command("history") # Display command history
run_command("crontab -l") # Display current user's cron jobs
run_command("uptime") # Display system uptime
run_command("last") # Display last logged in users
run_command("who") # Display currently logged in users
run_command("env") # Display environment variables
run_command("alias") # Display shell aliases
run_command("set") # Display shell variables and functions
run_command("export") # Display exported environment variables
run_command("uname -r") # Display kernel release
run_command("uname -m") # Display machine hardware name
run_command("hostname") # Display hostname


run_command("hostname -I")     # Display IP addresses assigned to the hostname

run_command("cat /proc/cpuinfo")           # Display CPU information

run_command("cat /proc/meminfo")           # Display memory information
run_command("cat /proc/version")       # Display kernel version

run_command("cat /proc/partitions")    # Display disk partitions
run_command("cat /proc/net/dev")      # Display network device statistics

run_command("cat /proc/sys/kernel/osrelease")     # Display kernel OS release
run_command("cat /proc/sys/kernel/hostname")     # Display kernel hostname



run_command("cat /proc/sys/kernel/version")     # Display kernel version

run_command("cat /proc/sys/kernel/ostype")         # Display kernel OS type
run_command("cat /proc/sys/kernel/pid_max")      # Display maximum PID
run_command("cat /proc/sys/kernel/random/boot_id")    # Display boot ID
run_command("cat /proc/sys/kernel/random/uuid")        # Display UUID
run_command("cat /proc/sys/kernel/random/entropy_avail")    # Display available entropy





        
