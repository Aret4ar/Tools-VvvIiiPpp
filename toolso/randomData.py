a
    �w?a9  �                   @   s,   d dl Z d dlZdd� Zdd� Zdd� ZdS )�    Nc                  C   s4   g } t dd�D ]}| �tt�dd��� qd�| �S )Nr   �   �   ��   �.)�range�append�str�random�randint�join)Zip�_� r   �3/storage/emulated/0/Script Vip/toolso/randomData.py�	random_IP   s    r   c                  C   s<   t dd��} | �� } W d   � n1 s(0    Y  t�| �S )Nztoolso/other/referers.txt�r)�open�	readlinesr	   �choice)Zreferersr   r   r   �random_referer   s    &r   c                  C   sB   t dd��} t�| �d }W d   � n1 s.0    Y  t�|�S )Nztoolso/other/user_agents.jsonr   �agents)r   �json�loadr	   r   )r   Zuser_agentsr   r   r   �random_useragent   s    ,r   )r   r	   r   r   r   r   r   r   r   �<module>   s   