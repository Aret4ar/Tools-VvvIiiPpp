a
    g�`�  �                   @   s0   d dl Z d dlZd dlZd dlmZ dd� ZdS )�    N)�urlparsec                 C   s�   t | �}dj|d�}z^t�|�}t�d�j}dd� |�� D �}tt	|��D ]$}t
�|�t
�|| �v rJ W dS qJW n tjy�   td� Y dS 0 d S )	Nz{uri.netloc})Zuriz!https://www.cloudflare.com/ips-v4c                 S   s   g | ]}|� � �qS � )�rstrip)�.0�rowr   r   �0/storage/emulated/0/Script Vip/toolso/ipTools.py�
<listcomp>   �    z isCloudFlare.<locals>.<listcomp>TzV[1;31m[-][0mUnable to verify if victim's IP address belong to a CloudFlare's subnet!F)r   �format�socketZgethostbyname�requests�get�text�
splitlines�range�len�	ipaddressZ
ip_addressZ
ip_networkZgaierror�print)ZlinkZ
parsed_uri�domain�originZiprangeZipv4�ir   r   r   �isCloudFlare	   s    
r   )r   r   r   Zurllib.parser   r   r   r   r   r   �<module>   s   