a
    �w?a�  �                   @   sJ   d dl Z d dlZdZdd� Zdd� Zddd	�Zd
d� Zdd� Zdd� ZdS )�    N)
zmail.ruzinbox.ruzlist.ruzbk.ruzya.ruz
yandex.comz	yandex.uaz	yandex.ruz	gmail.comz	yahoo.comc                 C   s
   t �| �S )N)�random�choice)�list� r   �7/storage/emulated/0/Script Vip/toolso/SMS/randomData.py�random_service   s    r   c                  C   sB   t dd��} t�| �d } W d   � n1 s.0    Y  t�| �S )Nztoolso/SMS/names.json�r�names��open�json�loadr   r   )r	   r   r   r   �random_name   s    ,r   �   c                 C   s2   g }t | �D ]}|�tt�dd��� qd�|�S )N�   �	   � )�range�append�strr   �randint�join)�	int_rangeZnumbers�_r   r   r   �random_suffix   s    r   c                   C   s   t � t�  d t�t� S )N�@)r   r   r   r   �mailsr   r   r   r   �random_email(   s    r   c                   C   s   t � tdd� S )N�
   )r   )r   r   r   r   r   r   �random_password-   s    r   c                  C   sB   t dd��} t�| �d }W d   � n1 s.0    Y  t�|�S )Nztoolso/SMS/user_agents.jsonr   �agentsr
   )r    Zuser_agentsr   r   r   �random_useragent1   s    ,r!   )r   )	r   r   r   r   r   r   r   r   r!   r   r   r   r   �<module>   s   
	