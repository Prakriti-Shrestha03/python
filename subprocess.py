import os
import shutil
import subprocess

def generate_system_report(output_file):
    try:
        cwd=os.getcwd()
        disk_usage=shutil.disk_usage(cwd)
        
        system_info=subprocess.run(['systeminfo'],capture_output=True ,text=True).stdout
        with open(output_file,'w') as file:
            file.write(f"Current Working Directory: {cwd}\n")
            file.write(f"Disk Usage:\n")
            file.write(f"Total: {disk_usage.total/(1024**3):.2f} GB\n")
            file.write(f"Used: {disk_usage.used/(1024**3):.2f} GB\n")
            file.write(f"Free: {disk_usage.free/(1024**3):.2f} GB\n")
            file.wrie(f"System Information:\n{system_info}\n")
        print(f"System diagonostics report saved to '{output_file}'")
    except Exception as e:
        print(f"Error:{e}")

generate_system_report("sytem_report.txt")