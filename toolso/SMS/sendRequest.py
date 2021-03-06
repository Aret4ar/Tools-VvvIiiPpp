a
    ?w?aA  ?                   @   sb   d dl Z d dlZd dlm  mZ d dlm  mZ ddd?Zddd?Zdd	? Z	G d
d? d?Z
dS )?    N?toolso/SMS/services.jsonc                 C   s<   t | d??}t?|?d W  d   ? S 1 s.0    Y  d S )N?r?services??open?json?load)?filer   ? r
   ?8/storage/emulated/0/Script Vip/toolso/SMS/sendRequest.py?getServices	   s    r   ?toolso/SMS/proxy.jsonc                 C   s<   t | d??}t?|?d W  d   ? S 1 s.0    Y  d S )Nr   ?proxyr   )r	   Zproxysr
   r
   r   ?	getProxys   s    r   c                 C   s   | ? d?d S )N?/?   )?split)?urlr
   r
   r   ?	getDomain   s    r   c                   @   s$   e Zd Zdd? Zdd? Zdd? ZdS )?Servicec                 C   s   || _ t? | _d| _d S )N?
   )?servicer   r   ?timeout)?selfr   r
   r
   r   ?__init__   s    zService.__init__c                 C   s?   d }zd}| j d }W n ty(   Y n0 zd}| j d }W n tyN   Y n0 |slt?d| j d i?}d}d|t?|d?t?? t?? t?	? d??
? D ]\}}|?||?}q?t?|?|fS )N?datar   r   ?"?   )?'z%phone%z%phone5%z%name%z%email%z
%password%)r   ?KeyErrorr   ?dumps?numberToolsZtransformPhone?
randomDataZrandom_nameZrandom_emailZrandom_password?items?replace?loads)r   ?phone?payload?dataType?old?newr
   r
   r   ?	parseData   s.    
?zService.parseDatac              	   C   s?  | j d }| ?|?\}}dddddt?? d?}z| j d }W n tyN   Y n*0 t?|?dd	???? D ]\}}|||< qfd
t	|? d }	d
t	|? d }
z?|dkr?t
j||| j|| jd?}nF|dkr?t
j||| j|| jd?}n$|dk?rt
j|d | j|| jd?}|jdk?rtd|	 ? n&|jdk?r6td|
 ? ntd|
 ? |jW S  t
jjt
jjf?yt   td|
 ? Y n$ t
jj?y?   td|
 ? Y n0 d S )Nr   ZXMLHttpRequestz
keep-alivezno-cachezgzip, deflate, br)zX-Requested-WithZ
ConnectionZPragmazCache-ControlzAccept-Encodingz
User-agent?headersr   r   z	Service (z) >> Message was sent!z) >> Message was not sent.r   )r   r   r,   ?proxiesr   )r   r   r,   r-   )r   r,   r-   ??   z[1;32m[+][0m i?  z[1;33m[!][0m )r   r+   r"   Zrandom_useragentr   r   r%   r$   r#   r   ?requestsZpostr   r   Zstatus_code?print?
exceptionsZReadTimeoutZConnectTimeout?ConnectionError)r   r&   r   r'   r(   r,   ZcustomHeaders?key?valueZokay?errorr   r
   r
   r   ?sendMessage>   sD    
?


zService.sendMessageN)?__name__?
__module__?__qualname__r   r+   r6   r
   r
   r
   r   r      s   r   )r   )r   )r   r/   Ztoolso.SMS.numberToolsZSMSr!   Ztoolso.SMS.randomDatar"   r   r   r   r   r
   r
   r
   r   ?<module>   s   

